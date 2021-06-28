from pathlib import Path

import pandas as pd 

import src
from src import ppSplitter

datasets_path = Path.joinpath(src.PATH, "output_data", "ppp_bw", "articles", "state_datasets", "baden-württemberg")

years = [
    "2015", 
    "2016",
    "2017", 
    "2018", 
    "2019", 
    "2020", 
    "2021",
    ]

for year in years:
    df = pd.read_csv(Path.joinpath(datasets_path, "baden-württemberg_" + year + ".csv"))
    df_split = pd.read_csv(Path.joinpath(datasets_path, "baden-württemberg_" + year + "_split.csv"))
    ppSplitter.eval_splits(df=df, df_split=df_split, doc_name="eval_split_bw_"+year, n=False, frac=0.001)
