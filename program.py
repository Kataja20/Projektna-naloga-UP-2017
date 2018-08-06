import random

### NAVODILA ###
# Napiši ukaz: zacetek(mat), izberi smer, pritisni Enter
# i = gor
# j = levo
# l = desno
# k = dol



mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

indeksi = [0, 1, 2, 3]
mat[random.choice(indeksi)][random.choice(indeksi)] = 2
# random.choice(indeksi) nam iz nabora indeksi naključno izbere en člen,
# kar nam določi, v katerem polju plošče se bo pojavila številka 2

###############################################################################
def nova_dvojka(mat):
    kandidati_vrstica = []
    kandidati_stolpec = []
    prazna_polja = 0
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                kandidati_vrstica.append(i)
                kandidati_stolpec.append(j)
                prazna_polja +=1
    nakljucni_indeks = kandidati_vrstica.index(random.choice(kandidati_vrstica))
    mat[kandidati_vrstica[nakljucni_indeks]][kandidati_stolpec[nakljucni_indeks]] = 2
    return mat


################################################################################
def gor(mat):
    # s for zanko se bomo peljali po stolpcih, vrstice pa bomo
    # spreminjali ročno
    i = 0
    for j in range(4):
        if mat[i][j] == 0 and (mat[i+1][j] != 0 or mat[i+2][j] != 0 or mat[i+3][j] != 0):
            while mat[i][j] == 0:
                mat[i][j] = mat[i+1][j]
                mat[i+1][j] = mat[i+2][j]
                mat[i+2][j] = mat[i+3][j]
                mat[i+3][j] = 0
            if mat[i+1][j] == 0 and mat[i+2][j] != 0:
                mat[i+1][j] = mat[i+2][j]
                mat[i+2][j] = 0
        else:
            if mat[i+1][j] == 0 and (mat[i+2][j] != 0 or mat[i+3][j] != 0):
                while mat[i+1][j] == 0:
                    mat[i+1][j] = mat[i+2][j]
                    mat[i+2][j] = mat[i+3][j]
                    mat[i+3][j] = 0
            else:
                if mat[i+2][j] == 0 and mat[i+3][j] != 0:
                    mat[i+2][j] = mat[i+3][j]
                    mat[i+3][j] = 0
    i = 0
    for j in range(4):
        if mat[i][j] == mat[i+1][j]:
            mat[i][j] += mat[i+1][j]
            mat[i+1][j] = mat[i+2][j]
            mat[i+2][j] = mat[i+3][j]
            mat[i+3][j] = 0
            if mat[i+1][j] == mat[i+2][j]:
                mat[i+1][j] += mat[i+2][j]
                mat[i+2][j] = 0
        elif mat[i+1][j] == mat[i+2][j]:
            mat[i+1][j] += mat[i+2][j]
            mat[i+2][j] = mat[i+3][j]
            mat[i+3][j] = 0
        elif mat[i+2][j] == mat[i+3][j]:
            mat[i+2][j] += mat[i+3][j]
            mat[i+3][j] = 0
        

    return mat

###############################################################################
def levo(mat):
    # s for zanko se bomo peljali po vrsticah, stolpce pa bomo spreminjali ročno
    j = 0
    for i in range(4):
        if mat[i][j] == 0 and (mat[i][j+1] != 0 or mat[i][j+2] != 0 or mat[i][j+3] != 0):
            while mat[i][j] == 0:
                mat[i][j] = mat[i][j+1]
                mat[i][j+1] = mat[i][j+2]
                mat[i][j+2] = mat[i][j+3]
                mat[i][j+3] = 0
            if mat[i][j+1] == 0 and mat[i][j+2] != 0:
                mat[i][j+1] = mat[i][j+2]
                mat[i][j+2] = 0
        else:
            if mat[i][j+1] == 0 and (mat[i][j+2] != 0 or mat[i][j+3] != 0):
                while mat[i][j+1] == 0:
                    mat[i][j+1] = mat[i][j+2]
                    mat[i][j+2] = mat[i][j+3]
                    mat[i][j+3] = 0
            else:
                if mat[i][j+2] == 0 and mat[i][j+3] != 0:
                    mat[i][j+2] = mat[i][j+3]
                    mat[i][j+3] = 0
    j = 0 
    for i in range(4):
        if mat[i][j] == mat[i][j+1]:
            mat[i][j] += mat[i][j+1]
            mat[i][j+1] = mat[i][j+2]
            mat[i][j+2] = mat[i][j+3]
            mat[i][j+3] = 0
            if mat[i][j+1] == mat[i][j+2]:
                mat[i][j+1] += mat[i][j+2]
                mat[i][j+2] = 0
        elif mat[i][j+1] == mat[i][j+2]:
            mat[i][j+1] += mat[i][j+2]
            mat[i][j+2] = mat[i][j+3]
            mat[i][j+3] = 0
        elif mat[i][j+2] == mat[i][j+3]:
            mat[i][j+2] += mat[i][j+3]
            mat[i][j+3] = 0

    return mat

