def rangStranice(rezultujuciRecnik, graph, operator, reciUpita):
    rangirani_recnik = {}

    #prolazak kroz sve pronadjenje stranice
    for key, value in rezultujuciRecnik.items():
        linkRang, straneSaLinkovima = rangPoLinkovima(key, graph)

        brReci = 0
        #prebrojavanje trazenih reci u stranicama koje sadrze link na trazenu stranicu
        for kljuc, vrednost in rezultujuciRecnik.items():
            for stranica in straneSaLinkovima:
                if kljuc == stranica:
                    brReci += vrednost

        konacniRang = value*1.5 + linkRang*1.3 + brReci*1.2
        # value - broj pojavljivanja trazenih reci na html stranici
        # linkRang - broj linkova iz drugih stranica na pronadjenu stranicu
        # brReci - broj trazenih reci u stranicama koje sadrze link na trazenu stranicu

        konacniRang = round(konacniRang, 2)

        rangirani_recnik.update({key: konacniRang})

    return rangirani_recnik


def rangPoLinkovima(cvor, graph):
    brLinkovaKaNjemu = 0
    strane_sa_linkovima = []

    #prolazak kroz sve cvorove i njihove linkove i pronalazak broja linkova iz drugih stranica na pronadjenu stranicu
    for vertex in graph.lista_cvorova:
        for link in graph.lista_cvorova[vertex].links:
            if vertex == cvor:
               break
            if link == cvor:
                brLinkovaKaNjemu = brLinkovaKaNjemu + 1
                strane_sa_linkovima.append(vertex)

    strane_sa_linkovima = list(dict.fromkeys(strane_sa_linkovima))

    return brLinkovaKaNjemu, strane_sa_linkovima

