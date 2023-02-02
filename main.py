def osszeg(kartyak: [int]):
    pontok: int = 0
    for i in range(len(kartyak)):
        pontok += kartyak[i]
    return pontok

def eredmeny(jatekosLapok: [int], gepLapok: [int]):
    pass

#jatekos vesztett

def jatekos_vesztett_tobbMintHuszonegy():
    jatekos = [10, 9, 6]
    gep = [10, 10]
    vart_eredmeny = "jatekos vesztett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Több mint 21 tesztje]: teszt sikeres")
    else:
        print("[Több mint 21 tesztje]: megbukott")
    pass

def jatekos_vesztett_kevesebbMintHuszonegy():
    jatekos = [10, 8]
    gep = [10, 9, 2]
    vart_eredmeny = "jatekos vesztett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Kevesebb mint 21 tesztje]: teszt sikeres")
    else:
        print("[Kevesebb mint 21 tesztje]: megbukott")

def jatekos_vesztett_tobbLapbolHuszonegy():
    jatekos = [10, 5, 2, 4]
    gep = [10, 9, 2]
    vart_eredmeny = "jatekos vesztett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Több lapból 21 tesztje]: teszt sikeres")
    else:
        print("[Több lapból 21 tesztje]: megbukott")

def jatekos_vesztett_kisebbEredmeny():
    jatekos = [10, 8]
    gep = [10, 10]
    vart_eredmeny = "jatekos vesztett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Kisebb eredmény tesztje]: teszt sikeres")
    else:
        print("[Kisebb eredmény tesztje]: megbukott")

#gep vesztett

def gep_vesztett_tobbMintHuszonegy():
    jatekos = [10, 9, 2]
    gep = [10, 8, 6]
    vart_eredmeny = "gep vesztett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Kisebb eredmény tesztje]: teszt sikeres")
    else:
        print("[Kisebb eredmény tesztje]: megbukott")

def gep_vesztett_kevesebbMintHuszonegy():
    jatekos = [10, 9, 2]
    gep = [10, 8, 6]
    vart_eredmeny = "gep vesztett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Kisebb eredmény tesztje]: teszt sikeres")
    else:
        print("[Kisebb eredmény tesztje]: megbukott")

def gep_vesztett_tobbLapbolHuszonegy():
    jatekos = [10, 3, 6, 2]
    gep = [4, 3, 3, 4, 2, 3, 2]
    vart_eredmeny = "gep vesztett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Több lapból 21 tesztje]: teszt sikeres")
    else:
        print("[Több lapból 21 tesztje]: megbukott")

def gep_vesztett_kisebbEredmeny():
    jatekos = [10, 10]
    gep = [10, 8]
    vart_eredmeny = "gep vesztett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Kisebb eredmény tesztje]: teszt sikeres")
    else:
        print("[Kisebb eredmény tesztje]: megbukott")


#dontetlen tesztesetek
def dontetlen_egyenloEredmeny():
    jatekos = [10, 10]
    gep = [10, 10]
    vart_eredmeny = "dontetlen"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Egyenlő eredmény döntetlenjének tesztje]: teszt sikeres")
    else:
        print("[Egyenlő eredmény döntetlenjének tesztje]: megbukott")

def dontetlen_egyenloLapok():
    jatekos = [10, 6, 3]
    gep = [10, 5, 4]
    vart_eredmeny = "gep vesztett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Egyenlő lapok döntetlenjének tesztje]: teszt sikeres")
    else:
        print("[Egyenlő lapok döntetlenjének tesztje]: megbukott")

def dontetlen_egyenloLapok_TobbMint21():
    jatekos = [10, 6, 3, 5]
    gep = [10, 5, 4, 5]
    vart_eredmeny = "gep vesztett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[21 felett egyenlő lapok tesztje]: teszt sikeres")
    else:
        print("[21 felett egyenlő lapok tesztje]: megbukott")

def dontetlen_egyenloEredmeny_TobbMint21():
    jatekos = [10, 10, 6]
    gep = [10, 6, 4, 6]
    vart_eredmeny = "gep vesztett"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[21 felett egyenlő eredmény tesztje]: teszt sikeres")
    else:
        print("[21 felett egyenlő eredmény tesztje]: megbukott")


def teszt_esetek():

    #Játékos vesztett esetek:

    jatekos_vesztett_tobbMintHuszonegy()
    jatekos_vesztett_kevesebbMintHuszonegy()
    jatekos_vesztett_tobbLapbolHuszonegy()
    jatekos_vesztett_kisebbEredmeny()

    #Gép vesztett esetek:
    gep_vesztett_tobbMintHuszonegy()
    gep_vesztett_kevesebbMintHuszonegy()
    gep_vesztett_tobbLapbolHuszonegy()
    gep_vesztett_kisebbEredmeny()

teszt_esetek()