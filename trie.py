from set import Set

class TrieNode:
    def __init__(self, parent = None, char = None):
        self.char = char
        if self.char is not None:
            self.char = self.char.lower()   # Pretraga treba da bude case insensitive
        self.parent = parent
        self.children = []
        self.end = False
        self.count = 0
        self.set = Set()
        self.path_count = {}

class Trie:

    def __init__(self):
        self.root = TrieNode() # Koren je prazan cvor tj. nema u sebi nijedan karakter

    def add(self, word, html_file):
        curr_node = self.root
        word = word.lower() # Zato sto treba da bude case insensitive pretraga
        for char in word:
            found_in_child = False
            for child in curr_node.children:
                if child.char == char:
                    curr_node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_Node = TrieNode(curr_node, char)
                curr_node.children.append(new_Node)
                curr_node = new_Node
        curr_node.end = True                                # Stigli smo do kraja reci, potrebno je uvecati brojac i upisati putanju u set
        if html_file not in curr_node.path_count.keys():    # Ako ne postoji html fajl u recniku, dodaj ga u recnik i u set
            curr_node.path_count[html_file] = 1
            curr_node.set.add(html_file)
        else:                                               # Ako fajl vec postoji u recniku uvecaj broj pojavljivanja reci u tom fajlu
            curr_node.path_count[html_file] += 1

    def search(self, word):
        word = word.lower().strip()
        if len(self.root.children) == 0:
            return False, Set(), {}

        node = self.root

        for char in word:
            char_not_found = True
            for child in node.children:
                if child.char == char:
                    char_not_found = False
                    node = child
                    break
            if char_not_found:
                return False, Set(), {}

        if node.end == False:
            return False, Set(), {}

        # U ovom slucaju je end = True i vracamo skup koji sadrzi putanje do html stranica za trazenu rec
        # i recnik koji sadrzi parove (putanja, broj pojavljivanja reci na putanji)
        return node.end, node.set, node.path_count

    def is_empty(self): # Koristi se za proveru da li je uneta validna putanja za parsiranje .html dokumenta
        return len(self.root.children) == 0