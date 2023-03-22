from pathlib import Path

import pandas as pd

import src
from src.models import Base

# Drops and recreates DB
engine, Session = src.db_connection(init=False)
Base.metadata.drop_all(engine)
Base.metadata.create_all(bind=engine)

# Import legacy data into db
output_folder_name = "ppp_bw"


def import_newsroom_legacy_data(output_folder_name, engine):
    """
    Imports legacy csv files of newrooms to database
    """
    folder_path = Path.joinpath(
        src.PATH,
        "output_data",
        output_folder_name,
        "departments",
    )

    list_of_dfs = []
    for f in Path(folder_path).iterdir():
        df = pd.read_csv(Path.joinpath(folder_path, f.name))
        list_of_dfs.append(df)

    df_all = pd.concat(list_of_dfs, ignore_index=False)
    df_all = df_all.rename(columns={'newsroom_title': 'title',
                                    'newsroom_subtitle': 'subtitle',
                                    'name_of_dept': 'dept_name',
                                    'district_of_dept': 'dept_district',
                                    'state_of_dept': 'dept_state',
                                    'newsroom_link': 'link',
                                    'newsroom_weblinks': 'weblinks'})
    df_all = df_all.drop(columns=['scraping_datetime'])
    df_all = df_all.drop_duplicates()
    df_all = df_all.sort_values(by='newsroom_nr')
    df_all.to_sql(name="newsrooms", con=engine, if_exists="append", index=False)
    return (df_all)


import_newsroom_legacy_data(output_folder_name, engine)
