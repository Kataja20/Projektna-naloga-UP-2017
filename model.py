from random import randint

mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

################################################################################

def nova_dvojka(mat):
    prosta_polja = []
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                prosta_polja.append([i, j])            
    [i, j] = prosta_polja[randint(0, len(prosta_polja)-1)]
    mat[i][j] = 2
    return mat

################################################################################
################################################################################

def premik_gor(mat):
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

################################################################################

def premik_dol(mat):
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

def premik_levo(mat): 
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

def premik_desno(mat):
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
    nova_dvojka(mat)
    print(mat)
    smer(mat)

def smer(mat):
    izbira_smeri = input("smer: ")
    if izbira_smeri == 'i':
        print('gor')
        premik_gor(mat)
        nova_dvojka(mat)
        print(mat[0])
        print(mat[1])
        print(mat[2])
        print(mat[3])
        nadaljevanje_igre(mat)
    elif izbira_smeri == 'k':
        print('dol')
        premik_dol(mat)
        nova_dvojka(mat)
        print(mat[0])
        print(mat[1])
        print(mat[2])
        print(mat[3])
        nadaljevanje_igre(mat)
    elif izbira_smeri == 'j':
        print('levo')
        premik_levo(mat)
        nova_dvojka(mat)
        print(mat[0])
        print(mat[1])
        print(mat[2])
        print(mat[3])
        nadaljevanje_igre(mat)
    elif izbira_smeri == 'l':
        print('desno')
        premik_desno(mat)
        nova_dvojka(mat)
        print(mat[0])
        print(mat[1])
        print(mat[2])
        print(mat[3])
        nadaljevanje_igre(mat)
    else:
        smer(mat)
    

        


def status_igre(mat):
    for i in range(4):
        if 2048 in mat[i]:
            return 'zmaga'
        elif 0 in mat[i]:
            return 'ni še konec'
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]:
                return 'ni še konec'
            if mat[3][i] == mat[3][i+1] or mat[i][3] == mat[i+1][3]:
                return 'ni še konec'
    
                
        
                
def nadaljevanje_igre(mat):
    if status_igre(mat) == 'ni še konec':
        smer(mat)
    elif status_igre(mat) == 'zmaga':
        print('Čestitamo!')
    else:
        print('Konec igre')
        mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]








