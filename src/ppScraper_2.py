# -*- coding: utf-8 -*-

import datetime
import os
from pathlib import Path
import random
import time

from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

import src
from src import DEVEL_MODE
from src import utils
from src.models import Newsroom, Newsroom_visit

from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation


LINK_BASE = "https://www.presseportal.de/"

###############################################################################
# functions for scraping on department level
###############################################################################

def get_dept_data():
    """
    FUNCTION
    This function collects informations of all departments listed on this page: 
    "https://www.presseportal.de/blaulicht/dienststellen".
    For each department found on the page, the scraper visits the newsroom of 
    the dept and collects further information about the newsroom and writes it
    to tabele newsrooms.
    The function tracks each subequent scraping in table newsroom_visits. 
    If Newsroom properties change, a new instance is added. 
    
    INPUT
    None
    
    OUTPUT
    If Newsroom not in DB or does not meet unique constraint: 
    add db entry for Newsroom and add entry for Newsroom_visit.
    If Newsroom unchanged, only add entry for Newsroom_visit. 

    Todo: Initiate task for queue: Scrape Articles for Newsrooms 
    """
    
    engine, Session = src.db_connection(init=False)
    session = Session()

    utils.print_status("start scraping list of departments.")

    # website containing overview of departments on presseportal/blaulicht
    html = utils.get_html("https://www.presseportal.de/blaulicht/dienststellen")
    
    # table with all departments
    dienstellen_container = html.find("div", class_ = "card dienststellen-container")
    
    # subset content by state
    states = dienstellen_container.find_all("div", class_ = "row")
    states = [state for state in states if state.find("a", class_ = "dienststellen-ankh")]
    
    # list for storing department level data
    data = []
    
    # for every state
    for i, s in enumerate(states):
        pass
        # Get the name of the state
        name_of_state = s.find("a", class_ = "dienststellen-ankh")["name"]
        
        # For development
        if DEVEL_MODE:
            if name_of_state != "baden-württemberg":
                continue
        
        # find all departments in the state
        departments = s.find_all("div", class_ = "col four")


        # for every department in the state
        for d in departments:
            pass           
            try:
                session = Session()

                # get name of dept
                name_of_dept = d.find("a")["title"]
                name_of_dept = name_of_dept.replace("weiter zum newsroom von","")
                
                dept_type = utils.get_dept_type(name_of_dept)
                
                # get district of dept
                district_of_dept = d.find("a").text
                
                # get newsroom_nr (number in "blaulicht-link")
                newsroom_nr = d.find("a")["href"].split("/")[-1]
                
                # build newsroom-link, go to newsroom and collect further data about newsroom
                newsroom_link = LINK_BASE + "blaulicht/nr/" + str(newsroom_nr)
                newsroom_html = utils.get_html(newsroom_link)
                
                # title of newsroom
                newsroom_title = newsroom_html.find("h1", class_ = "newsroom-title").text
                
                # subtitle of newsroom
                newsroom_subtitle = newsroom_html.find("div", class_ = "newsroom-extra").text
                
                # weblinks
                newsroom_weblinks = newsroom_html.find("div", class_ = "newsroom-extra").find_all("a")
                newsroom_weblinks = [[link["title"], link["href"]] for link in newsroom_weblinks]
                
                # Newsroom
                newsroom = Newsroom(
                    newsroom_nr = newsroom_nr,
                    title = newsroom_title,
                    subtitle = newsroom_subtitle,
                    dept_name = name_of_dept,
                    dept_district = district_of_dept,
                    dept_state = name_of_state,
                    link = newsroom_link,
                    weblinks = str(newsroom_weblinks),
                    dept_type = dept_type,
                )

                add_newsrooms_and_visits_to_db(newsroom)

            except Exception as error:
                print("WARNING: error occured.")
                print(error)
        
    utils.print_status("finished scraping list of depts.")


