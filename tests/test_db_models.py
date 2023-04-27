import pytest

import src
from src.models import *
import datetime

from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

newsroom = Newsroom(
    id=None,
    newsroom_nr=126725,
    title="Erbeut Veränderte Landespolizeiinspektion Suhl",
    subtitle="http://www.thueringen.de\nWeblinksHomepage\nSocial Web@Facebook@twitter",
    dept_name="Landespolizeiinspektion Suhl",
    dept_district="Suhl",
    dept_state="thüringen",
    dept_type="police",
    link="https://www.presseportal.de/blaulicht/nr/126725",
    weblinks=str(
        [
            [
                "Zur Homepage von Landespolizeiinspektion Suhl",
                "http://www.thueringen.de/th3/polizei/index.aspx",
            ],
            ["Website Homepage", "http://www.thueringen.de/th3/polizei/index.aspx"],
            ["@Facebook", "https://www.facebook.com/Polizei.Thueringen"],
            ["@twitter", "https://twitter.com/Polizei_Thuer"],
        ]
    ),
)


