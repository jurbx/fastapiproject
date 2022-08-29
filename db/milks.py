import datetime
import sqlalchemy
from .base import metadata


milks = sqlalchemy.Table(
    'milks',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('name', sqlalchemy.String, unique=True),
    sqlalchemy.Column('rating', sqlalchemy.Integer, minvalue=0, maxvalue=10, nullable=False),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow),
)

