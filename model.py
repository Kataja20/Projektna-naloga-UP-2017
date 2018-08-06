import tkinter as tk

okno = tk.Tk()

frame00=tk.Frame(okno, width=30, height=30, background="blue").grid(row=0, column=0)
m00 = tk.Label(okno, text='0').grid(row=0, column=0)

frame01=tk.Frame(okno, width=30, height=30, background="grey").grid(row=0, column=1)
m01 = tk.Label(okno, text='0').grid(row=0, column=1)

frame02=tk.Frame(okno, width=30, height=30, background="blue").grid(row=0, column=2)
m02 = tk.Label(okno, text='0').grid(row=0, column=2)

frame03=tk.Frame(okno, width=30, height=30, background="grey").grid(row=0, column=3)
m03 = tk.Label(okno, text='0').grid(row=0, column=3)

frame10=tk.Frame(okno, width=30, height=30, background="grey").grid(row=1, column=0)
m10 = tk.Label(okno, text='0').grid(row=1, column=0)

frame11=tk.Frame(okno, width=30, height=30, background="blue").grid(row=1, column=1)
m11 = tk.Label(okno, text='0').grid(row=1, column=1)

frame12=tk.Frame(okno, width=30, height=30, background="grey").grid(row=1, column=2)
m12 = tk.Label(okno, text='0').grid(row=1, column=2)

frame13=tk.Frame(okno, width=30, height=30, background="blue").grid(row=1, column=3)
m13 = tk.Label(okno, text='0').grid(row=1, column=3)

frame20=tk.Frame(okno, width=30, height=30, background="blue").grid(row=2, column=0)
m20 = tk.Label(okno, text='0').grid(row=2, column=0)

frame21=tk.Frame(okno, width=30, height=30, background="grey").grid(row=2, column=1)
m21 = tk.Label(okno, text='0').grid(row=2, column=1)

frame22=tk.Frame(okno, width=30, height=30, background="blue").grid(row=2, column=2)
m22 = tk.Label(okno, text='0').grid(row=2, column=2)

frame23=tk.Frame(okno, width=30, height=30, background="grey").grid(row=2, column=3)
m23 = tk.Label(okno, text='0').grid(row=2, column=3)

frame30=tk.Frame(okno, width=30, height=30, background="grey").grid(row=3, column=0)
m30 = tk.Label(okno, text='0').grid(row=3, column=0)

frame31=tk.Frame(okno, width=30, height=30, background="blue").grid(row=3, column=1)
m31 = tk.Label(okno, text='0').grid(row=3, column=1)

frame32=tk.Frame(okno, width=30, height=30, background="grey").grid(row=3, column=2)
m32 = tk.Label(okno, text='0').grid(row=3, column=2)

frame33=tk.Frame(okno, width=30, height=30, background="blue").grid(row=3, column=3)
m33 = tk.Label(okno, text='0').grid(row=3, column=3)

gumb_gor=tk.Button(okno, text="gor").grid(row=1, column=6)

gumb_dol=tk.Button(okno, text="dol").grid(row=2, column=6)

gumb_levo=tk.Button(okno, text="levo").grid(row=2, column=5)

gumb_desno=tk.Button(okno, text="desno").grid(row=2, column=7)


