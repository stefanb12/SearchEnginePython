from set import Set

class TrieNode:
    def __init__(self, parent = None, char = None, html_file = None):
        self.char = char
        if self.char is not None:
            self.char = self.char.lower()   # Pretraga treba da bude case insensitive
        self.parent = parent
        self.children = []
        self.end = False
        self.count = 0
        self.html_file = html_file
        self.set = Set()

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
                new_Node = TrieNode(curr_node, char, html_file)
                curr_node.children.append(new_Node)
                curr_node = new_Node
        curr_node.end = True
        if curr_node.html_file == html_file:  # Ako se rec vise puta nalazi na istoj stranici uvecavaj brojac
            if curr_node.count == 0:
                curr_node.count = 1
            else:
                curr_node.count += 1
        elif curr_node.html_file != html_file:  # Kada u cvor stigne nova stranica prethodna stranica i broj pojavljivanja reci na njoj se smestaju u skup
            if curr_node.count != 0:
                curr_node.set.add(curr_node.html_file, curr_node.count)  # U skup dodajemo putanju do html dokumenta i broj pojavljivanja reci na njoj
                curr_node.count = 1
            curr_node.html_file = html_file  # U trenutnom cvoru stavljamo da stara html stranica postaje nova

    def search(self, word):
        word = word.lower().strip()
        if len(self.root.children) == 0:
            return False, Set(), None, 0

        node = self.root

        for char in word:
            char_not_found = True
            for child in node.children:
                if child.char == char:
                    char_not_found = False
                    node = child
                    break
            if char_not_found:
                return False, Set(), None, 0

        if node.end == False:
            return False, Set(), None, 0

        # U ovom slucaju je end = True i vracamo skup koji sadrzi putanje do html stranice i broj pojavljivanja reci na toj stranici
        # Vracamo i putanju do poslednje stranice i broj pojavljivanja reci na njoj da bi ih dodali u skup
        return node.end, node.set, node.html_file, node.count

    def is_empty(self): # Koristi se za proveru da li je uneta validna putanja za parsiranje .html dokumenta
        return len(self.root.children) == 0