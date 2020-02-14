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
        print('GRESKA! U pretrazi ne sme da postoji vise od jednog logickog operatora.')
        return None, None
    elif len(saLogickimOperatorom) == 1:
        if delovi[0].upper() in ['AND', 'OR']:  # Pre svega se stavlja ogranicenje da AND i OR ne mogu da budu na prvom mestu u upitu
            print('GRESKA! Logicki operatori AND i OR ne mogu da stoje na pocetku pretrage.')
            return None, None
        for logickiOperator in saLogickimOperatorom:
            if logickiOperator.upper().__eq__('AND'):
                print('Uneli ste AND logicki operator.')
                if delovi[1].upper() != 'AND' or len(delovi) != 3: # Ako smo uneli AND, ono mora da stoji izmedju dve reci, ne sme da bude vise od 3 reci uneto
                    print('GRESKA! Logicki operator AND mora da bude izmedju tacno dve reci.')
                    return None, None
                print('AND je na dobrom mestu')
                return 'AND', reciUpita
            elif logickiOperator.upper().__eq__('OR'):
                print('Uneli ste OR logicki operator.')
                if delovi[1].upper() != 'OR' or len(delovi) != 3: # Ako smo uneli OR, ono mora da stoji izmedju dve reci, ne sme da bude vise od 3 reci uneto
                    print('GRESKA! Logicki operator OR mora da bude izmedju tacno dve reci.')
                    return None, None
                print('OR je na dobrom mestu')
                return 'OR', reciUpita
            elif logickiOperator.upper().__eq__('NOT'):
                print('Uneli ste NOT logicki operator.')
                if delovi[0].upper() == 'NOT' and len(delovi) != 2:   # Mora ova provera za slucaj kada se unese samo operator NOT u pretragu bez reci
                    print('GRESKA! Iza NOT mora da sledi tacno jedna rec.')
                    return None, None
                if delovi[0].upper() == 'NOT' and len(delovi) == 2:   # Slucaj kada se operator NOT nalazi na prvom mestu
                    print('NOT je na dobrom mestu (Prvom)')
                    return 'NOT1', reciUpita
                elif delovi[1].upper() == 'NOT' and len(delovi) == 3:   # Slucaj kada se operator NOT nalazi izmedju dve reci
                    print('NOT je na dobrom mestu (Izmedju dve reci)')
                    return 'NOT2', reciUpita
                else:
                    print('GRESKA! Logicki operator NOT mora da bude izmedju tacno dve reci ili na prvom mestu.')
                    return  None, None
    elif len(saLogickimOperatorom) == 0 and len(reciUpita) != 0:
        print('Uneli ste reci za pretragu bez logickih operatora.')
        return 'BEZ_LOG_OP', reciUpita
    elif len(saLogickimOperatorom) == 0 and len(reciUpita) == 0:    # Ukoliko se u pretragu ne unese nista
        print('GRESKA! Niste uneli validan upit.')
        return None, None
    else:
        print('GRESKA! Niste uneli validan upit.')
        return None, None
