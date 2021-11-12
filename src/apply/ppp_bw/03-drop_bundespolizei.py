# -*- coding: utf-8 -*-

from pathlib import Path

import pandas as pd 

import src
from src import ppCleaner as ppc

datasets_path = Path.joinpath(src.PATH, "output_data", "ppp_bw", "articles", "state_datasets", "baden-württemberg")

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
    df = pd.read_csv(Path.joinpath(datasets_path, "baden-württemberg_" + str(year) + ".csv"))
    
    len1 = len(df)
    
    df = df[df["newsroom"].str.contains("Bundespolizei")==False]
    df = df.reset_index(drop=True)
    
    len2 = len(df)
    
    print(len1, len2)
    
    df.to_csv(Path.joinpath(datasets_path, "baden-württemberg_" + str(year) + ".csv"))
