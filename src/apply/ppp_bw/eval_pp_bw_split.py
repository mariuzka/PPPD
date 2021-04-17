from pathlib import Path

import pandas as pd 

import src
from src import ppSplitter

datasets_path = Path.joinpath(src.PATH, "output_data", "ppp_bw", "PMs", "state_datasets", "baden-württemberg")

for year in ["2015", "2016","2017", "2018", "2019", "2020", "2021"]:
    df = pd.read_csv(Path.joinpath(datasets_path, "baden-württemberg_" + year + ".csv"))
    df_split = pd.read_csv(Path.joinpath(datasets_path, "baden-württemberg_" + year + "_split.csv"))
    ppSplitter.eval_splits(df, df_split)