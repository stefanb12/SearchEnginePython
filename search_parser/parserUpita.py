def parsiraj_upit(upit):

    delovi = upit.split()
    saLogickimOperatorom = []
    reciUpita = []

    for deo in delovi:
        if deo.upper() in ['AND', 'OR', 'NOT']:
            saLogickimOperatorom.append(deo)
        else:
            reciUpita.append(deo)

    if len(saLogickimOperatorom) > 1: # Ako je duzina veca od jedan znaci da je uneto vise logickih operatora
        print('\nGREŠKA! U pretrazi ne sme da postoji više od jednog logičkog operatora.\n')
        return None, None
    elif len(saLogickimOperatorom) == 1:
        if delovi[0].upper() in ['AND', 'OR', 'NOT']:  # Pre svega se stavlja ogranicenje da AND i OR ne mogu da budu na prvom mestu u upitu
            print('\nGREŠKA! Logički operatori AND, OR i NOT ne mogu da stoje na početku pretrage.\n')
            return None, None
        for logickiOperator in saLogickimOperatorom:
            if logickiOperator.upper().__eq__('AND'):
                if delovi[1].upper() != 'AND' or len(delovi) != 3: # Ako smo uneli AND, ono mora da stoji izmedju dve reci, ne sme da bude vise od 2 reci uneto
                    print('\nGREŠKA! Logički operator AND mora da bude između tačno dve reči.\n')
                    return None, None
                return 'AND', reciUpita
            elif logickiOperator.upper().__eq__('OR'):
                if delovi[1].upper() != 'OR' or len(delovi) != 3: # Ako smo uneli OR, ono mora da stoji izmedju dve reci, ne sme da bude vise od 2 reci uneto
                    print('\nGREŠKA! Logički operator OR mora da bude između tačno dve reči.\n')
                    return None, None
                return 'OR', reciUpita
            elif logickiOperator.upper().__eq__('NOT'):
                if delovi[1].upper() != 'NOT' or len(delovi) != 3: # Ako smo uneli NOT, ono mora da stoji izmedju dve reci, ne sme da bude vise od 2 reci uneto
                    print('\nGREŠKA! Logički operator NOT mora da bude između tačno dve reči.\n')
                    return None, None
                return 'NOT', reciUpita
    elif len(saLogickimOperatorom) == 0 and len(reciUpita) != 0:
        bezDuplikata = []   # U slucaju da se unese vise puta ista rec, ne treba sabirati broj pojavljivanja reci na istim stranicama, pa vracamo reci upita bez duplikata
        for rec in reciUpita:
            if rec not in bezDuplikata:
                bezDuplikata.append(rec)
        return 'BEZ_LOG_OP', bezDuplikata
    elif len(saLogickimOperatorom) == 0 and len(reciUpita) == 0: # Ukoliko se u pretragu ne unese nista
        print('\nGREŠKA! Morate uneti reči koje želite da pretražite.\n')
        return None, None
    else:
        print('\nGREŠKA! Niste uneli validan upit.\n')
        return None, None
