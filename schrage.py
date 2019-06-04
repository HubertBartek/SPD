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

            
            print(Cmax)
            G.pop(j) 

            for i in range(len(G_rpq)):
                G_rpq[i].pop(j)

    pi = sigma
    
    # for i in range(len(pi)):
    #    pi[i] = pi[i]+1
    
    return pi, Cmax, pi_rpq



plik = "in50.txt"

lista, zad = czytaj(plik)
pi, Cmax, pi_rpq = schrage(lista)
print ("Zad: ",zad)
print ("PI ",pi)
print ("PI RPQ ",pi_rpq)
print("Cmax ", Cmax)
