def eredmeny(jatekosLapok: [int], gepLapok: [int]):
    pass

def osszeg(kartyak: [int]):
    pontok: int = 0
    for i in range(len(kartyak)):
        pontok += kartyak[i]
    return pontok

def jatekos_vesztett_tobbMintHuszonegy():
    jatekos = [10, 9, 6]
    gep = [10, 10]
    vart_eredmeny = "jatekos vesztett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("megbukott")
    pass

def jatekos_vesztett_kevesebbMintHuszonegy():
    jatekos = [10, 8]
    gep = [10, 9, 2]
    vart_eredmeny = "jatekos vesztett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("megbukott")

def jatekos_vesztett_tobbLapbolHuszonegy():
    jatekos = [10, 5, 2, 4]
    gep = [10, 9, 2]
    vart_eredmeny = "jatekos vesztett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("megbukott")

def jatekos_vesztett_kisebbEredmenyMintAGepnek():
    jatekos = [10, 8]
    gep = [10, 10]
    vart_eredmeny = "jatekos vesztett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("megbukott")

def teszt_esetek():
    jatekos_vesztett_tobbMintHuszonegy()
    jatekos_vesztett_kevesebbMintHuszonegy()
    jatekos_vesztett_tobbLapbolHuszonegy()
    jatekos_vesztett_kisebbEredmenyMintAGepnek()

teszt_esetek()