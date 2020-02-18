from set import Set

def pretrazi_dokumente(operator, reciUpita, trie):
    if operator == 'AND':   # Ukoliko je unet AND operator postojace dve reci za pretragu, u suprotnom ce biti prijavljena greska
        postoji1, set1, recnik1 = trie.search(reciUpita[0])
        postoji2, set2, recnik2 = trie.search(reciUpita[1])

        if postoji1 == False or postoji2 == False:
            print('Ne postoje HTML dokumenti koji zadovoljavaju upit koji ste uneli.')
            return None, None
        elif postoji1 == True and postoji2 == True:
            rezRecnik = {}
            rezSet = Set()
            if reciUpita[0] == reciUpita[1]: # Ukoliko je uneta ista rec pre i posle operatora and, rezultat ce biti samo prvi skup (ne treba duplirati broj poajvljivanja reci na stranici)
                return set1, recnik1
            rezSet = set1.intersection(set2)
            for putanja in rezSet.skup.keys():
                rezRecnik[putanja] = recnik1[putanja] + recnik2[putanja]  # Potrebno je sabrati proj prikazivanja reci na istim stranicama prve i druge reci
            return rezSet, rezRecnik
    elif operator == 'OR':  # Ukoliko je unet OR operator postojace dve reci za pretragu, u suprotnom ce biti prijavljena greska
        postoji1, set1, recnik1 = trie.search(reciUpita[0])
        postoji2, set2, recnik2 = trie.search(reciUpita[1])

        if postoji1 == False and postoji2 == False:
            print('Ne postoje HTML dokumenti koji zadovoljavaju upit koji ste uneli.')
            return None, None
        elif postoji1 == True and postoji2 == False: # Ukoliko postji skup samo za prvu rec, rezultujuci skup je prvi skup
            return set1, recnik1
        elif postoji2 == True and postoji1 == False: # # Ukoliko postji skup samo za drugu rec, rezultujuci skup je drugi skup
            return set2, recnik2
        elif postoji1 == True and postoji2 == True:
            rezRecnik = {}
            rezSet = Set()
            if reciUpita[0] == reciUpita[1]: # Ukoliko je uneta ista rec pre i posle operatora or rezulat je prvi skup (ne treba duplirati broj pojavljivanja reci  na stranici)
                return set1, recnik1
            rezSet = set1.union(set2)
            for putanja in rezSet.skup.keys():
                if putanja in recnik1.keys() and putanja in recnik2.keys():  # Potrebno je sabrati brojeve prikazivanja prve i druge reci za iste putanje
                    rezRecnik[putanja] = recnik1[putanja] + recnik2[putanja]
                elif putanja in recnik1.keys():                              # Ako je putanja iz prvog recnika treba broj prikazivanja reci iz prvog recnika
                    rezRecnik[putanja] = recnik1[putanja]
                else:                                                        # U ovom slcaju ce putanja biti iz drugog recnika pa treba broj iz drugo recnika
                    rezRecnik[putanja] = recnik2[putanja]
            return rezSet, rezRecnik
    elif operator == 'NOT':  # Ukoliko je unet NOT operator postojace dve reci za pretragu, u suprotnom ce biti prijavljena greska
        postoji1, set1, recnik1 = trie.search(reciUpita[0])
        postoji2, set2, recnik2 = trie.search(reciUpita[1])

        if postoji1 == False:  # Ako ne postoje fajlovi koji sadrze prvu rec upita (rec pre not) rezulat pretrage ce uvek biti bez fajlova
            print('Ne postoje HTML dokumenti koji zadovoljavaju upit koji ste uneli.')
            return None, None
        elif postoji1 == True and postoji2 == False:  # Ako ne postoje fajlovi koji sadrze rec posle not, rezultat ce uvek biti skup prve reci
            return set1, recnik1
        elif postoji1 == True and postoji2 == True:  # Ako postoji skup za obe reci upita, resenje je njihov komplement
            rezRecnik = {}
            rezSet = Set()
            if reciUpita[0] == reciUpita[1]:    # Ukoliko je uneta ista rec pre i posle not operatora, rezulat ce uvek biti prazan skup
                print('Ne postoje HTML dokumenti koji zadovoljavaju upit koji ste uneli.')
                return None, None
            rezSet = set1.complement(set2)
            for putanja in rezSet.skup.keys():
                rezRecnik[putanja] = recnik1[putanja]   # Broj prikazivanja reci po stranici ce uvek biti iz prvog skupa
            return rezSet, rezRecnik
    elif operator == 'BEZ_LOG_OP':
        rezRecnik = {}
        rezSet = Set()
        broj_reci = len(reciUpita)  # Broj reci unetih u upit
        i = 0
        for i in range(broj_reci):
            postoji, set, recnik = trie.search(reciUpita[i]) # Za svaku rec unetu u upitu vracamo skup putanja i recnik (putanja, broj pojavljivanja reci na putanji)
            i += 1
            if postoji == True: # Ukoliko postoji skup za unetu rec pozivamo uniju sa prethodnim rezultujucim skupom
                rezSet = rezSet.union(set)
                if i == 1:  # Prvi put u rezultujuci recnik ubacujemo parove (putanja, broj prikazivanja reci na putanji) od prve reci
                    for putanja in set.skup.keys():
                        rezRecnik[putanja] = recnik[putanja]
                elif i > 1: # Za svaku sledecu unetu rec sabiramo proj pojavljivanja reci na putanjama koje su iste
                    rezRecnik = saberiBrojeveIstihPutanja(rezSet, rezRecnik, recnik)

        if len(rezSet.skup) == 0:
            print('Ne postoje HTML dokumenti koji zadovoljavaju upit koji ste uneli.')
            return None, None
        else:
            return rezSet, rezRecnik
    # else slucaj nije potreban zato sto se u parsiraj_upit ispisuju poruke o greskama ukoliko nije unet validan upit.

def saberiBrojeveIstihPutanja(rezSet, stari_recnik, novi_recnik):  # U rezultujucem recniku sabiramo brojeve pojavljivanja reci na istim putanjama
    rezRecnik = {}
    for putanja in rezSet.skup.keys():
        if putanja in stari_recnik.keys() and putanja not in novi_recnik.keys(): # Ukoliko se putanja pojavljuje u starom recniku, broj pojavljivanja reci je iz starog recnika
            rezRecnik[putanja] = stari_recnik[putanja]
        elif putanja in novi_recnik.keys() and putanja not in stari_recnik.keys(): # Ukoliko se putanja pojavljuje u novom recniku, broj pojavljivanja reci je iz starog recnika
            rezRecnik[putanja] = novi_recnik[putanja]
        elif putanja in stari_recnik.keys() and putanja in novi_recnik.keys(): # Ukoliko se putanja pojavljuje u oba recnika, potrebno je sabrati broj prikazivanja reci za tu istu putanju
            rezRecnik[putanja] = novi_recnik[putanja] + stari_recnik[putanja]
    return rezRecnik

