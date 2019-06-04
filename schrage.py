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

def schrage(lista):


    t = min(lista[0])

    G = []
    G_rpq = [[] for i in range(len(lista))]
    pi=[]
    pi_rpq = [[] for i in range(len(lista))]
    sigma = []
    Cmax = 0
    N = list(range(0, lista[0]))
      
    while G or N:
        while N and lista[0] and lista[1] and lista[2] and min(lista[0]) <= t :
              
            j = lista[0].index(min(lista[0]))

            G.append(N[j])

            for k in range(len(G_rpq)):           # uzupelnia ostatnie miejsca list czasu zerami 
                G_rpq[k].append(lista[k][j])

            # G_r.append(r[j])
            # G_p.append(p[j])
            # G_q.append(q[j])
            
            N.pop(j)
            for i in range(len(lista)):
                lista[i].pop(j)
            # r.pop(j)
            # p.pop(j)
            # q.pop(j)

        if not G:
            t=min(lista[0])
            
        else:
            j=G_rpq[2].index(max(G_rpq[2]))   
            sigma.append(G[j]) 
            
            for k in range(len(pi_rpq)):          
                pi_rpq[k].append(G_rpq[k][j])
               
            # pi_r.append(G_r[j])
            # pi_q.append(G_q[j])
            # pi_p.append(G_p[j])

            t=t+G_rpq[1][j]
           
            Cmax = max(Cmax, t+G_rpq[2][j])

            
            print(Cmax)
            G.pop(j) 

            for i in range(len(G_rpq)):
                G_rpq[i].pop(j)
            # G_r.pop(j)
            # G_p.pop(j)
            # G_q.pop(j)
            
    pi = sigma
    
    # for i in range(len(pi)):
    #    pi[i] = pi[i]+1
    
    return pi, Cmax, pi_rpq


def wyz_b(pi, lista, Cmax_schrage):
    czas = []
    print("Cmax z calier: ", Cmax_schrage)
    print("LISTA Z B: ", lista)
    b_q = []
    t = lista[0][0]+lista[1][0]
    k = 1
    while k != len(pi):
    # for i in range(len(pi)):
        print("Czas z b 1111: ", lista[0][k], t)
        if lista[0][k] > t:
            t = lista[0][k]
            print("Czas z petli: ", t)
        t = t+lista[1][k]
        Cmax = t +lista[2][k]
        print("Cmax z wyznacz b: ",k,  Cmax)
        if Cmax_schrage == Cmax:
            czas.append(k)
            b_q.append(lista[2][k])
        k+=1
    return czas[-1], b_q[-1]

def wyz_a(pi, lista, Cmax_schrage, b):

    qp = lista[1][b]+lista[2][b]
    print("QP: ", qp)
    suma = 0
    
    for k in range(b+1):
        z = k
        print("ZZZ: ",z)
        for y in range(b-k):
            
            suma += lista[1][z]
            
            z +=1
        
        Cmax = lista[0][k]+suma+qp
        print("Cmax a: ",Cmax)
        print("SUMA: ", suma)
        suma = 0
        print("KKK: ", k)
        if Cmax_schrage == Cmax:
            return k
   


def wyz_c (lista, b, a, b_q):
    print("A_A_A_A: ",a)
    print("B_B: ", b)
    c = []
    x=a
    while x != b:
        if lista[2][x] < b_q:
            c.append(x)
        x +=1
    if c:
        return c[-1]
    else:
        return False

def tab_k (c, b, pi, pi_rpq):

    K_rpq = [[] for i in range(3)]
    K = []
    x = c
    for i in range(b-c):
    # x = pi.index(c)
    # for i in range(pi.index(b)-pi.index(c)):
        K.append(pi[x+1])
        for z in range(len(pi_rpq)):
            K_rpq[z].append(pi_rpq[z][x+1])

        x+=1
    print ("tab k: ",K)
    K_r = min(K_rpq[0])
    K_q = min(K_rpq[2])

    suma = 0
    for y in range(len(K_rpq[1])):
            
        suma += K_rpq[1][y]
            
    K_p = suma
    print("tab krpq: ",K_rpq)

    stare_r = pi_rpq[0][c]
    print ("Stare r ", stare_r)
    pi_rpq[0][c] = max(pi_rpq[0][c], K_r+K_p)
    print ("nowe r ", pi_rpq[0][c])

    return K_r, K_q, K_p

plik = "in50.txt"
lista =[[0, 25, 31, 27, 207, 158, 297, 353, 357, 411, 453, 580, 623, 639, 657, 737, 631, 784, 704, 918, 967, 1009, 1290, 1227, 1170, 1132, 1086, 1166, 1447, 1387, 980,
895, 1609, 1646, 969, 1676, 1726, 1771, 1722, 1725, 1805, 1772, 1889, 928, 1708, 1215, 875, 1333, 1723, 1098], [26, 26, 97, 63, 51, 55, 64, 18, 84, 25, 38, 26, 26, 67, 31, 34, 35, 49, 66, 66, 98, 64, 82, 63, 49, 9, 8, 88, 47, 18, 60, 56, 8, 10, 59, 16, 46, 19, 37, 27, 3, 93, 68, 14, 44, 98, 81, 48, 14, 64], [426, 822, 1032, 1023, 1893, 360, 90, 1238, 585, 1760, 263, 1219, 77, 1329, 1441, 1476, 1278, 946, 875, 1468, 1713, 1595, 1148, 1730, 1362, 1027, 746, 574, 1442, 853, 448, 413, 1290, 612, 412, 326, 1254, 1196,
803, 738, 695, 407, 742, 282, 245, 228, 214, 156, 115, 6]]
zad = 50
# lista, zad = czytaj(plik)
pi, Cmax, pi_rpq = schrage(lista)
print ("Zad: ",zad)
print ("PI ",pi)
print ("PI RPQ ",pi_rpq)
print("Cmax ", Cmax)

b, b_q = wyz_b (pi, pi_rpq, Cmax)
a = wyz_a (pi, pi_rpq, Cmax, b)
print("b ", b)
print("b_q ", b_q)
print("a ", a)
c = wyz_c (pi_rpq, b, a, b_q)

Kr, Kq, Kp = tab_k(c, b, pi, pi_rpq)


print("b ", b)
print("b_q ", b_q)
print("a ", a)
print("c ", c)
print("Kr: ",Kr)
print("Kq: ",Kq)
print("Kp: ",Kp)

