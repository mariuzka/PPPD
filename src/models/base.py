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
    date = Column(Date)
    daily_index = Column(Integer)
    scraped_at = Column(DateTime)

    newsroom = relationship("Newsroom", back_populates="articles", uselist=False)
    raw_html = relationship("ArticleHTML", backref="article", uselist=False)


class Newsroom(Base, Str):
    __tablename__ = "newsrooms"

    id = Column(Integer, primary_key=True)

    title = Column(Text)
    subtitle = Column(Text)

    dept_name = Column(Text)
    dept_district = Column(Text)
    dept_state = Column(Text)
    dept_type = Column(Text)

    link = Column(Text)
    weblinks = Column(Text)

    articles = relationship("Article", back_populates="newsroom")

    scraping_datetime = Column(DateTime, default=dt.datetime.now)


class ArticleHTML(Base, Str):
    __tablename__ = "articles_html_raw"

    article_id = Column(Integer, ForeignKey("articles.id"), primary_key=True)
    html = Column(Text)