maszyna1 = [4,4,10,6,2] #czasy zadania pierwszego
maszyna2 = [6,1,4,10,3] #czasy zad drugiego

zad = [0,1,2,3,4]


def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p
            xs[low], xs[i] = xs[i], xs[low]


#funkcja licząca czas wykonywania wszystkich zadan
def licz():
    suma_masz2 = maszyna1[zad[0]]
    
    suma_masz1 = 0
    for i in zad:
        suma_masz1
        suma_masz1=suma_masz1+maszyna1[i]
        suma_masz2
        if suma_masz1 > suma_masz2:
            suma_masz2=suma_masz1
        suma_masz2=suma_masz2+maszyna2[i]
    return suma_masz2

lista = []
czasy = []
for p in permute(zad):
    for i in permute(zad):
        lista.append(p)
        czasy.append(licz())
     
    
    print("permutacja:",p, " Cmax:", licz())

id = czasy.index(min(czasy))
print("Najmniejszy czas: ", czasy[id], " dla permutacji: ", lista[id] )

