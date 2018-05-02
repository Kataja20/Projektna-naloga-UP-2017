import math

## OSNOVNE FUNKCIJE ############################################################

def sestevanje(x, y):
    return x + y

def odstevanje(x, y):
    return x - y

def mnozenje(x, y):
    return x * y

def deljenje(x, y):
    if y == 0:
        return print('Error')
    else:
        return x / y

## ŠTEVILO PI IN e #############################################################

def pi():
    return math.pi 

def euler():
    return math.exp(1)

## FAKULTETA ###################################################################

def fakulteta(x):
    if x < 0:
        return print('Error')
    elif x == 0:
        return 1
    elif x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return x * fakulteta(x-1)

## DISKRETNA MATEMATIKA ########################################################

def nPr(n, r):
    if n <= 0 or r <= 0 or n < r:
        return print('Error')
    else:
        return fakulteta(n) / fakulteta(n - r)

def nCr(n, r):
    if n <= 0 or r <= 0 or n < r:
        return print('Error')
    else:
        return fakulteta(n) / (fakulteta(r) * fakulteta (n - r))

## POTENCE #####################################################################

def kvadrat(x):
    return x ** 2

def kub(x):
    return x ** 3

def obratna_vrednost(x):
    return x ** (-1)

def potenca(x, n):
    return x ** n

## KORENI ######################################################################

def kvadratni_koren(x):
    return math.sqrt(x)

def kubicni_koren(x):
    return x ** (1 / 3)

def koren(x, n):
    if n == 0:
        return print('Error')
    else:
        return x ** (1 / n)

## LOGARITMI ###################################################################

def logaritem_10(x):
    return math.log10(x)

def logaritem_e(x):
    return math.log(x)

def logaritem(x, a):
    return math.log(x, a)

















    
