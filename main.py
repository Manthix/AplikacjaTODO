#SQL
import DB_connect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
from datetime import date

zadaniaDB = DB_connect.Zadania
Session = sessionmaker(bind=DB_connect.engine)
session = Session()

#API
from fastapi import FastAPI
app = FastAPI()

#Funkcje zapytań
def DodajZadanie(Tytul, Opis):
    zadanie = zadaniaDB(Tytul, Opis, date.today(), False)
    #Zapisanie
    session.add(zadanie)
    session.commit() 

def WyswietlWykonanieZadania(stan):
    lista=[]
    for zadanie in session.query(zadaniaDB).filter(zadaniaDB.Status==stan):
        lista.append(zadanie)
    return lista
def WyswietlZadania():
    lista=[]
    for zadanie in session.query(zadaniaDB).all():
        lista.append(zadanie)
    return lista

def WykonajZadanie(ZmienianeID):
    session.execute(update(zadaniaDB).where(zadaniaDB.ID_Zadania==ZmienianeID).values(Status=True))
    session.commit() 

#Endpointy
@app.get("/Zadania/Zrobione")
async def Zrobione():
    return WyswietlWykonanieZadania(True)
@app.get("/Zadania/NieZrobione")
async def NieZrobione():
    return WyswietlWykonanieZadania(False)
@app.get("/Zadania/Wszystkie")
async def Wszystkie():
    return WyswietlZadania()
@app.put("/Zadania/WykonajZadanie")
async def Wykonaj(ZmienianeID: int):
    return WykonajZadanie(ZmienianeID)
@app.post("/Zadania/DodajZadanie/")
async def Dodaj(Tytul: str, Opis: str):
    return DodajZadanie(Tytul, Opis)

#Start serwera
from uvicorn import run
if __name__ == "__main__":
    run("main:app", host="127.0.0.1", port=5000, log_level="info")