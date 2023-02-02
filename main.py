def osszeg(kartyak: [int]):
    pontok: int = 0
    for i in range(len(kartyak)):
        pontok += kartyak[i]
    return pontok

def lapDarab(kartyak: [int]):
    db: int = 0
    for i in range(len(kartyak)):
        db += 1
    return db

def eredmeny(jatekosLapok: [int], gepLapok: [int]):
    jatekosLapOsszeg = osszeg(jatekosLapok)
    gepLapOsszeg = osszeg(gepLapok)
    jatekosLapDarab = lapDarab(jatekosLapok)
    gepLapDarab = lapDarab(gepLapok)

    vegEredmeny = ""

    if jatekosLapOsszeg <= 21 and gepLapOsszeg <= 21:
        if jatekosLapOsszeg > gepLapOsszeg:
            vegEredmeny = "Játékos nyert!"
        elif gepLapOsszeg > jatekosLapOsszeg:
            vegEredmeny = "Gép nyert!"
        elif gepLapOsszeg == jatekosLapOsszeg:
            if jatekosLapDarab < gepLapDarab:
                vegEredmeny = "Játékos nyert!"
            elif jatekosLapDarab > gepLapDarab:
                vegEredmeny = "Gép nyert!"
            else:
                vegEredmeny = "Döntetlen, osztoztok a nyereségben!"
    else:
        if jatekosLapOsszeg > 21:
            vegEredmeny = "Játékos vesztett!"
        elif gepLapOsszeg > 21:
            vegEredmeny = "Gép vesztett!"
        elif jatekosLapOsszeg > 21 and gepLapOsszeg > 21:
            vegEredmeny = "Döntetlen, a Ház nyert!"

    print(vegEredmeny)
    return vegEredmeny
#jatekos vesztett

def gep_nyert_tobbMintHuszonegy():
    jatekos = [10, 9, 6]
    gep = [10, 10]
    vart_eredmeny = "Játékos vesztett!"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Több mint 21 tesztje]: teszt sikeres")
    else:
        print("[Több mint 21 tesztje]: megbukott")
    pass

def gep_nyert_kevesebbMintHuszonegy():
    jatekos = [10, 8]
    gep = [10, 9, 2]
    vart_eredmeny = "Gép nyert!"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Kevesebb mint 21 tesztje]: teszt sikeres")
    else:
        print("[Kevesebb mint 21 tesztje]: megbukott")

def gep_nyert_tobbLapbolHuszonegy():
    jatekos = [10, 5, 2, 4]
    gep = [10, 9, 2]
    vart_eredmeny = "Gép nyert!"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Több lapból 21 tesztje]: teszt sikeres")
    else:
        print("[Több lapból 21 tesztje]: megbukott")

def gep_nyert_kisebbEredmeny():
    jatekos = [10, 8]
    gep = [10, 10]
    vart_eredmeny = "Gép nyert!"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Kisebb eredmény tesztje]: teszt sikeres")
    else:
        print("[Kisebb eredmény tesztje]: megbukott")

#gep vesztett

def jatekos_nyert_tobbMintHuszonegy():
    jatekos = [10, 9, 2]
    gep = [10, 8, 6]
    vart_eredmeny = "Gép vesztett!"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Kisebb eredmény tesztje]: teszt sikeres")
    else:
        print("[Kisebb eredmény tesztje]: megbukott")

def jatekos_nyert_kevesebbMintHuszonegy():
    jatekos = [10, 8]
    gep = [10, 7]
    vart_eredmeny = "Játékos nyert!"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Kisebb eredmény tesztje]: teszt sikeres")
    else:
        print("[Kisebb eredmény tesztje]: megbukott")

def jatekos_nyert_tobbLapbolHuszonegy():
    jatekos = [10, 3, 6, 2]
    gep = [4, 3, 3, 4, 2, 3, 2]
    vart_eredmeny = "Játékos nyert!"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Több lapból 21 tesztje]: teszt sikeres")
    else:
        print("[Több lapból 21 tesztje]: megbukott")

def jatekos_nyert_kisebbEredmeny():
    jatekos = [10, 10]
    gep = [10, 8]
    vart_eredmeny = "Játékos nyert!"
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
    vart_eredmeny = "dontetlen"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[Egyenlő lapok döntetlenjének tesztje]: teszt sikeres")
    else:
        print("[Egyenlő lapok döntetlenjének tesztje]: megbukott")

def dontetlen_egyenloLapok_TobbMint21():
    jatekos = [10, 6, 3, 5]
    gep = [10, 5, 4, 5]
    vart_eredmeny = "dontetlen"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[21 felett egyenlő lapok tesztje]: teszt sikeres")
    else:
        print("[21 felett egyenlő lapok tesztje]: megbukott")

def dontetlen_egyenloEredmeny_TobbMint21():
    jatekos = [10, 10, 6]
    gep = [10, 6, 4, 6]
    vart_eredmeny = "döntetlen"
    kapott_eredmeny = eredmeny(jatekos, gep)
    if kapott_eredmeny == vart_eredmeny:
        print("[21 felett egyenlő eredmény tesztje]: teszt sikeres")
    else:
        print("[21 felett egyenlő eredmény tesztje]: megbukott")


def teszt_esetek():

    #Játékos vesztett esetek:

    gep_nyert_tobbMintHuszonegy()
    gep_nyert_kevesebbMintHuszonegy()
    gep_nyert_tobbLapbolHuszonegy()
    gep_nyert_kisebbEredmeny()

    #Gép vesztett esetek:
    jatekos_nyert_tobbMintHuszonegy()
    jatekos_nyert_kevesebbMintHuszonegy()
    jatekos_nyert_tobbLapbolHuszonegy()
    jatekos_nyert_kisebbEredmeny()

teszt_esetek()