from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.Calendar import Base

class DatabaseConnection:
    def __init__(self, db_path: str = "./database/database.db"):
        self.engine = create_engine(f"sqlite:///{db_path}")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def close(self):
        self.session.close()