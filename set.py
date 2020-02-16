class Set:

    def __init__(self):
        self.skup = {}

    def add(self, putanja):
        if putanja not in self.skup.keys():
            self.skup[putanja] = putanja

    def union(self, other):
        result = Set()
        for putanja in self.skup.keys():
            result.add(putanja)
        for putanja in other.skup.keys():
            result.add(putanja)
        return result

    def intersection(self, other):
        result = Set()
        for putanja in self.skup.keys():
            if putanja in other.skup.keys():
                result.add(putanja)

        return result

    def complement(self, other):
        result = Set()
        for putanja in self.skup.keys():
            if putanja not in other.skup.keys():
                result.add(putanja)

        return result