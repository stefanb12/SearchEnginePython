import os

from parserHTML import Parser
from parserUpita import *
from pretraga import *
from trie import Trie
from graph import Graph

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
                operator, reciUpita = parsiraj_upit(upit) # Pozivanje metode za parsiranje upita i utvrdjivanja postojanja nekog od logickih operatora i reci
                if operator != None and reciUpita != None:
                    rezultujuciSet, rezultujuciRecnik = pretrazi_dokumente(operator, reciUpita, trie) # Pozivanje pretrage dokumenta, rezultat pretrage je skup putanja do HTML dokumenata i recnik koji sadrzi parove(putanja, broj pojavljivanja reci na putanji)
                    if rezultujuciRecnik != None:
                        for key, value in rezultujuciRecnik.items():
                            print(key, ' ->', value)
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