def add_newsrooms_and_visits_to_db(newsroom):
    """
    Handles unique constraint exceptions for Newsrooms

    Newsrooms are added to the database by adding a Newsroom_visit that backpopulates
    to the related Newsroom.
    Newsrooms are unique, as long as all properties are equal (see UniqueConstraint
    in model definition). As properties of Newsrooms may change, a new instance with
    a new PK is added to the db.
    For a revisit (a newerly Newsroom_visit) of an already existing instance of Newsroom,
    a unique constraint exceptions is raised - and catched within this function.
    In this case, the Newsroom_visit gets the existing Newsroom instance as foreign key.
    """

    session = Session()

    nsroom = session.query(Newsroom).filter_by(
                newsroom_nr=newsroom.newsroom_nr,
                title=newsroom.title,
                subtitle=newsroom.subtitle,
                dept_name=newsroom.dept_name,
                dept_district=newsroom.dept_district,
                dept_state=newsroom.dept_state,
                link=newsroom.link,
                weblinks=newsroom.weblinks,
                dept_type=newsroom.dept_type,
            ).one_or_none()
    
    if nsroom is not None:
        newsroom = nsroom

    scraping_datetime = datetime.datetime.now()
    newsroom_visit = Newsroom_visit(scraping_datetime=scraping_datetime)
    newsroom_visit.newsroom = newsroom
    session.add(newsroom_visit)
    try:
        session.flush()
    except IntegrityError as e:
        session.rollback()
        session.close()
        if isinstance(e.orig, UniqueViolation):
            print("Newsroom already exists...")
            # Check if Newsroom exists ()
            session = Session()
            q = session.query(Newsroom).filter_by(
                newsroom_nr=newsroom.newsroom_nr,
                title=newsroom.title,
                subtitle=newsroom.subtitle,
                dept_name=newsroom.dept_name,
                dept_district=newsroom.dept_district,
                dept_state=newsroom.dept_state,
                link=newsroom.link,
                weblinks=newsroom.weblinks,
                dept_type=newsroom.dept_type,
            )
            # If Newsroom exists
            if session.query(q.exists()).scalar():
                print("Adding Newsroom_visit...")
                newsroom_visit = Newsroom_visit(scraping_datetime=scraping_datetime)
                newsroom_visit.newsroom = q.first()
                session.add(newsroom_visit)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
    session.close()


###############################################################################
# functions for scraping on article level
###############################################################################

def search_by_newsroom_and_date(newsroom_link, date):
    """
    FUNCTION
    Goes to a newsroom and searches for all articles for the given date/day.
    Returns a list containing the links to the articles.
    
    INPUT
    newsroom_link: complete link to the newsroom page
    date: a date of a day (as a datetime object???)
        
    OUTPUT
    article_links: a list of links to the articles of the day in the newsroom
    """
    
    date = str(date)
    search_link = newsroom_link + "/?startDate=" + date + "&endDate=" + date
    html = utils.get_html(search_link)
    articles = html.find_all("article", class_ = "news")
    article_links = [article["data-url-ugly"] for article in articles]
    article_links = [link.replace("@", "/") for link in article_links]
    
    
    return article_links
            

def one_day_of_a_newsroom(newsroom_nr, date, blaulicht):
    """
    FUNCTION
    Goes to webpage of the newsroom which is referenced by its newsroom_nr,
    searches for all articles of a day (by using the search_by_newsroom_and_date()),
    saves each raw html in a list and returns this list.
    
    INPUT
    newsroom_nr: ...
    date: ...
    blaulicht:  Logical Value. True if the newsroom is part of the Blaulicht section
                on presseportal.
    
    OUTPUT
    raw_html_list: list of the raw html
    """

    raw_html_list = []

    # build link to newsroom
    newsroom_link = LINK_BASE + ("blaulicht/nr/" if blaulicht else "nr/") + newsroom_nr
    
    # get all links to articles
    article_links_per_day = search_by_newsroom_and_date(newsroom_link, date)
    
    # for each article link
    for i, link in enumerate(article_links_per_day):
        # get html
        article_html = utils.get_html(link)
        raw_html_list.append(str(article_html))

    return raw_html_list


