from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import datetime
import time
import random
import os
from pathlib import Path

import src
from src import utils

LINK_BASE = "https://www.presseportal.de/"


###############################################################################
# functions for scraping on department level
###############################################################################

def get_dept_data():
    """
    FUNCTION
    This function collects informations of all departments listed on this page: 
    "https://www.presseportal.de/blaulicht/dienststellen".
    For every department found on the page, the scraper goes to the newsroom of 
    the dept and collects further information about the newsroom.
    The resulting dataset is the starting point for scraping the articles of all
    newsrooms. Articles and departments are linked by the "newsroom_nr".
    
    INPUT
    None
    
    OUTPUT
    data: a dataframe containing the informations about depts
    """
    
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
        
        # Get the name of the state
        name_of_state = s.find("a", class_ = "dienststellen-ankh")["name"]
        
        # find all departments in the state
        departments = s.find_all("div", class_ = "col four")
        
        # for every department in the state
        for d in departments:
            
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
            
            # store data in dict
            department_data = {
                "newsroom_nr": newsroom_nr,
                "name_of_dept": name_of_dept,
                "district_of_dept": district_of_dept,
                "state_of_dept": name_of_state,
                "newsroom_link": newsroom_link,
                "newsroom_title": newsroom_title,
                "newsroom_subtitle": newsroom_subtitle,
                "newsroom_weblinks": newsroom_weblinks,
                "dept_type": dept_type,
                "scraping_datetime": datetime.datetime.now(),
                }
            
            # append dict to data-list
            data.append(department_data)
        
    df = pd.DataFrame(data)
    utils.print_status("finished scraping list of depts.")
    return df


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
    article_links = [article["data-url"] for article in articles]
    article_links = ["https://www.presseportal.de/" + link for link in article_links]
    
    return article_links
            

def one_day_of_a_newsroom(newsroom_nr, date, blaulicht):
    """
    FUNCTION
    Goes to webpage of the newsroom which is referenced by its newsroom_nr,
    searches for all articles of a day (by using the search_by_newsroom_and_date()),
    loads each article found and extracts the information from the html (by using
    extract_article_data()).
    
    INPUT
    newsroom_nr: ...
    date: ...
    blaulicht:  Logical Value. True if the newsroom is part of the Blaulicht section
                on presseportal.
    
    OUTPUT
    output_dict: dict that contains a list with the unmodified html of every article of that day
                   and a list of dicts with informations extracted from each article-html
        raw_html: list of the raw html
        extracted_data: list of dicts each containing information about one article of that day
    
    """

    output_dict = {
        "extracted_data": [],
        "raw_html": [],
        }
    
    # build link to newsroom
    newsroom_link = LINK_BASE + ("blaulicht/nr/" if blaulicht else "nr/") + newsroom_nr
    
    # get all links to articles
    article_links_per_day = search_by_newsroom_and_date(newsroom_link, date)
    
    # for each article link
    for i, link in enumerate(article_links_per_day):
        article_html = utils.get_html(link)
        output_dict["raw_html"].append(str(article_html))

    return output_dict


def error_handler(
    error_counter, 
    error_infos, 
    sleep_time = 25, 
    max_retries = 10,
    ):
    
    """
    FUNCTION
    This function is called in presseportal_crawler().
    If an error occurs, it either freezes the program for 20 secs (sleep_time) 
    or inserts informations about the error into the database.
    What happens depends on the value of error_counter, which counts how often
    the error_handler was called for this specific error.
    
    INPUT
    error_counter: integer
    error_infos: dict which contains informations about the error
    sleep_time: amount of seconds, the program is freezed after an error occurs
    max_retries: maximum number of tries the program tries to execute the failing command
    
    
    OUTPUT
    keep_running: Logical Value. True if the maximum number of retries was not reached.
    """
    
    print(" ")
    print("####################################################")
    print(" ERROR ", " /// ", "Retries: ", error_counter, "/", max_retries)
    print(" ")
    print(error_infos["error_type"])
    print(" ")
    print("####################################################")
    print(" ")
    
    if error_counter <= max_retries:
        time.sleep(sleep_time)
        keep_running = True
    
    else:
        print(" ")
        print("ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(" ")
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
    end date as inputs and collects all articles from all newsrooms for every date.
    It uses the functions defined above.
    In addition it inserts the collected data into the databank.
    If an error occurs while scraping the data the function waits am moment and then
    tries it again for 20 times.    
    
    INPUT
    newsroom_nr: ...
    start_date: start date as a datetime object
    end_date: end date as a datetime object
    blaulicht: are the newsroom part of the Blaulicht section on Presseportal?
    
    OUTPUT
    None
    """
    
    ###########################################################################
    # step 1: check and transform input-values
    ###########################################################################
    
    # put link-number in a list, if it was inserted as a single number
    list_of_newsroom_nr = ( [newsroom_nr] if type(newsroom_nr) in [int, str] else newsroom_nr )
    
    # change every link-number to string
    list_of_newsroom_nr = [str(nr) for nr in list_of_newsroom_nr]
    
    # if no end_date was inserted, give it the same value as the start_date
    end_date = (start_date if end_date == "same" else end_date)
    
    # create list of dates
    dates_to_scrape = utils.dates_between(start_date, end_date)

    # measures of progress
    number_of_newsroom_dates = len(list_of_newsroom_nr) * len(dates_to_scrape)
    done = 0

    ###########################################################################
    # step 2: collect every article for every day and every newsroom
    ###########################################################################
    
    # for each newsroom respectively newsroom_nr
    for newsroom_counter, newsroom_nr in enumerate(list_of_newsroom_nr):
        utils.print_status("scraping articles from newsroom " + str(newsroom_nr))
            
        # for every date
        for date in dates_to_scrape:
            time.sleep(0.01)
            
            # create year data folder
            year_data_folder_path = Path.joinpath(data_folder_path, str(date.year))
            utils.create_folder(year_data_folder_path)

            error_counter = 0
            try_it = True
            
            while try_it == True:
                
                try:
                    # get daily data
                    data_of_one_day = one_day_of_a_newsroom(newsroom_nr, date, blaulicht)

                     # save raw html on disk
                    for i, raw_html in enumerate(data_of_one_day["raw_html"]):
                        str_date = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
                        now = datetime.datetime.now()
                        str_scraping_datetime = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute)
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
                            
                        # Datei speichern
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
                    
                    try_it = error_handler(error_counter, error_infos)
                    
    utils.print_status("finished scraping articles.")

def run_ppScraper(
    state,
    dept_type,
    output_folder_name,
    year = None,
    start_date = None,
    end_date = None,
    update=True,
    dept_df=None,
    ):

    assert year or start_date and end_date
    assert dept_type in ("police", "fire dept.", "customs", "other")
    
    if year:
        start_date = datetime.date(year, 1, 1)
        end_date = datetime.date(year, 12, 31)

    data_folder = Path.joinpath(src.PATH, "output_data", output_folder_name)
    state_data_folder = Path.joinpath(data_folder, "PMs", "raw_article_html", state)
    
    utils.create_folder(Path.joinpath(src.PATH, "output_data"))
    utils.create_folder(data_folder)
    utils.create_folder(Path.joinpath(data_folder, "departments"))
    utils.create_folder(Path.joinpath(data_folder, "PMs"))
    utils.create_folder(Path.joinpath(data_folder, "PMs", "raw_article_html"))
    utils.create_folder(state_data_folder)

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