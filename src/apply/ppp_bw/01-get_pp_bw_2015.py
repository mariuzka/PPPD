from src import ppRunner as ppr

ppr.get_blaulicht_data(
    states="baden-württemberg",
    years=2015,
    dept_type="police",
    output_folder_name="ppp_bw",
)
