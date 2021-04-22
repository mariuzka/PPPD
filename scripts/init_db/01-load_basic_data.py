import datetime as dt
from pathlib import Path

import src
from src.models import *

SCRAPER_DATA_PATH = "/home/lukas/Desktop/pppd_data/ppp_bw/articles/raw_article_html/"

def parse_newsroom(state, year, newsroom):
    global engine, Session
    session = Session()

    room = session.query(Newsroom).filter_by(id=newsroom.name).one_or_none()
    if not room:
        room = Newsroom(
            id = newsroom.name,
        )
        session.add(room)


    for file in newsroom.iterdir():
        _, published, i, crawled = file.name.rstrip(".txt").split("_")
        published = dt.datetime.strptime(published, "%Y-%m-%d")
        crawled = dt.datetime.strptime(crawled, "%Y-%m-%d-%H-%M-%S")
        content = file.read_text()

        article = Article(
            date = published,
            scraped_at = crawled,
            daily_index = i,
        )
        article.newsroom = room
        article.raw_html = ArticleHTML(html=content)
        session.add(article)

    session.commit()
    session.close()


def main():

    # create tables from src.models.Base
    Base.metadata.create_all(bind=engine)

    for state in Path(SCRAPER_DATA_PATH).iterdir():
        for year in state.iterdir():
            for newsroom in year.iterdir():
                parse_newsroom(state, year, newsroom)


if __name__ == "__main__":
    engine, Session = src.db_connection(init=False)
    main()
    engine.dispose()