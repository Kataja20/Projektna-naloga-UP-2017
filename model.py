import math

def sestevanje(x, y):
    return x + y

def odstevanje(x, y):
    return x - y

def mnozenje(x, y):
    return x * y

def deljenje(x, y):
    if y == 0:
        return 'Error'
    else:
        return x / y

def pi():
    return math.pi 

def euler():
    return math.exp(1)

def fakulteta(x):
    if x < 0:
        return 'Error'
    elif x == 0:
        return 1
    elif x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return x * fakulteta(x-1)
