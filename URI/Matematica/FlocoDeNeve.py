from math import sqrt

while True:
    try:
        A = float(input())
        Area_do_floco = (2*sqrt(3) * pow(A,2)) / 5 
        print("%.2f" % Area_do_floco)
    except EOFError:
        break