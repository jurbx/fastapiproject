import datetime
import sqlalchemy
from .base import metadata


products = sqlalchemy.Table(
    'products',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False),
    sqlalchemy.Column('email', sqlalchemy.String, primary_key=True, unique=True),
    sqlalchemy.Column('title', sqlalchemy.String),
    sqlalchemy.Column('description', sqlalchemy.String),
    sqlalchemy.Column('price', sqlalchemy.Integer),
    sqlalchemy.Column('is_active', sqlalchemy.Boolean),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column('updated_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow),
    sqlalchemy.Column('img', sqlalchemy.String)
)