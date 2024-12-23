from sqlmodel import SQLModel, create_engine, Session
from models import *


sqlite_file_name = "cards.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo = False)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def main():
    create_db_and_tables()


if __name__ == "__main__":
    main()