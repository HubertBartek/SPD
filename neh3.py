import datetime
start = datetime.datetime.now()

# lista = [[4,4,1,5],[1,3,2,1],[4,3,3,3]]

# ilosc = 4
# zad = list(range(1, ilosc+1))


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


def licz(lista, zadanie):       # liczy od gory do dołu tak jak na schemacie 

    lista_czasu = [[] for i in range(len(lista))]

    for k in range(len(lista_czasu)):           # uzupelnia pierwsze miejsca list czasu zerami 
        lista_czasu[k].append(0)

    for j in range(1,len(zadanie)+1):       # dla pierwszej listy sumuje wszystki wartosci 
        lista_czasu[0].append(lista_czasu[0][j-1] + lista[0][zadanie[j-1]])
   
    for i in range(1, len(lista)):      # dla kolejnych list sprawdza ktora wartosc jest wieksza i dodaje wartosc z listy
        for j in range(1, len(zadanie)+1):
            lista_czasu[i].append(max(lista_czasu[i-1][j], lista_czasu[i][j-1]) + lista[i][zadanie[j-1]])


    return lista_czasu # zwraca uzyskany czas

def licz2 (lista, zadanie):     #liczy od dolu do gory

    lista_czasu = [[] for i in range(len(lista))]

    for k in range(len(lista_czasu)):           # uzupelnia ostatnie miejsca list czasu zerami 
        lista_czasu[k].append(0)

    for j in range(1,len(zadanie)+1):        # dla ostatniej listy sumuje wszystki wartosci 
        lista_czasu[-1].insert(0, lista_czasu[-1][-j] + lista[-1][zadanie[-j]])

    for i in range(2, len(lista)+1):      # dla kolejnych list sprawdza ktora wartosc jest wieksza i dodaje wartosc z listy
        for j in range(2, len(zadanie)+2):
            lista_czasu[-i].insert(0, max(lista_czasu[-i+1][-j], lista_czasu[-i][-j+1]) + lista[-i][zadanie[-j+1]])
    
    return lista_czasu

def licz_konce(lista, zadanie, lista_czasu, l):     # liczy czas dla nowej tablicy czasu (tylko dwa elementy)
    
    
    lista_czasu[0].append(lista_czasu[0][-1] + lista[0][zadanie[l]])
    
    for i in range(1,len(lista)):
        lista_czasu[i].append(max(lista_czasu[i-1][-1], lista_czasu[i][-1]) + lista[i][zadanie[l]])

    return lista_czasu
    

def suma(index, lista):     # sumuje kolumne
    sum_p = 0
    for i in range(len(lista)):
        sum_p += lista[i][index]
    return sum_p

def sortowanie(lista):      # sortuje rosnaco utworzona liste zadan z wartsciami od 0 do ilosci zadan
    new_lista = []              # wedlug sumy 
    for j in range(len(lista[0])):      # tak jakby posortowane indexy 
        new_lista.append(j)
    
    return sorted(new_lista, key=lambda index: suma(index, lista), reverse=True)


def neh(lista):

    zad_sort = sortowanie(lista)
       
    zadanie = []
    zadanie.append(zad_sort[0])

    war = []  
    lista_czasu1 = [[] for i in range(len(lista))]
    lista_czasu2 = [[] for i in range(len(lista))]
    lista_czasu1_new = [[] for i in range(len(lista))]
    lista_wartosci = []
    
     
    k=1
    l=0
  
    
    for a in range(len(zadanie)+1):
        zadanie.insert(l, zad_sort[k])

        lista_czasu = licz(lista, zadanie)
        war.append(lista_czasu[-1][-1])

        zadanie.pop(l)
        l+=1

    for b in range(len(war)):
        if (min(war) == war[b]):
            zadanie.insert(b,zad_sort[k])
            break
            
    mini = min(war)
    war.clear()
    k= k+1
    l = 0

   
    lista_czasu1 = licz(lista, zadanie)
    lista_czasu2 = licz2(lista, zadanie)

    for c in range(len(zad_sort)-2):

        for a in range(len(zadanie)+1):
            zadanie.insert(l, zad_sort[k])


            for i in range(len(lista_czasu1)):
                lista_czasu1_new[i].append(lista_czasu1[i][l])
     
            cmax = licz_konce(lista, zadanie, lista_czasu1_new, l)

            for x in range(len(lista_czasu1)):
                lista_wartosci.append(cmax[x][-1]+lista_czasu2[x][l])

            war.append(max(lista_wartosci))

            for i in range(len(lista_czasu1_new)):

                lista_czasu1_new[i].clear()

            zadanie.pop(l)
            lista_wartosci.clear()
            l+=1
    
        for b in range(len(war)):
            if (min(war) == war[b]):
                zadanie.insert(b,zad_sort[k])
                break
        
        
        mini = min(war)
        war.clear()
        k= k+1
        l = 0
        
        for i in range(len(lista_czasu1)):

            lista_czasu1[i].clear()
            lista_czasu2[i].clear()

        lista_czasu1 = licz(lista, zadanie)
        lista_czasu2 = licz2(lista, zadanie)

        
    for i in range(len(zadanie)):
        zadanie[i] = zadanie[i]+1

    return zadanie, mini



lista, ilosc = czytaj("test.txt")


z, w = neh(lista)

duration = datetime.datetime.now() - start

print("zadania: ",z)
print("czas: ", w)


print("Czas wykonania programu: ",duration)