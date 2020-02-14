import os

from parserHTML import Parser
from set import Set
from trie import Trie
from graph import Graph
from parserUpita import *

def parsiranje_HTML_dokumenata(path):
    trie = Trie()
    parser = Parser()
    graph = Graph()

    for root, directories, files in os.walk(path):
        for file in files:
            if '.html' in file: # U direktorijumu posmatramo samo .html dokumente
                parser.parse(os.path.join(root, file))
                graph.dodajCvor(os.path.join(root, file))
                for word in parser.words:  # Dodavanje reci u stablo
                    trie.add(word, os.path.join(root, file))

    if trie.is_empty(): # Ako je stablo prazno znaci da ne postoji reci u .html dokumentu
        return False, trie
    else:
        return True, trie

def main():
    global trie
    uspesno = False
    while uspesno == False:
        path = input("Unesite putanju do direktorijuma u okviru kog zelite da vrsite pretragu:")
        # path = 'D:\Korisnik\Stefan\Desktop\Python\test-skup\python-2.7.7-docs-html\c-api'

        uspesno, trie = parsiranje_HTML_dokumenata(path)
        if uspesno == False:
            print("GRESKA! Niste uneli validnu putanju ili ne postoje HTML dokumenti u direktorijumu koji ste uneli.")
            print("Primer validne putanje -> D:\Korisnik\Stefan\Desktop\Python\\test-skup\python-2.7.7-docs-html")

    while True:
        print('OPCIJE:')
        print('1. Pretraga reci u HTML dokumentima.')
        print('2. Unos nove putanje do direktorijuma za pretragu.')
        print('3. Izlazak iz programa.')
        opcija = input('Izaberite opciju: ')
        if opcija.isnumeric() == True:
            answer = int(opcija)
            if answer == 1:
                upit = input("Unesite upit za pretragu: ")
                operator, reciUpita = parsiraj_upit(upit)
                if operator == 'AND':   # Ukoliko je unet AND operator postoje tacno dve reci za pretragu
                    postoji1, set1, putanja1, broj1 = trie.search(reciUpita[0]) # Skup za prvu rec upita
                    postoji2, set2, putanja2, broj2 = trie.search(reciUpita[1]) # Skup za drugu rec upita
                elif operator == 'OR':  # Ukoliko je unet Or operator postoje tacno dve reci za pretragu
                    postoji1, set1, putanja1, broj1 = trie.search(reciUpita[0]) # Skup za prvu rec upita
                    postoji2, set2, putanja2, broj2 = trie.search(reciUpita[1]) # Skup za drugu rec upita
                elif operator == 'NOT1':    # Slucaj kada se operator NOT nalazi na prvom mestu u upitu
                    postoji, set, putanja, broj = trie.search(reciUpita[0]) # Skup za rec koja je uneta posle NOT operatora
                elif operator == 'NOT2':    # Slucaj kada se operator NOT nalazi izmedju dve recu u upitu
                    postoji1, set1, putanja1, broj1 = trie.search(reciUpita[0]) # Skup za prvu rec upita
                    postoji2, set2, putanja2, broj2 = trie.search(reciUpita[1]) # Skup za drugu rec upita
                elif operator == 'BEZ_LOG_OP':  # Ukoliko nije unet logicki operator moze se uneti proizvoljan broj reci za pretragu
                    broj_reci = len(reciUpita)
                    i = 0
                    for i in range(broj_reci):
                        postoji, set, putanja, broj = trie.search(reciUpita[i]) # Odredjivanje skupova za onoliko reci koliko je uneto u upit
                        # Pozvati uniju za svaki set
                # else slucaj nije potreban zato sto se u parsiraj_upit ispisuju poruke o greskama ukoliko nije unet validan upit.
            elif answer == 2:
                path = input("Unesite putanju do direktorijuma u okviru kog zelite da vrsite pretragu:")
                uspesno, new_trie = parsiranje_HTML_dokumenata(path)
                if uspesno == True:
                    print("OBAVESTENJE: Uspesno ste uneli putanju do novog direktorijuma.")
                    print("NAPOMENA: Pretraga ce se vrsiti u okviru novog direktorijuma koji ste uneli.")
                    trie = new_trie
                else:
                    print("GRESKA! Niste uneli validnu putanju ili ne postoje HTML dokumenti u direktorijumu koji ste uneli.")
                    print("NAPOMENA: Pretraga ce se vrsiti u okviru direktorijuma koji je prethodno unet.")
            elif answer == 3:
                return
            else:
                print("GRESKA! Morate izabrati jednu od ponudjenih opcija.")
        else:
            print("GRESKA! Morate izabrati jednu od ponudjenih opcija.")

if __name__ == '__main__':
    main()