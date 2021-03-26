from src.ppRunner import ppRunnerFunctions as ppr

ppr.get_blaulicht_data(
    states="baden-württemberg",
    years=[2020, 2021],
    dept_type="police",
    output_folder_name="baden-württemberg",
)