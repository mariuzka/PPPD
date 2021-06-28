from src import ppCleaner as ppc

years = [
    2015,
    2016,
    2017,
    2018,
    2019,
    2020,
    2021,
    ]

for year in years:
    ppc.html_to_df(
        state="baden-württemberg",
        year=str(year),
        output_folder_name="ppp_bw",
        )