import datetime

import src
from src.ppScraper import ppScraperFunctions as pps
from src.ppCleaner import ppCleanerFunctions as ppc

def get_blaulicht_data(
    states,
    years,
    dept_type,
    output_folder_name,
    update=True,
    split_reports=False,
    ):

    if split_reports:
        splittable_states = (
            "baden-württemberg",
        )
        for s in states:
            assert state in splittable_states, "For this state there is no split-function() available."

    if not isinstance(states, list):
        states = [states]
    
    if not isinstance(years, list):
        years = [years]

    for s in states:
        for y in years:
            
            pps.run_ppScraper(
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
            
            if split_reports == True:
                if state == "baden-württemberg":
                    split_reports_bw(
                        state=s,
                        year=y,
                        output_folder_name=output_folder_name,
                    )

def export_dataset(states, years, output_folder_name, dataset_name):
    pass