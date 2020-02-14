from parserHTML import Parser

class CvorGrafa:
    def __init__(self,stranice = None):

        self.stranice = stranice
        self.links, self.words = self.parser()
        self.lista_linkova = []

    def parser(self):
        parser = Parser()
        return parser.parse(self.stranice)

class GranaGrafa:
    def __init__(self,origin,destination):
        self.origin = origin
        self.destiantion = destination

    def __hash__(self):
        return hash((self.origin, self.destiantion))

class Graph:
    def __init__(self):

        self.lista_cvorova = dict()
        self.lista_grana = []


    def dodajCvor(self,naziv_cvora):
        if naziv_cvora not in self.lista_cvorova:
            cvor = CvorGrafa(naziv_cvora)
            self.lista_cvorova[naziv_cvora] = cvor

        for link in self.lista_cvorova[naziv_cvora].links:
            if link in self.lista_cvorova:
                self.lista_cvorova[link].lista_linkova.append(self.lista_cvorova[link])
            else:
                c = CvorGrafa(link)
                self.lista_cvorova[link] = c
                self.lista_cvorova[link].lista_linkova.append(c)

            grana = GranaGrafa(self.lista_cvorova[naziv_cvora],self.lista_cvorova[link])
            self.lista_grana.append(grana)

    def __str__(self):
        return str(self.lista_cvorova.keys())


