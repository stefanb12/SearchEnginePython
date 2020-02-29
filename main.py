import os
from time import time

from search_parser.parserHTML import Parser
from search_parser.parserUpita import *
from search_parser.pretraga import *
from data_structures.trie import Trie
from data_structures.graph import Graph
from pagination_rang_sort.sortiranje import *
from pagination_rang_sort.paginacija import paginacijaRezultata
from pagination_rang_sort.rangiranje import *

def parsiranje_HTML_dokumenata(path):
    trie = Trie()
    parser = Parser()
    graph = Graph()
    start = time()
    for root, directories, files in os.walk(path):
        for file in files:
            if '.html' in file: # U direktorijumu posmatramo samo .html dokumente
                parser.parse(os.path.join(root, file))
                graph.dodajCvor(os.path.join(root, file))
                graph.dodajGranu(os.path.join(root, file))
                for word in parser.words:  # Dodavanje reci u stablo
                    trie.add(word, os.path.join(root, file))
    end = time()
    if trie.is_empty(): # Ako je stablo prazno znaci da ne postoji reci u .html dokumentu
        return False, trie, graph, end - start
    else:
        return True, trie, graph, end - start

def main():
    global trie
    global graph
    uspesno = False
    while uspesno == False:
        path = input("Unesite putanju do direktorijuma u okviru kog želite da vršite pretragu: ")

        uspesno, trie, graph, vreme = parsiranje_HTML_dokumenata(path)

        if uspesno == False:
            print("\nGREŠKA! Niste uneli validnu putanju ili ne postoje HTML dokumenti u direktorijumu koji ste uneli.")
            print("NAPOMENA: Direktorijum za pretragu mora da sadrži HTML dokumente.\n")
        else:
            print("\nOBAVEŠTENJE: Uspešno ste uneli putanju do direktorijuma za pretragu.")
            print("VREME UČITAVANJA PODATAKA:", vreme, "\n")

    while True:
        print("IZABERITE OPCIJU:")
        print('0. Izlazak iz programa.')
        print('1. Pretraga reči u HTML dokumentima.')
        print('2. Unos nove putanje do direktorijuma za pretragu.')
        opcija = input('Vaša opcija: ')
        if opcija.isnumeric() == True:
            answer = int(opcija)
            if answer == 1:
                upit = input("Unesite upit za pretragu: ")
                operator, reciUpita = parsiraj_upit(upit) # Pozivanje metode za parsiranje upita i utvrdjivanja postojanja nekog od logickih operatora i reci
                if operator != None and reciUpita != None:
                    rezultujuciSet, rezultujuciRecnik = pretrazi_dokumente(operator, reciUpita, trie)  # Pozivanje pretrage dokumenta, rezultat pretrage je skup putanja do HTML dokumenata i recnik koji sadrzi parove(putanja, broj pojavljivanja reci na putanji)
                    if rezultujuciSet != None and rezultujuciRecnik != None:
                        print("\nOBAVEŠTENJE: Pretraga uspešno izvršena, broj pronađenih HTML dokumenata je " + str(len(rezultujuciSet.skup)) + ".")
                        lista_vrednosti = []
                        lista_kljuceva = []
                        rangirani_recnik = rangStranice(rezultujuciRecnik, graph, operator, reciUpita) # Pozivanjem rangStranice dobijemo recnik u kome su kljucevi HTML stranice a vrednosti njihovi rangovi

                        for key, value in rangirani_recnik.items():
                            lista_vrednosti.append(value)

                        sortiraj(lista_vrednosti)

                        sortirani_recnik = {}
                        lista_vrednosti = list(dict.fromkeys(lista_vrednosti)) #izbacivanje duplikata iz liste
                        for vrednost in lista_vrednosti:
                            for kljuc in rangirani_recnik.keys():
                                if rangirani_recnik.get(kljuc) == vrednost:
                                    sortirani_recnik.update({kljuc: vrednost})
                                    lista_kljuceva.append(kljuc)

                        print("\nREZULTATI PRETRAGE:")
                        paginacijaRezultata(sortirani_recnik, lista_kljuceva)
            elif answer == 2:
                path = input("Unesite putanju do direktorijuma u okviru kog želite da vršite pretragu: ")
                uspesno, new_trie, new_graph, vreme = parsiranje_HTML_dokumenata(path)
                if uspesno == True:
                    print("\nOBAVEŠTENJE: Uspešno ste uneli putanju do novog direktorijuma.")
                    print("NAPOMENA: Pretraga će se vršiti u okviru novog direktorijuma koji ste uneli.")
                    print("VREME UČITAVANJA PODATAKA:", vreme, "\n")
                    trie = new_trie
                    graph = new_graph
                else:
                    print("\nGREŠKA! Niste uneli validnu putanju ili ne postoje HTML dokumenti u direktorijumu koji ste uneli.")
                    print("NAPOMENA: Pretraga će se vršiti u okviru direktorijuma koji je prethodno unet.\n")
            elif answer == 0:
                return
            else:
                print("\nGREŠKA! Morate izabrati jednu od ponuđenih opcija.\n")
        else:
            print("\nGREŠKA! Morate izabrati jednu od ponuđenih opcija.\n")

if __name__ == '__main__':
    main()