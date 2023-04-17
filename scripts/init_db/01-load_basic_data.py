import datetime as dt
from pathlib import Path

from bs4 import BeautifulSoup as bs
from sqlalchemy import Index
from sqlalchemy.exc import ProgrammingError

import src
from src import ppCleaner as ppc
from src.models import Article, ArticleHTML, Newsroom, Newsroom_visit
from src.ppSplitter import split_articles_and_add_reports_to_db

DATA_FOLDER_NAME = "ppp_bw"


def parse_newsroom(state, year, newsroom):
    global engine, Session
    session = Session()

    room = session.query(Newsroom).filter_by(newsroom_nr=newsroom.name).one_or_none()
    if not room:
        room = Newsroom(
            newsroom_nr=newsroom.name,
        )
        session.add(room)

    for file in newsroom.iterdir():
        newsroom_nr, published, i, crawled = file.name.rstrip(".txt").split("_")

        published = dt.datetime.strptime(published, "%Y-%m-%d")
        crawled = dt.datetime.strptime(crawled, "%Y-%m-%d-%H-%M-%S")

        content = file.read_text(encoding="utf-8")

        html = bs(content, "html.parser")

        article_data = ppc.extract_article_data(html, newsroom_nr)

        article = Article(
            date=published,
            scraped_at=crawled,
            daily_index=i,
            article_link=article_data["article_link"],
            newsroom_nr=newsroom_nr,
            location=article_data["location"],
            header=article_data["header"],
            text=article_data["text"],
            location_tags_names=article_data["location_tags_names"],
            location_tags_scores=article_data["location_tags_scores"],
            topic_tags_names=article_data["topic_tags_names"],
            topic_tags_scores=article_data["topic_tags_scores"],
        )
        article.newsroom = room
        article.newsroom_visit = session.query(Newsroom_visit).filter_by(newsroom_id=room.id).one_or_none()
        article.article_html = ArticleHTML(html=content)
        session.add(article)
        split_articles_and_add_reports_to_db(article, session)

    session.commit()
    session.close()


def add_final_indexes():
    global engine

    indexes = [
        Index("article_newsroom_ix", Article.newsroom_id),
        Index("article_date_ix", Article.date),
    ]

    for index in indexes:
        try:
            index.create(bind=engine)
        except ProgrammingError:
            pass


def main():

    # create tables from src.models.Base
    # Base.metadata.create_all(bind=engine)

    data_folder_path = Path.joinpath(
        src.PATH, "output_data", DATA_FOLDER_NAME, "articles", "raw_article_html"
    )

    for state in Path(data_folder_path).iterdir():
        for year in state.iterdir():
            for newsroom in year.iterdir():
                parse_newsroom(state, year, newsroom)

    add_final_indexes()


if __name__ == "__main__":
    engine, Session = src.db_connection(init=False)
    main()
    engine.dispose()
