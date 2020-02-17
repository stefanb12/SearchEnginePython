def pretrazi_dokumente(operator, reciUpita, trie):
    if operator == 'AND':   # Ukoliko je unet AND operator postojace dve reci za pretragu, u suprotnom ce biti prijavljena greska
        postoji1, set1, recnik1 = trie.search(reciUpita[0])
        postoji2, set2, recnik2 = trie.search(reciUpita[1])
        print('Skup za rec', reciUpita[0], ':')
        for putanja in set1.skup.keys():
            print(putanja)
        print('Skup za rec', reciUpita[1], ':')
        for putanja in set2.skup.keys():
            print(putanja)
    elif operator == 'OR':  # Ukoliko je unet OR operator postojace dve reci za pretragu, u suprotnom ce biti prijavljena greska
        postoji1, set1, recnik1 = trie.search(reciUpita[0])
        postoji2, set2, recnik2 = trie.search(reciUpita[1])
        print('Skup za rec', reciUpita[0], ':')
        for putanja in set1.skup.keys():
            print(putanja)
        print('Skup za rec', reciUpita[1], ':')
        for putanja in set2.skup.keys():
            print(putanja)
    elif operator == 'NOT':  # Ukoliko je unet NOT operator postojace dve reci za pretragu, u suprotnom ce biti prijavljena greska
        postoji1, set1, recnik1 = trie.search(reciUpita[0])
        postoji2, set2, recnik2 = trie.search(reciUpita[1])
        print('Skup za rec', reciUpita[0], ':')
        for putanja in set1.skup.keys():
            print(putanja)
        print('Skup za rec', reciUpita[1], ':')
        for putanja in set2.skup.keys():
            print(putanja)
    elif operator == 'BEZ_LOG_OP':
        broj_reci = len(reciUpita)
        i = 0
        for i in range(broj_reci):
            postoji, set, recnik = trie.search(reciUpita[i])   # Za svaku unetu rec u upitu se odredjuje skup
            print('Skup za rec', reciUpita[i], ':')
            for putanja in set.skup.keys():
                print(putanja)
            i += 1

    # else slucaj nije potreban zato sto se u parsiraj_upit ispisuju poruke o greskama ukoliko nije unet validan upit.

