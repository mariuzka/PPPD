import datetime
import os
from pathlib import Path

from bs4 import BeautifulSoup as bs
import requests

import src



def dates_between(date1, date2):
    """
    FUNCTION
    Returns all dates between the given dates incl. the given dates
    
    INPUT
    date1: start date (object type: datetime.date)
    date2: end date (object type: datetime.date)
    
    OUTPUT
    dates: list of dates between the given dates incl. the given dates
    """
    day_diff = (date2 - date1).days
    dates = [date1 + datetime.timedelta(days = i) for i in range(day_diff + 1)]
    return dates


def get_html(link):
    """
    FUNCTION
    Goes to a webpage and returns the html of the webpage
    
    INPUT
    link: a complete link to the homepage of interest
    
    OUTPUT
    html: beautiful soup html parser object
    """
    page = requests.get(link, timeout = 10)
    html = bs(page.content, "html.parser")
    return html


def get_dept_type(text):
    # extract the type of dept from name of dept

    text = text.lower()
    if "poliz" in text or "kriminal" in text:
        dept_type = "police"
    elif "feuer" in text:
        dept_type = "fire dept."
    elif "zoll" in text:
        dept_type = "customs"
    else:
        dept_type = "other"
    return dept_type


def create_folder(folder_path):
    # create folders
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

class logbook:
    def __init__(self, output_folder_name, name):
        self.output_folder_name = output_folder_name
        self.name = name
        self.logbook_file_path = Path.joinpath(
            src.PATH,
            "output_data",
            output_folder_name,
            "logs",
            self.name, 
            )
        create_folder(Path.joinpath(self.output_folder_name, "logs"))

    def write_entry(self, entry):
        str_datetime = str(datetime.datetime.now())
        entry = str_datetime + ":" + entry
        txt_file = open(self.logbook_file_path, "a", encoding="utf-8")
        txt_file.write("\n")
        txt_file.write(entry)
        txt_file.close()

def print_status(text):
    print(str(datetime.datetime.now()),":", text)