import datetime

import src
from src import ppScraperFunctions as pps
from src import ppCleanerFunctions as ppc


def get_blaulicht_data(
    states,
    years,
    dept_type,
    output_folder_name,
    update=True,
    ):

    """
    FUNCTION
    Collects press releases posted on presseportal.de/blaulicht.
    Extracted data is saved in dataframes.
    Raw html is also saved.
    Make sure you have a stable internet connection and enough free space on your hard drive.

    INPUT
    states: The state of interest (str) or a list of states of interest.
    years: The year of interest (int) or a list of years of interest.
    dept_type: The department type of interest ("police", "fire dept.", "customs", "other").
    output_folder_name: The name of the folder in which all the data shall be stored.
    update: If True: No already existing articles are saved.

    OUTPUT
    None
    """

    if not isinstance(states, list):
        states = [states]
    
    if not isinstance(years, list):
        years = [years]

    for s in states:
        for y in years:
            
            pps.scrape_blaulicht(
                state=s,
                year=y,
                dept_type=dept_type,
                output_folder_name=output_folder_name,
                update=update,
                )
    
            ppc.html_to_df(
                state=s,
                year=y,
                output_folder_name=output_folder_name,
                )
            