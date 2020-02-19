import math

def paginacijaRezultata(rezultati):

    uredu = True
    while uredu:
        broj = input("Izaberite broj rezultata pretrage na jednoj strani: ")
        print("")
        #brPoStr = int(broj)
        if broj.isnumeric() == True:
            brPoStr = int(broj)
            if brPoStr > 0:
                #print('Broj rezultata pretrage po stranici:', brPoStr)
                #print("")
                break
            else:
                print("POTREBNO JE UNETI BROJ VECI OD NULE.\n")
        else:
            print("POTREBNO JE UNETI ISKLJUCIVO BROJ\n")

    broj_stranica = math.ceil(len(rezultati) / brPoStr)

    i = 0
    for rez in rezultati:
        print(rez)
        i = i + 1
        if i == brPoStr:
            break

    print('strana 1 od', broj_stranica, '\n')

    odabir = True
    trenutnaStrana = 1
    while odabir:
        print("IZABERITE OPCIJU:")
        print("1 - Prethonda stranica")
        print("2 - Sledeca stranica")
        print("3 - Izlazak iz paginacionog prikaza")
        opcija = input("Vasa opcija: ")
        print("")
        if opcija.isnumeric() == True:
            answer = int(opcija)
            if answer == 1:
                if trenutnaStrana - 1 <= 0:
                    print("VAN OPSEGA, mozete izabrati samo sledecu stranicu")
                else:
                    trenutnaStrana = trenutnaStrana - 1
                    i = brPoStr * (trenutnaStrana - 1)
                    kraj = brPoStr * trenutnaStrana
                    for rez in range(i, kraj):
                        print(rezultati[rez])
                        i = i + 1
                        if i == i + brPoStr:
                            break
                    print('strana', trenutnaStrana, 'od', broj_stranica, '\n')
            elif answer == 2:
                if trenutnaStrana + 1 > broj_stranica:
                    print("VAN OPSEGA, mozete izabrati samo prethodnu stranicu")
                else:
                    trenutnaStrana = trenutnaStrana + 1
                    i = brPoStr * (trenutnaStrana - 1)
                    if trenutnaStrana == broj_stranica:
                        kraj = brPoStr * (trenutnaStrana - 1) + (len(rezultati) - brPoStr * (trenutnaStrana - 1))
                    else:
                        kraj = brPoStr * trenutnaStrana
                    for rez in range(i, kraj):
                        print(rezultati[rez])
                        i = i + 1
                        if i == i + brPoStr:
                            break
                    print('strana', trenutnaStrana, 'od', broj_stranica, '\n')
            elif answer == 3:
                print("IZASLI STE IZ PAGINACIONOG PRIKAZA REZULTATA.")
                return
            else:
                print("GRESKA IZABRALI STE NEPOSTOJECU OPERACIJU")
        else:
            print("NEPOSTOJECA OPCIJA")


