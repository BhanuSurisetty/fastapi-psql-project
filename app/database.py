# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DatabaseURL = "postgresql://postgres:Psql@123@localhost:5432/postgres"
DatabaseURL = "postgresql://postgres:Psql%40123@localhost:5432/postgres"

# Create the database engine
engine = create_engine(DatabaseURL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()