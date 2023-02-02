def eredmeny():
    pass

def osszeg(kartyak: [int]):
    pontok: int = 0
    for i in range(len(kartyak)):
        pontok += kartyak[i]
    return pontok

def teszt_esetek():
    jatekos_vesztett()
teszt_esetek()

def jatekos_vesztett():
    jatekos = [10, 9, 3]
    gep = [10, 9]
    vart_eredmeny = "jatekos vesztett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("megbukott")