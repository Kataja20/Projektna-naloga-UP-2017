import random
import tkinter as tk

mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

indeksi = [0, 1, 2, 3]
mat[random.choice(indeksi)][random.choice(indeksi)] = 2


###################################################################################
###################################################################################
class Matrika:

    def __init__(self, okno, mat):
        self.mat = mat
        self.okno = okno

        self.igra(mat)

    def __str__(self):
        return "{}\n{}\n{}\n{}".format(self.mat[0], self.mat[1], self.mat[2], self.mat[3])

    def igralno_polje(self, mat):
        mat = self.mat
        okno = self.okno

        frame00=tk.Frame(okno, width=30, height=30, background="blue")
        frame00.grid(row=0, column=0)
        self.m00 = tk.Label(okno, text=str(mat[0][0])).grid(row=0, column=0)

        frame01=tk.Frame(okno, width=30, height=30, background="grey")
        frame01.grid(row=0, column=1)
        self.m01 = tk.Label(okno, text=str(mat[0][1])).grid(row=0, column=1)

        frame02=tk.Frame(okno, width=30, height=30, background="blue")
        frame02.grid(row=0, column=2)
        self.m02 = tk.Label(okno, text=str(mat[0][2])).grid(row=0, column=2)

        frame03=tk.Frame(okno, width=30, height=30, background="grey")
        frame03.grid(row=0, column=3)
        self.m03 = tk.Label(okno, text=str(mat[0][3])).grid(row=0, column=3)

        frame10=tk.Frame(okno, width=30, height=30, background="grey")
        frame10.grid(row=1, column=0)
        self.m10 = tk.Label(okno, text=str(mat[1][0])).grid(row=1, column=0)

        frame11=tk.Frame(okno, width=30, height=30, background="blue")
        frame11.grid(row=1, column=1)
        self.m11 = tk.Label(okno, text=str(mat[1][1])).grid(row=1, column=1)

        frame12=tk.Frame(okno, width=30, height=30, background="grey")
        frame12.grid(row=1, column=2)
        self.m12 = tk.Label(okno, text=str(mat[1][2])).grid(row=1, column=2)

        frame13=tk.Frame(okno, width=30, height=30, background="blue")
        frame13.grid(row=1, column=3)
        self.m13 = tk.Label(okno, text=str(mat[1][3])).grid(row=1, column=3)

        frame20=tk.Frame(okno, width=30, height=30, background="blue")
        frame20.grid(row=2, column=0)
        self.m20 = tk.Label(okno, text=str(mat[2][0])).grid(row=2, column=0)

        frame21=tk.Frame(okno, width=30, height=30, background="grey")
        frame21.grid(row=2, column=1)
        self.m21 = tk.Label(okno, text=str(mat[2][1])).grid(row=2, column=1)

        frame22=tk.Frame(okno, width=30, height=30, background="blue")
        frame22.grid(row=2, column=2)
        self.m22 = tk.Label(okno, text=str(mat[2][2])).grid(row=2, column=2)

        frame23=tk.Frame(okno, width=30, height=30, background="grey")
        frame23.grid(row=2, column=3)
        self.m23 = tk.Label(okno, text=str(mat[2][3])).grid(row=2, column=3)

        frame30=tk.Frame(okno, width=30, height=30, background="grey")
        frame30.grid(row=3, column=0)
        self.m30 = tk.Label(okno, text=str(mat[3][0])).grid(row=3, column=0)

        frame31=tk.Frame(okno, width=30, height=30, background="blue")
        frame31.grid(row=3, column=1)
        self.m31 = tk.Label(okno, text=str(mat[3][1])).grid(row=3, column=1)

        frame32=tk.Frame(okno, width=30, height=30, background="grey")
        frame32.grid(row=3, column=2)
        self.m32 = tk.Label(okno, text=str(mat[3][2])).grid(row=3, column=2)

        frame33=tk.Frame(okno, width=30, height=30, background="blue")
        frame33.grid(row=3, column=3)
        self.m33 = tk.Label(okno, text=str(mat[3][3])).grid(row=3, column=3)

        gumb_gor=tk.Button(okno, text="gor", command=self.go(mat)).grid(row=1, column=6)

        gumb_dol=tk.Button(okno, text="dol", command=self.do(mat)).grid(row=2, column=6)

        gumb_levo=tk.Button(okno, text="levo", command=self.le(mat)).grid(row=2, column=5)

        gumb_desno=tk.Button(okno, text="desno", command=self.de(mat)).grid(row=2, column=7)

    def igra(self, mat):
        mat = self.mat
        self.igralno_polje(mat)
        print(mat)
        self.osvezi_prikaz(mat)
    
    def nova_dvojka(self, mat):
        mat = self.mat
        kandidati_vrstica = []
        self.kandidati_stolpec = []
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
    

    def gor(self, mat):
        mat = self.mat
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
    def levo(self, mat):
        mat = self.mat
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
    def dol(self, mat):
        mat = self.mat
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
    def desno(self, mat):
        mat = self.mat
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

    def prazni_prostor(self, mat):
        mat = self.mat
        stevilo_nicel = 0
        for i in range(4):
            for j in range(4):
                if mat[i][j] == 0:
                    stevilo_nicel += 1
        return stevilo_nicel > 0

    def enaki_sosedi(self, mat):
        mat = self.mat
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

    def go(self, mat):
        mat = self.mat
        if self.prazni_prostor(mat) or self.enaki_sosedi(mat):
            stara_mat = mat
            nova_mat = self.gor(mat)
            if stara_mat != nova_mat:
                mat = nova_mat
                mat = self.nova_dvojka(mat)
                print(mat[0])
                print(mat[1])
                print(mat[2])
                print(mat[3])
                self.osvezi_prikaz(mat)

    def do(self, mat):
        mat = self.mat
        if self.prazni_prostor(mat) or self.enaki_sosedi(mat):
            stara_mat = mat
            nova_mat = self.dol(mat)
            if stara_mat != nova_mat:
                mat = nova_mat
                mat = self.nova_dvojka(mat)
                print(mat[0])
                print(mat[1])
                print(mat[2])
                print(mat[3])
                self.osvezi_prikaz(mat)

    def le(self, mat):
        mat = self.mat
        if self.prazni_prostor(mat) or self.enaki_sosedi(mat):
            stara_mat = mat
            nova_mat = self.levo(mat)
            if stara_mat != nova_mat:
                mat = nova_mat
                mat = self.nova_dvojka(mat)
                print(mat[0])
                print(mat[1])
                print(mat[2])
                print(mat[3])
                self.osvezi_prikaz(mat)

    def de(self, mat):
        mat = self.mat
        if self.prazni_prostor(mat) or self.enaki_sosedi(mat):
            stara_mat = mat
            nova_mat = self.desno(mat)
            if stara_mat != nova_mat:
                mat = nova_mat
                mat = self.nova_dvojka(mat)
                print(mat[0])
                print(mat[1])
                print(mat[2])
                print(mat[3])
                self.osvezi_prikaz(mat)
            

    def osvezi_prikaz(self, mat):
        mat = self.mat
        print('osvežena matrika: {}'.format(mat))
        self.m00.config(text=str(mat[0][0]))
        self.m01.config(text=str(mat[0][1]))
        self.m02.config(text=str(mat[0][2]))
        self.m03.config(text=str(mat[0][3]))

        self.m10.config(text=str(mat[1][0]))
        self.m11.config(text=str(mat[1][1]))
        self.m12.config(text=str(mat[1][2]))
        self.m13.config(text=str(mat[1][3]))

        self.m20.config(text=str(mat[2][0]))
        self.m21.config(text=str(mat[2][1]))
        self.m22.config(text=str(mat[2][2]))
        self.m23.config(text=str(mat[2][3]))

        self.m30.config(text=str(mat[3][0]))
        self.m31.config(text=str(mat[3][1]))
        self.m32.config(text=str(mat[3][2]))
        self.m33.config(text=str(mat[3][3]))
        

 
        

okno=tk.Tk()

okno.wm_title("2048")
matrika=Matrika(okno, mat)

okno.mainloop()
