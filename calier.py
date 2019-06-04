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

def schrage(lista):

    t = min(lista[0])

    G = []
    G_rpq = [[] for i in range(len(lista))]
    pi_rpq = [[] for i in range(len(lista))]
    sigma = []
    Cmax = 0
    N = list(range(0, len(lista[0])))
      
    while G or N:
        while N and lista[0] and lista[1] and lista[2] and min(lista[0]) <= t :
              
            j = lista[0].index(min(lista[0]))

            G.append(N[j])

            for k in range(len(G_rpq)):           # uzupelnia ostatnie miejsca list czasu zerami 
                G_rpq[k].append(lista[k][j])
           
            N.pop(j)
            for i in range(len(lista)):
                lista[i].pop(j)

        if not G:
            t=min(lista[0])
            
        else:
            j=G_rpq[2].index(max(G_rpq[2]))   
            sigma.append(G[j]) 
            
            for k in range(len(pi_rpq)):          
                pi_rpq[k].append(G_rpq[k][j])
               
            t=t+G_rpq[1][j]
           
            Cmax = max(Cmax, t+G_rpq[2][j])
            G.pop(j) 

            for i in range(len(G_rpq)):
                G_rpq[i].pop(j)
           
    return Cmax, pi_rpq

def schrage_przerwania(lista):

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
    N = list(range(0, len(lista[0])))
      
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

def wyz_b(lista, Cmax_schrage):
    czas = []
    b_q = []
    t_czas = lista[0][0]+lista[1][0]
    k = 1
    while k != len(lista[0]):
        if lista[0][k] > t_czas:
            t_czas = lista[0][k]
        t_czas = t_czas+lista[1][k]

        Cmax = t_czas +lista[2][k]
        if Cmax_schrage == Cmax:
            czas.append(k)
            b_q.append(lista[2][k])
        k+=1
    return czas[-1], b_q[-1]

def wyz_a(lista, Cmax_schrage, b):

    qp = lista[1][b]+lista[2][b]
    suma = 0
    
    for k in range(b+1):
        z = k
        for y in range(b-k):
            
            suma += lista[1][z]
            
            z +=1
        
        Cmax = lista[0][k]+suma+qp
        suma = 0
        if Cmax_schrage == Cmax:
            return k
   


def wyz_c (lista, b, a, b_q):
    c = []
    x=a
    while x != b:
        if lista[2][x] < b_q:
            c.append(x)
        x +=1
        
    if c:
        return c[-1]
    else:
        return -1

def licz_abc1(zadania):
    cmax,kol = schrage(zadania)
    b, b_q = wyz_b (kol, cmax)
    a = wyz_a (kol, cmax, b)
    c = wyz_c (kol, b, a, b_q)

    return b, c, kol, cmax


def Carlier(lista, UB):
    b, c, kol, U = licz_abc1(lista)
    tab = copy.deepcopy(kol)
    # print("czas: ",U)
    tab[0].insert(0,UB)
    
    K_p = 0

    if U < UB:
        UB = U
        kolejnosc = copy.deepcopy(kol)
        # print (kolejnosc)

    if c == -1:
        print("nie ma c")
        return kolejnosc

    K_r = min(kol[0][c+1:b+1])
    K_q = min(kol[2][c+1:b+1])
    
    for i in range(c+1,b+1):
        K_p = K_p + kol[1][i]
    
    rpic = kol[0][c]
    kol[0][c] = max(kol[0][c], K_r + K_p)

    K_p_c = 0
    K_r_c = min(kol[0][c:b+1])
    K_q_c = min(kol[2][c:b+1])
    
    for i in range(c,b+1):
        K_p_c = K_p_c + kol[1][i]
    
    tab_schrage = copy.deepcopy(kol)
    LB = schrage_przerwania(tab_schrage)
    h_k = K_r + K_q + K_p 
    h_k_c = K_r_c + K_q_c + K_p_c 
    LB = max(h_k, LB, h_k_c)

    if LB < UB:
        tab2 = Carlier(kol,LB)
        UB = tab2[0][0]
        tab2[0].pop(0)
        kol = copy.deepcopy(tab2)


    kol[0][c] = rpic

    qpic = kol[2][c]
    kol[2][c] = max(kol[2][c], K_q + K_p)

    tab_schrage = copy.deepcopy(kol)

    LB = schrage_przerwania(tab_schrage)
    h_k = K_r + K_q + K_p 
    h_k_c = K_r_c + K_q_c + K_p_c 
    LB = max(h_k, LB, h_k_c)

    tab = copy.deepcopy(kol)
    tab.insert(0,UB)

    if LB < UB:
        #print('cz3')
        tab3 = Carlier(kol,LB)
        UB = tab3[0][0]
        tab3[0].pop(0)
        kol = copy.deepcopy(tab3)
    
    kol[2][c] = qpic

    tab = copy.deepcopy(kol)
    tab[0].insert(0,LB)
    print('cmax ost',LB)

    return tab

plik = "in50.txt"
lista, zad = czytaj(plik)
ub = 99999999999999999999999999999999
Carlier(lista,ub)
