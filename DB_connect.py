from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Boolean, Date
from sqlalchemy.orm import declarative_base

engine = create_engine('postgresql://User:Password@localhost/mydatabase')
#Link prowadzacy do przykladow uzycia innych serwerow sql niz postgresql dla powyzszego pola:
#https://docs.sqlalchemy.org/en/20/core/engines.html

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
