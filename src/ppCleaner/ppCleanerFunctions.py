import os
from pathlib import Path

from bs4 import BeautifulSoup as bs
import pandas as pd

import src
from src.ppCleaner import splitter
from src import utils


def extract_article_data(html, newsroom_nr):
    """
    FUNCTION
    Extracts some specific informations from the html of an article page.
    It returns a dict containing the informations together with the newsroom_nr.
    
    INPUT
    html: beautiful soup html parser object
    newsroom_nr: number in the newsroom link / newsroom-id
    
    OUTPUT
    data: dict containing the extracted informations
    """
    
    # institution / newsroom
    institution = html.find("a", "story-customer").text
    
    # datetime of publishing
    dt = html.find("p", class_ = "date").text
    dt = dt.split("–")
    
    date = dt[0].strip().split(".")
    year = date[2]
    month = date[1]
    day = date[0]
    
    time = dt[1].strip().split(":")
    hour = time[0]
    minute = time[1]
    
    date = "-".join([year, month, day])
    time = ":".join([hour, minute])
    dt = " ".join([date, time])
    

    # get the main location of event
    location = html.find("a", class_ = "story-city event-trigger").text
    
    # story header
    header = html.find("h1").text
    
    # story text (at this point the date, the institution etc. are still included)
    text = html.find("div", class_ = "card")
    text = text.find_all("p")
    text = [p.text for p in text]
    text = "\n".join(text)
    
    # get tags used by presseportal
    tags = html.find_all("ul", class_ = "tags")
    
    # tags for locations
    location_tags = tags[0]
    location_tags = location_tags.find_all("li")
    location_tags_names = [tag.find("a").text for tag in location_tags]
    location_tags_scores = [tag["data-score"] for tag in location_tags]
    
    # tags for topics in story
    topic_tags = tags[1]
    topic_tags = topic_tags.find_all("li")
    topic_tags_names = [tag.find("a").text for tag in topic_tags]
    topic_tags_scores = [tag["data-score"] for tag in topic_tags]
    
    data = {
        # "scraping_datetime": datetime.datetime.now(),
        "newsroom_nr": newsroom_nr,
        "from_presseportal": 1,
        "newsroom": institution,
        "date_release": dt,
        "location": location,
        "header": header,
        "text": text,
        "location_tags_names": location_tags_names,
        "location_tags_scores": location_tags_scores,
        "topic_tags_names": topic_tags_names,
        "topic_tags_scores": topic_tags_scores,
        }
    
    return data

def html_to_df(state, year, output_folder_name):
    utils.print_status("start converting raw html files to datasets.")
    
    year = str(year)

    state_newsroom_datasets = []

    output_folder_path = Path.joinpath(src.PATH, "output_data", output_folder_name)

    utils.create_folder(Path.joinpath(output_folder_path, "PMs", "state_datasets"))

    state_year_data_folder_path = Path.joinpath(
        output_folder_path,
        "PMs",
        "raw_article_html",
        state,
        year,
    )

    # list of subfolders for each newsroom
    newsroom_folder_names = os.listdir(state_year_data_folder_path)
    
    number_of_newsrooms = len(newsroom_folder_names)
    
    # for each newsroom
    for i, newsroom_folder_name in enumerate(newsroom_folder_names):
        # progress
        overall_progress = round(((i+1)/number_of_newsrooms)*100)
        utils.print_status("start converting raw html files to datasets for newsroom " + str(newsroom_folder_name))

        # build path to newsroom-folder
        newsroom_folder_path = Path.joinpath(state_year_data_folder_path, newsroom_folder_name)
        
        # list of all files in this newsroom-folder
        list_of_html_files = os.listdir(newsroom_folder_path)
        
        # list for storing the newsroom_data
        newsroom_dataset = []
        
        # for each file in newsroom-folder
        for j, html_file_name in enumerate(list_of_html_files):
            
            number_of_html_files = len(list_of_html_files)
            
            # build path to this file
            html_file_path = Path.joinpath(newsroom_folder_path, html_file_name)
            
            # if it is a txt-file
            if str(html_file_path).endswith(".txt"):
                    
                # open, read, close
                file = open(html_file_path, "r", encoding = "utf-8")
                html = file.read()
                file.close()
                
                # convert to a bs-object
                html = bs(html, "html.parser")
                
                try:
                    # extract informations from html
                    extracted_data = extract_article_data(html, newsroom_folder_name)
                    
                    scraping_date_time = html_file_name.split("_")[-1].strip(".txt")
                    extracted_data.update({"scraping_date_time": scraping_date_time})
                
                    # append result (a dict) to list
                    newsroom_dataset.append(extracted_data)
                    
                except Exception as error:
                    print(error, state, html_file_path)
                    
        # convert result of the current newsroom to dataframe
        newsroom_dataset = pd.DataFrame(newsroom_dataset)
        newsroom_dataset["state"] = state
        
        state_newsroom_datasets.append(newsroom_dataset)
        
    state_year_df = pd.concat(state_newsroom_datasets)
    
    state_datasets_folder_path = Path.joinpath(
        output_folder_path,
        "PMs", 
        "state_datasets", 
        state,
        )
    utils.create_folder(state_datasets_folder_path)
    
    state_year_dataset_file_name = state + "_" + year + ".csv"
    state_year_df.to_csv(
        Path.joinpath(state_datasets_folder_path, state_year_dataset_file_name),
        index = False,
        )
    
    utils.print_status("finished converting raw html files to datasets.")


def split_reports_bw(state, year, output_folder_name):
    year = str(year)
    
    # load data
    folder_path = Path.joinpath(
        src.PATH, 
        "output_data",
        output_folder_name,
        "PMs", 
        "state_datasets", 
        state,
    )

    df = pd.read_csv(Path.joinpath(folder_path, state + "_" + year + ".csv"))
    df_split = splitter.split_reports_in_df(df, "text")
    df_split.to_csv(Path.joinpath(folder_path, state + "_" + year + "_split.csv"), index = False)