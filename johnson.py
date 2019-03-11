def licz(lista):            # funkcja licząca czas 
    suma = [0] 
    
    for i in range(len(lista)-1):
        suma.insert(i+1, lista[i][0]+suma[i])

    for k in range(len(lista[0])):

        suma[0]=suma[0]+lista[0][k]

        for i in range(len(lista)-1):
            if suma[i] > suma[i+1]:
                suma[i+1]=suma[i]
                
        suma[i+1]=suma[i+1]+lista[i+1][k]

    return suma[len(suma)-1]

def czytaj(plik):               # czyta z pliku 
    f = open(plik, "r" )

    lines = f.read()
    
    for line in lines: 
        x = (lines.split())
        x = list(map(int, x))

    ilosc = x[0]
    masz  = x[1]
    j=2  

    num_lists = x[1]
    lists = [[] for i in range(num_lists)]  
    k = 0
 
    while j < (x[0]*x[1]+2):
            
        for k in range(num_lists):
            
            lists[k].append(x[j])
            j +=1

    f.close()
    return lists, masz, ilosc

def johnson(zad,lista):         # algorytm johnsona
    
    l = [[] for i in range(len(lista))]
    z =  []
    new_list = [[] for i in range(2)]

    dl = len(lista)
    zadania = len(zad)

    if (dl == 3):
        
    
        for i in range(len(lista[0])):
            new_list[0].append(lista[0][i] + lista[1][i])
            new_list[1].append(lista[1][i] + lista[2][i])
        
    elif (dl == 2):   
        new_list = lista
    else:
        print("ERROR")
    
    
    k = 0
    j = 0

    for i in range(zadania):
        
        if (min(new_list[0]) <= min(new_list[1])):
            id = new_list[0].index(min(new_list[0]))
            for q in range(dl):
                
                l[q].insert(k, lista[q][id])
                q = q+1
           
            z.insert(k,zad[id])
            k=k+1

        else:
            id = new_list[1].index(min(new_list[1]))
            for q in range(dl):
                l[q].insert((i - j), lista[q][id]) 
                q = q+1
             
            z.insert((i-j), zad[id])
            
            j=j+1

        for q in range(dl):
            lista[q].pop(id)
            q = q+1
        
        if (dl == 3):
           
            for q in range(len(new_list)):
                new_list[q].pop(id)
                q = q+1

        zad.pop(id)   
        

    return z, l


def losuj(ilosc):           # generuje liczy

    from random import seed, randint

    seed()
    liczby = []
    for i in range(ilosc):
        liczby.append(randint(1,100))               # zakres losowanych liczb
    return liczby

def tekst(z,lista, czas):               # wypisuje tekst

    print ("    Najlepsza kolejnosc zadan   \n")
    print ("Nr zadania:       ", z)
    print ("Maszyna pierwsza: ", lista[0])
    print ("Maszyna druga:    ", lista[1])

    if (len(lista) == 3):
        print("Maszyna trzecia:  ", lista[2])
    
    print("Cmax:", czas)
    
def main():
    
    import os 
       
    skad_czytac = int(input("Podaj skad czytac dane: \n - z pliku wybierz 1 \n - generuj wybierz 2 \n"))
    
    if (skad_czytac == 1):                      # dla pliku
        plik = input("Podaj nazwe pliku: ")

        if (os.path.isfile(plik) == True):

            lista, x, ilosc = czytaj(plik)
            
            zad = list(range(1, ilosc+1))
            
            z, lista = johnson(zad, lista)
            czas = licz(lista)

            tekst(z,lista,czas)                   
                
        else:
            print("Nie ma takiego pliku !")
            

    elif (skad_czytac == 2):                # dla generowanych zadan 
            
        ilosc = int(input("Podaj ile zadan ma sie wykowywac: "))
        ile = int(input("Podaj na ilu maszynach ma maja sie wykonywac zadania (2 lub 3): "))

    
        zad = list(range(1, ilosc+1)) 
        m1 = losuj(ilosc)
        m2 = losuj(ilosc)
        
        lista = [m1,m2]
        
        print ("Nrumery zadan:       ", zad)
        print ("Czasy na maszynie 1: ", m1)
        print ("Czasy na maszynie 2: ", m2)

        if (ile == 3):
            m3 = losuj(ilosc)
            lista = [m1,m2,m3]
            print ("Czasy na maszynie 3: ", m3)
            
            z, lista = johnson(zad, lista) 
            
            czas = licz(lista)


        if (ile != 2 and ile != 3):
            print("Podales zla liczbe maszyn! ")
    

        tekst(z,lista,czas) 
   

main()
