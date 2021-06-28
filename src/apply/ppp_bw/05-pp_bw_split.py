from src import ppCleaner as ppc

STATE = "baden-württemberg"
OUTPUT_FOLDER_NAME = "ppp_bw"

years = [
    2015,
    2016,
    #2017,
    #2018,
    #2019,
    #2020,
    #2021,
    ]

for year in years:
    ppc.split_reports_bw(state=STATE, year=year, output_folder_name=OUTPUT_FOLDER_NAME)
