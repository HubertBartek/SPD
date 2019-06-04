import copy 

def czytaj(plik):               # czyta z pliku 
    f = open(plik, "r" )

    lines = f.readline()
    
    x = (lines.split())
    x = list(map(int, x))
    
    zad = x[0]
    maszyny = x[1]
   
    lista = [[] for i in range(maszyny)] 

    for i in range(zad):
        lista_i = f.readline().split()
        for j in range(maszyny):
            lista[j].append(int(lista_i[j]))
    f.close()
    return lista, zad 

def schrage_przerwania(lista, ilosc):

    r = lista[0]
    p = lista[1]
    q = lista[2]

    t = min(lista[0])
    l = 0
    l_q = 9999999999999999999999999999999999999
    G = []
    G_r = []
    G_p = []
    G_q = []

    Cmax = 0
    N = list(range(0, ilosc))
      
    while G or N:
        while N and r and q and p and min(r) <= t :
              
            j = r.index(min(r))

            G.append(N[j])
            G_r.append(r[j])
            G_p.append(p[j])
            G_q.append(q[j])
            
            N.pop(j)

            if q[j] > l_q:
                l_p = t - r[j]
                t = r[j]

                if l_p > 0:
                    G.append(l)
                    G_r.append(l_r)
                    G_p.append(l_p)
                    G_q.append(l_q)
            
            r.pop(j)
            p.pop(j)
            q.pop(j)
            
        if not G:
            t=min(r)
            
        else:
            j=G_q.index(max(G_q))   
               
            t = t + G_p[j]
            l = j
            l_r = G_r[j]
            l_p = G_p[j]
            l_q = G_q[j]

            
            Cmax = max(Cmax, t+G_q[j])
            G.pop(j) 
            G_r.pop(j)
            G_p.pop(j)
            G_q.pop(j)
            
    
    return Cmax

plik = "in200.txt"

lista, zad = czytaj(plik)
Cmax = schrage_przerwania(lista, zad)
 
print ("Zad: ",zad)

print("Cmax ", Cmax)
