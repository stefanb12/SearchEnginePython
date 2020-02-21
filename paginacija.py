import math

def paginacijaRezultata(rezultati, kljucevi): #prosledjuje se recnik(rezultati) i lista kljuceva istog recnika(kljucevi)

    brPoStr = 5

    broj_stranica = math.ceil(len(rezultati.keys()) / brPoStr)

    #inicijalno se pokazuje prva strana pretrazenih rezultata

    i = 0
    for rez in rezultati.keys():
        print(str(i + 1) + ". " + str(rez) + ' -> ' + str(rezultati.get(rez)))
        i = i + 1
        if i == brPoStr:
            break

    print('strana 1 od', broj_stranica, '\n')

    #meni za prikaz paginacije rezultata

    odabir = True
    trenutnaStrana = 1 #trenutna strana prikaza pri ulasku u while petjlu je 1
    while odabir:
        print("IZABERITE OPCIJU:")
        print("1 - Prethodna stranica")
        print("2 - Sledeca stranica")
        print("3 - Odabir broja rezultata pretrage na jednoj strani")
        print("4 - Izlazak iz paginacionog prikaza")
        opcija = input("Vasa opcija: ")
        print("")
        if opcija.isnumeric() == True:
            answer = int(opcija)
            if answer == 1:
                if trenutnaStrana - 1 <= 0: #provera - ne moze se ici u nazad ako smo na prvoj stranici
                    print("VAN OPSEGA, mozete izabrati samo sledecu stranicu")
                else:
                    trenutnaStrana = trenutnaStrana - 1 #svaki put kada se izabere opcija "Prethodna stranica" trenutnaStrana se smanji za 1
                    i = brPoStr * (trenutnaStrana - 1) #i pretstravlja pocetak iteracije
                    kraj = brPoStr * trenutnaStrana #kraj iteracije
                    for rez in range(i, kraj):
                        print(str(i + 1) + ". " + str(kljucevi[rez]) + " -> " + str(rezultati.get(kljucevi[rez]))) #stampa se kljuc recnika(html stranica) i uparena vrednost
                        i = i + 1
                        if i == i + brPoStr:
                            break
                    print('strana', trenutnaStrana, 'od', broj_stranica, '\n') #numeracija stranica
            elif answer == 2:
                if trenutnaStrana + 1 > broj_stranica: #provera - ne moze se ici u napred ako smo na poslednjoj stranici
                    print("VAN OPSEGA, mozete izabrati samo prethodnu stranicu")
                else:
                    trenutnaStrana = trenutnaStrana + 1
                    i = brPoStr * (trenutnaStrana - 1)
                    #kod ispisa poslednje strane prikaza rezultata moze se desiti da ostanje manji broj rezultata nego
                    #na prethodnim stranama prikaza rezultata zbog toga je potrebno pomeriti kraj iteriranja u nazad
                    if trenutnaStrana == broj_stranica:
                        kraj = brPoStr * (trenutnaStrana - 1) + (len(rezultati) - brPoStr * (trenutnaStrana - 1))
                    #ako je broj prikaza rezultata na poslednjoj strani isti kao i kod prethodnih
                    else:
                        kraj = brPoStr * trenutnaStrana
                    for rez in range(i, kraj):
                        print(str(i + 1) + ". " + str(kljucevi[rez]) + " -> " + str(rezultati.get(kljucevi[rez])))
                        i = i + 1
                        if i == i + brPoStr:
                            break
                    print('strana', trenutnaStrana, 'od', broj_stranica, '\n')
            elif answer == 3:
                uredu = True
                while uredu:
                    broj = input("Izaberite broj rezultata pretrage na jednoj strani: ")
                    print("")
                    # brPoStr = int(broj)
                    if broj.isnumeric() == True:
                        brPoStr = int(broj)
                        if brPoStr > 0:
                            # print('Broj rezultata pretrage po stranici:', brPoStr)
                            # print("")
                            break
                        else:
                            print("POTREBNO JE UNETI BROJ VECI OD NULE.\n")
                    else:
                        print("POTREBNO JE UNETI ISKLJUCIVO BROJ\n")

                broj_stranica = math.ceil(len(rezultati.keys()) / brPoStr)

                i = 0
                for rez in rezultati.keys():
                    print(str(i + 1) + ". " + str(rez) + ' -> ' + str(rezultati.get(rez)))
                    i = i + 1
                    if i == brPoStr:
                        break

                print('strana 1 od', broj_stranica, '\n')
                trenutnaStrana = 1

            elif answer == 4:
                print("IZASLI STE IZ PAGINACIONOG PRIKAZA REZULTATA.")
                return
            else:
                print("GRESKA IZABRALI STE NEPOSTOJECU OPERACIJU")
        else:
            print("NEPOSTOJECA OPCIJA")

