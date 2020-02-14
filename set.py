class Set:

    def __init__(self):
        self.putanja_broj = {}  # Recnik - kljuc je putanja, vrednost je rang

    def add(self, putanja, broj):
        postoji = False
        for p, b in self.putanja_broj.items():
            if p == putanja:
                postoji = True

        if postoji == False:
            self.putanja_broj[putanja] = broj
        else:
            self.putanja_broj[putanja] = self.putanja_broj.get(putanja) + broj

    def union(self, other):
        result = Set()
        for p, b in self.putanja_broj.items():
            result.add(p, b)
        for p, b in other.putanja_broj.items():
            result.add(p, b)
        return result

    def intersection(self, other):
        result = Set()
        for p1, b1 in self.putanja_broj.items():
            for p2, b2 in other.putanja_broj.items():
                if p1 == p2:
                    result.add(p1, b1)
                    result.add(p2, b2)
        return result

    def complement(self, other):    # Komplement je presek self i other i onda se u self obrisu elementi koji su dobijeni kao rezultat preseka
        presek = self.intersection(other)
        for p, b in presek.putanja_broj.items():
            self.remove(p)

        return self

    def remove(self, putanja):
        self.putanja_broj.__delitem__(putanja)

    def print(self):
        for putanja, broj in self.putanja_broj.items():
            print('PUTANJA:', putanja, ' -> ', broj)