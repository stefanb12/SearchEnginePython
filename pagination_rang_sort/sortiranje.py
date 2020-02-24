def sortiraj(lista):
    if len(lista) > 1:
        polovina = len(lista) // 2  #pronalazak sredine liste

        #podela liste na polovine
        leva_polovina = lista[:polovina]
        desna_polovina = lista[polovina:]

        #sortiranje leve i desne polovine
        sortiraj(leva_polovina)
        sortiraj(desna_polovina)

        i = j = k = 0

        while i < len(leva_polovina) and j < len(desna_polovina):
            if leva_polovina[i] > desna_polovina[j]:
                lista[k] = leva_polovina[i]
                i += 1
            else:
                lista[k] = desna_polovina[j]
                j += 1
            k += 1

        while i < len(leva_polovina):
            lista[k] = leva_polovina[i]
            i += 1
            k += 1

        while j < len(desna_polovina):
            lista[k] = desna_polovina[j]
            j += 1
            k += 1
