import src
# from src.models import *
from src.ppCleaner import splitted_reports_csv_to_db

engine, Session = src.db_connection(init=False)

years = range(2015, 2022)
output_folder_name = "ppp_bw"
state = "baden-württemberg"

for y in years:
    splitted_reports_csv_to_db(output_folder_name, state, y, engine)
