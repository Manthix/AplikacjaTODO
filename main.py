import DB_connect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
from datetime import date

zadaniaDB = DB_connect.Zadania
 #Stworzenie sesji
Session = sessionmaker(bind=DB_connect.engine)
session = Session()

def DodajZadanie():
    #Pobranie danych zadań
    print('Podaj nazwę zadania')
    Tytul = input()
    print('Podaj opis zadania')
    Opis = input()

    zadanie = zadaniaDB(Tytul, Opis, date.today(), True)
    #Zapisanie
    session.add(zadanie)
    session.commit() 

def WyswietlWykonaneZadania():
    for zadanie in session.query(zadaniaDB).filter(zadaniaDB.Status==True):
        print(zadanie.ID_Zadania, zadanie.Tytul, '\n', zadanie.Opis, '\n', zadanie.Data, 'Wykonane')
def WyswietlNieWykonaneZadania():
    for zadanie in session.query(zadaniaDB).filter(zadaniaDB.Status==False):
        print(zadanie.ID_Zadania, zadanie.Tytul, '\n', zadanie.Opis, '\n', zadanie.Data, 'Do zrobienia')

def WykonajZadanie():
    print('Podaj id wykonanego zadania')
    ZmienianeID = input()
    session.execute(update(zadaniaDB).where(zadaniaDB.ID_Zadania==ZmienianeID).values(Status=True))
    session.commit() 

WyswietlNieWykonaneZadania()
WyswietlWykonaneZadania()