def error_handler(
    error_counter, 
    error_infos, 
    sleep_time = 25, 
    max_retries = 10,
    ):
    
    """
    FUNCTION
    This function is called in presseportal_crawler().
    If an error occurs, it freezes the program for X secs (sleep_time) and then tries the same task again.
    If the same tasks fails too often (>max_retries), the task is skipped and informations about the error are saved
    in an error file.
    
    INPUT
    error_counter: integer
    error_infos: dict which contains informations about the error
    sleep_time: amount of seconds the program is freezed after an error occurs
    max_retries: maximum number of tries the program tries to execute the failing command
    
    OUTPUT
    keep_running: Logical Value. True if the maximum number of retries was not reached.
    """
    
    if error_counter <= max_retries:
        time.sleep(sleep_time)
        keep_running = True
    
    else:
        print(" ")
        print("ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(" ")
        
        txt_file = open("errors.txt", "a", encoding = "utf-8")
        txt_file.write("\n")
        txt_file.write(str(error_infos))
        txt_file.close()
        
        keep_running = False
    
    return keep_running


def presseportal_crawler(
    newsroom_nr,
    start_date,
    data_folder_path,
    end_date = "same",
    update = True,
    blaulicht = False,
    ):

    """
    FUNCTION
    Main function for scraping articles from presseportal.
    It takes a single newsroom_nr or a list of newsrooms_nrs and the start date and 
    end date as inputs and collects all articles from all newsrooms for each given date.
    It saves the raw html files in the given folder (data_folder_path).
    If an error occurs while scraping the data the function waits a moment and then
    tries it again for X times.    
    
    INPUT
    newsroom_nr: ...
    start_date: start date as a datetime object
    data_folder_path: path to folder where the collected data shall be saved
    end_date: end date as a datetime object
    blaulicht: are the newsroom part of the Blaulicht section on Presseportal?
    
    OUTPUT
    None
    """
    
    # create logbook
    logbook = utils.Logbook(data_folder_path, "log_"+utils.get_str_dt()+".txt")

    # put link-number in a list, if it was inserted as a single number
    list_of_newsroom_nr = ( [newsroom_nr] if type(newsroom_nr) in [int, str] else newsroom_nr )
    
    # change every link-number to string
    list_of_newsroom_nr = [str(nr) for nr in list_of_newsroom_nr]
    
    # if no end_date was inserted, give it the same value as the start_date
    end_date = (start_date if end_date == "same" else end_date)
    
    # create list of dates
    dates_to_scrape = utils.dates_between(start_date, end_date)

    ###########################################################################
    # collect every article for every day and every newsroom
    ###########################################################################
    
    # for each newsroom respectively newsroom_nr
    for newsroom_counter, newsroom_nr in enumerate(list_of_newsroom_nr):
        logbook.write_entry("scraping articles from newsroom " + str(newsroom_nr))
            
        # for every date
        for date in dates_to_scrape:
            time.sleep(0.01)
            
            # create year data folder
            year_data_folder_path = Path.joinpath(data_folder_path, str(date.year))
            utils.create_folder(year_data_folder_path)

            # reset error counter
            error_counter = 0
            try_it = True
            
            while try_it == True:
                
                try:
                    # get daily html data
                    html_of_one_day = one_day_of_a_newsroom(newsroom_nr, date, blaulicht)

                     # save raw html on disk
                    for i, raw_html in enumerate(html_of_one_day):
                        # name the html file
                        str_date = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
                        str_scraping_datetime = utils.get_str_dt()
                        html_file_name = newsroom_nr + "_" + str_date + "_" + str(i) + "_" + str_scraping_datetime + ".txt"
                        
                        # Ordner für newsroom_nr anlegen
                        newsroom_year_data_folder_path = Path.joinpath(year_data_folder_path, str(newsroom_nr))
                        utils.create_folder(newsroom_year_data_folder_path)
                        
                        # check if article html already exists
                        html_files = [html_file.rsplit("_", 1)[0] for html_file in os.listdir(newsroom_year_data_folder_path)]
                        if html_file_name.rsplit("_", 1)[0] in html_files:
                            duplicate = True  
                        else:
                            duplicate = False
                            
                        # save file
                        if not update or (not duplicate and update):
                            file_path = Path.joinpath(newsroom_year_data_folder_path, html_file_name)
                            txt_file = open(file_path, "w", encoding = "utf-8")
                            txt_file.write(raw_html)
                            txt_file.close()
    
                    try_it = False
                
                except Exception as error:
                    error_counter += 1
                    error_infos = {
                        "error_type": error,
                        "newsroom_nr": newsroom_nr,
                        "date": date,
                        "error_datetime": datetime.datetime.now(),
                        }
                    logbook.write_entry("error_counter:" + " " + str(error_counter) + " " + str(error_infos))
                    try_it = error_handler(error_counter, error_infos)
                    
    logbook.write_entry("finished scraping articles.")


def scrape_blaulicht(
    state,
    dept_type,
    output_folder_name,
    year = None,
    start_date = None,
    end_date = None,
    update=True,
    dept_df=None,
    ):
    """
    FUNCTION
    Simplifies the scraping of "presseportal.de/blaulicht" by combining functions for scraping
    on department level and on article level.
    Use this function to get the raw html of all blaulicht-articles for a certain state/department-type/period.

    INPUT
    state: The federal state of interest
    dept_type: The type of departments that shall be scraped. Types are "police", "fire dept.", "customs", "other"
    output_folder_name: Name of the folder in which all the data should be stored.
    year: The year of interest. You can either define a year or start_date and end_date.
    start_date: ...
    end_date: ...
    update: If True: A certain html file will be saved only if there is no html file for the same article yet.
    dept_df: If you want to use an already downloaded dataframe containing department level informations 
                (output of the function "get_dept_data()"), insert it here.

    OUTPUT
    None
    """

    assert year or start_date and end_date
    assert dept_type in ("police", "fire dept.", "customs", "other")
    
    state = state.lower()

    if year:
        start_date = datetime.date(year, 1, 1)
        end_date = datetime.date(year, 12, 31)

    # create some important paths
    data_folder = Path.joinpath(src.PATH, "output_data", output_folder_name)
    state_data_folder = Path.joinpath(data_folder, "articles", "raw_article_html", state)
    
    # create folder structure
    utils.create_folder(Path.joinpath(src.PATH, "output_data"))
    utils.create_folder(data_folder)
    utils.create_folder(Path.joinpath(data_folder, "departments"))
    utils.create_folder(Path.joinpath(data_folder, "articles"))
    utils.create_folder(Path.joinpath(data_folder, "articles", "raw_article_html"))
    utils.create_folder(state_data_folder)

    # No dept_df inserted?
    if not isinstance(dept_df, pd.DataFrame):
        # scrape department data
        dept_df = get_dept_data()
        dept_df_file_name = "depts_" + str(datetime.datetime.now().date()) + ".csv"
        dept_df.to_csv(Path.joinpath(data_folder, "departments", dept_df_file_name), index=False)
    
    # filter department data
    filtered_dept_df = dept_df[dept_df["dept_type"] == dept_type]
    filtered_dept_df = filtered_dept_df[filtered_dept_df["state_of_dept"] == state]
    
    # get newsroom nrs of departments
    list_of_newsroom_nrs = list(filtered_dept_df["newsroom_nr"])

    # scrape article data
    presseportal_crawler(
        newsroom_nr = list_of_newsroom_nrs,
        start_date = start_date,
        end_date = end_date,
        data_folder_path = state_data_folder,
        blaulicht = True,
        update=update,
        )
