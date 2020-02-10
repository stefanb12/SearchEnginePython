class TrieNode:
    def __init__(self, parent = None, char = None):
        self.char = char
        if self.char is not None:
            self.char = self.char.lower()   # Pretraga treba da bude case insensitive
        self.parent = parent
        self.children = []
        self.end = False
        self.count = 0
        #self.html_file = html_file

class Trie:

    def __init__(self):
        self.root = TrieNode() # Koren je prazan cvor tj. nema u sebi nijedan karakter

    def add(self, word):
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
        curr_node.end = True
        curr_node.count += 1

    def search(self, word):
        word = word.lower().strip()
        if len(self.root.children) == 0:
            return False, 0

        node = self.root

        for char in word:
            char_not_found = True
            for child in node.children:
                if child.char == char:
                    char_not_found = False
                    node = child
                    break
            if char_not_found:
                return False, 0

        if node.end == False:
            return False, 0

        return node.end, node.count # U ovom slucaju je end = True i vraca se broj pojavljivanja reci

    def is_empty(self): # Koristi se za proveru da li je uneta validna putanja za parsiranje .html dokumenta
        return len(self.root.children) == 0