################################################################################
def dol(mat):
    # s for zanko se bomo peljali po stolpcih, vrstice pa bomo
    # spreminjali ročno
    i = 0
    for j in range(4):
        if mat[i+3][j] == 0 and (mat[i+2][j] != 0 or mat[i+1][j] != 0 or mat[i][j] != 0):
            while mat[i+3][j] == 0:
                mat[i+3][j] = mat[i+2][j]
                mat[i+2][j] = mat[i+1][j]
                mat[i+1][j] = mat[i][j]
                mat[i][j] = 0
            if mat[i+2][j] == 0 and mat[i+1][j] != 0:
                mat[i+2][j] = mat[i+1][j]
                mat[i+1][j] = 0
        else:
            if mat[i+2][j] == 0 and (mat[i+1][j] != 0 or mat[i][j] != 0):
                while mat[i+2][j] == 0:
                    mat[i+2][j] = mat[i+1][j]
                    mat[i+1][j] = mat[i][j]
                    mat[i][j] = 0
            else:
                if mat[i+1][j] == 0 and mat[i][j] != 0:
                    mat[i+1][j] = mat[i][j]
                    mat[i][j] = 0
    i = 0
    for j in range(4):
        if mat[i+3][j] == mat[i+2][j]:
            mat[i+3][j] += mat[i+2][j]
            mat[i+2][j] = mat[i+1][j]
            mat[i+1][j] = mat[i][j]
            mat[i][j] = 0
            if mat[i+2][j] == mat[i+1][j]:
                mat[i+2][j] += mat[i+1][j]
                mat[i+1][j] = 0
        elif mat[i+2][j] == mat[i+1][j]:
            mat[i+2][j] += mat[i+1][j]
            mat[i+1][j] = mat[i][j]
            mat[i][j] = 0
        elif mat[i+1][j] == mat[i][j]:
            mat[i+1][j] += mat[i][j]
            mat[i][j] = 0

    return mat
################################################################################
def desno(mat):
    # s for zanko se bomo peljali po vrsticah, stolpce pa bomo spreminjali ročno
    j = 0
    for i in range(4):
        if mat[i][j+3] == 0 and (mat[i][j+2] != 0 or mat[i][j+1] != 0 or mat[i][j] != 0):
            while mat[i][j+3] == 0:
                mat[i][j+3] = mat[i][j+2]
                mat[i][j+2] = mat[i][j+1]
                mat[i][j+1] = mat[i][j]
                mat[i][j] = 0
            if mat[i][j+2] == 0 and mat[i][j+1] != 0:
                mat[i][j+2] = mat[i][j+1]
                mat[i][j+1] = 0
        else:
            if mat[i][j+2] == 0 and (mat[i][j+1] != 0 or mat[i][j] != 0):
                while mat[i][j+2] == 0:
                    mat[i][j+2] = mat[i][j+1]
                    mat[i][j+1] = mat[i][j]
                    mat[i][j] = 0
            else:
                if mat[i][j+1] == 0 and mat[i][j] != 0:
                    mat[i][j+1] = mat[i][j]
                    mat[i][j] = 0
    j = 0
    
    for i in range(4):
        if mat[i][j+3] == mat[i][j+2]:
            mat[i][j+3] += mat[i][j+2]
            mat[i][j+2] = mat[i][j+1]
            mat[i][j+1] = mat[i][j]
            mat[i][j] = 0
            if mat[i][j+2] == mat[i][j+1]:
                mat[i][j+2] += mat[i][j+1]
                mat[i][j+1] = 0
        elif mat[i][j+2] == mat[i][j+1]:
            mat[i][j+2] += mat[i][j+1]
            mat[i][j+1] = mat[i][j]
            mat[i][j] = 0
        elif mat[i][j+1] == mat[i][j]:
            mat[i][j+1] += mat[i][j]
            mat[i][j] = 0

    return mat        

################################################################################
################################################################################

def zacetek(mat):
    izpis(mat)
    izbira_smeri(mat)

def prazni_prostor(mat):
    stevilo_nicel = 0
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                stevilo_nicel += 1
    return stevilo_nicel > 0

def enaki_sosedi(mat):
    enaka_soseda = 0
    i = 0
    for j in range(3):
        if mat[i][j] == mat[i+1][j] or mat[i+1][j] == mat[i+2][j]:
            enaka_soseda += 1
    j = 0
    for i in range(3):
        if mat[i][j] == mat[i][j+1] or mat[i][j+1] == mat[i][j+2]:
            enaka_soseda += 1
    return enaka_soseda > 0

def izbira_smeri(mat):
    izbira_igralca = input("smer: ")
    # igralec izbere GOR
    if izbira_igralca == 'i' and (prazni_prostor(mat) or enaki_sosedi(mat)):
        stara_mat = mat
        nova_mat = gor(mat)
        if (stara_mat != nova_mat) == 'True':
            nova_dvojka(nova_mat)
            izpis(mat)
            izbira_smeri(mat)
            
    # igralec izbere DOL
    if izbira_igralca == 'k' and (prazni_prostor(mat) or enaki_sosedi(mat)):
        stara_mat = mat
        nova_mat = dol(mat)
        if (stara_mat != nova_mat) == 'True':
            nova_dvojka(nova_mat)
            izpis(mat)
            izbira_smeri(mat)
            
    # igralec izbere LEVO
    if izbira_igralca == 'j' and (prazni_prostor(mat) or enaki_sosedi(mat)):
        stara_mat = mat
        nova_mat = levo(mat)
        if (stara_mat != nova_mat) == 'True':
            nova_dvojka(nova_mat)
            izpis(mat)
            izbira_smeri(mat)
        
    # igralec izbere DESNO
    if izbira_igralca == 'l' and (prazni_prostor(mat) or enaki_sosedi(mat)):
        stara_mat = mat
        nova_mat = desno(mat)
        if (stara_mat != nova_mat) == 'True':
            nova_dvojka(nova_mat)
            izpis(mat)
            izbira_smeri(mat)
        
          
def izpis(mat):
    print(mat[0])
    print(mat[1])
    print(mat[2])
    print(mat[3])
        
