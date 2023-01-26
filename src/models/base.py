import datetime as dt

from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Str:
    def __repr__(self):
        name = self.__class__.__name__

        columns = self.__table__.c
        colnames = [f"{c.name}={getattr(self, c.name)}" for c in columns]

        return f"{name}({', '.join(colnames)})"


class Article(Base, Str):
    __tablename__ = "articles"
    __table_args__ = (UniqueConstraint("newsroom_id", "date", "daily_index"),)

    id = Column(Integer, primary_key=True)
    newsroom_id = Column(Integer, ForeignKey("newsrooms.id"))
    newsroom_visit_id = Column(Integer, ForeignKey("newsroom_visits.id"))
    date = Column(Date)
    daily_index = Column(Integer)
    scraped_at = Column(DateTime)
    
    article_link = Column(Text)
    newsroom_nr = Column(Text)
    from_presseportal = Column(Text)
    location = Column(Text)
    header = Column(Text)
    text = Column(Text)
    location_tags_names = Column(Text)
    location_tags_scores = Column(Text)
    topic_tags_names = Column(Text)
    topic_tags_scores = Column(Text)

    newsroom = relationship("Newsroom", back_populates="articles", uselist=False)
    newsroom_visit = relationship("Newsroom_visit", back_populates="articles")
    article_html = relationship("ArticleHTML", back_populates="article", uselist=False)


class Newsroom(Base, Str):
    """
    Class to collect Newsrooms

    To track, whether Newsroom properties change, we pose
    a unique constraint an all fields. 
    """

    __tablename__ = "newsrooms"
    __table_args__ = (UniqueConstraint("newsroom_nr","title", "subtitle", 
        "dept_name", "dept_district", "dept_state", "dept_type",
            "link", "weblinks"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    newsroom_nr = Column(Integer)

    title = Column(Text)
    subtitle = Column(Text)

    dept_name = Column(Text)
    dept_district = Column(Text)
    dept_state = Column(Text)
    dept_type = Column(Text)

    link = Column(Text)
    weblinks = Column(Text)

    articles = relationship("Article", back_populates="newsroom")
    visits = relationship("Newsroom_visit", back_populates="newsroom")


class Newsroom_visit(Base, Str):
    __tablename__ = "newsroom_visits"
    __table_args__ = (UniqueConstraint("newsroom_id", "scraping_datetime"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    newsroom_id = Column(Integer, ForeignKey("newsrooms.id"))
    scraping_datetime = Column(DateTime, default=dt.datetime.now)

    newsroom = relationship("Newsroom", back_populates="visits", uselist=False)
    articles = relationship("Article", back_populates="newsroom_visit")


class ArticleHTML(Base, Str):
    __tablename__ = "articles_html_raw"

    article_id = Column(Integer, ForeignKey("articles.id"), primary_key=True)
    html = Column(Text)

    article = relationship("Article", back_populates="article_html")