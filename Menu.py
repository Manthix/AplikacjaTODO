import requests
import json
 
def printBody(body):
    zadania = json.loads(body)
    print("\n")
    for zadanie in zadania:
        if zadanie['Status'] == True:
            status = "skonczone"
        else:
            status = "do zrobienia"
        print(str(zadanie['ID_Zadania'])+". "+zadanie['Tytul']+" - "+status+"\n"+zadanie['Data']+"\n"+zadanie['Opis'])
        
    print("\n")

    
def menu():
    
    print("Jaką czynność chcesz wykonać? \n 1.Dodać zadanie \n 2.Wyświetl zadania \n 3.Oznacz zadanie za wykonane")
    wybor = input()
    match wybor:
        case '1':
            print('Podaj nazwę zadania')
            Tytul = input()
            print('Podaj opis zadania')
            Opis = input()

 
            requests.post("http://127.0.0.1:5000/Zadania/DodajZadanie?Tytul="+Tytul+"&Opis="+Opis)
        case '2':
            print("Jakie zadania wyświetlić? \n 1.Wszystkie \n 2.Wykonane \n 3.Niewykonane")
            wybor = input()
            match wybor:
                case '1':
                    body = requests.get("http://127.0.0.1:5000/Zadania/Wszystkie").content
                    printBody(body)
                case '2':
                    body = requests.get("http://127.0.0.1:5000/Zadania/Zrobione").content
                    printBody(body)
                case '3':
                    body = requests.get("http://127.0.0.1:5000/Zadania/NieZrobione").content
                    printBody(body)
                case _:
                    print("Zły wybór")
        case '3':
            print('Podaj id wykonanego zadania')
            ZmienianeID = input()
            requests.put("http://127.0.0.1:5000/Zadania/WykonajZadanie?ZmienianeID="+ZmienianeID)
        case _:
            print("Zły wybór")
    
    menu()
menu()
