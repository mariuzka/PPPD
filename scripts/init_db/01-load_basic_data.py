from pathlib import Path

import src
from src.models import *

SCRAPER_DATA_PATH = "/home/lukas/Desktop/pppd_data/ppp_bw/articles/raw_article_html/"

def main():

    #spark_session = src.spark_session()

    for state in Path(SCRAPER_DATA_PATH).iterdir():
        print(state.name)


if __name__ == "__main__":
    main()