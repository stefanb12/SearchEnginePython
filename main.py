import os

from parserHTML import Parser
from trie import Trie
from parserUpita import *

def parsiranje_HTML_dokumenata(path):
    trie = Trie()
    parser = Parser()

    if '.html' in path: # Ukoliko se unese putanja do odredjenog .html fajla nije potrebno prolaziti kroz direktorijume
        parser.parse(path)
        for word in parser.words:
            trie.add(word)
    else: # Ukoliko je unet putanja do direktorijuma, potrebno je proci kroz zadati direktorijum i poddirektroijume
        for root, directories, files in os.walk(path):
            for file in files:
                if '.html' in file: # U direktorijumu posmatramo samo .html dokumente
                    parser.parse(os.path.join(root, file))
                    for word in parser.words:  # Dodavanje reci u stablo
                        trie.add(word)

    if trie.is_empty(): # Ako je stablo prazno znaci da ne postoji reci u .html dokumentu
        return False, trie
    else:
        return True, trie

def main():
    path = input("Unesite putanju do korenskog direktorijuma koji zelite da parsirate:")
    # path = 'D:\Korisnik\Stefan\Desktop\Python\test-skup\python-2.7.7-docs-html\c-api'

    uspesno, trie = parsiranje_HTML_dokumenata(path)
    if uspesno == False:
        print("GRESKA! Niste uneli validnu putanju ili ne postoje .html dokumenti u direktorijumu koji zelite da parsirate.")
        print("Primer validne putanje -> D:\Korisnik\Stefan\Desktop\Python\\test-skup\python-2.7.7-docs-html")
        return

    while True:
        print('OPCIJE:')
        print('1. Pretraga reci u html dokumentima.')
        print('2. Izlazak iz programa.')
        opcija = input('Izaberite opciju: ')
        if opcija.isnumeric() == True:
            answer = int(opcija)
            if answer == 1:
                #print('Rezultati pretrage:')
                #flag, broj = trie.search('count')   # Provera da li ucitavanje reci u stablo dobro radi
                #print('Broj pojavljivanja reci count u direktorijumu c-api je : ', broj)
                upit = input("Unesite upit za pretragu: ")
                operator, reciUpita = parsiraj_upit(upit)
                if operator == 'AND':
                    print('Poziv pretrage sa AND operatorom')
                    print('Reci koje se pretrazuju:')
                    for rec in reciUpita:
                        print(rec)
                elif operator == 'OR':
                    print('Poziv pretrage sa OR operatorom')
                    print('Reci koje se pretrazuju:')
                    for rec in reciUpita:
                        print(rec)
                elif operator == 'NOT':
                    print('Poziv pretrage sa NOT operatorom')
                    print('Reci koje se pretrazuju:')
                    for rec in reciUpita:
                        print(rec)
                # else slucaj nije potreban zato sto se u parsiraj_upit ispisuju poruke o greskama ukoliko nije unet validan upit.
            elif answer == 2:
                return
            else:
                print("GRESKA! Morate izabrati jednu od ponudjenih opcija.")
        else:
            print("GRESKA! Morate izabrati jednu od ponudjenih opcija.")

if __name__ == '__main__':
    main()