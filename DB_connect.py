from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Boolean, Date
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://postgres:Lahcim@localhost/TODOlist')

base = declarative_base()

class Zadania(base):
    __tablename__ = 'Zadania'

    ID_Zadania = Column(Integer, primary_key=True)
    Tytul = Column(String)
    Opis = Column(String)
    Data = Column(Date)
    Status = Column(Boolean)

    def __init__(self, Tytul, Opis, Data, Status):
        self.Tytul = Tytul
        self.Opis = Opis
        self.Data = Data
        self.Status = Status

base.metadata.create_all(engine)