from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DEBUG = True

engine = SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/pdv'
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

SQLALCHEMY_TRACK_MODIFICATIONS = True
