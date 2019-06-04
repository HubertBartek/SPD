import math
from random import random, randint, sample


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
    return lista, zad, maszyny

def licz(lista, zadanie):       # liczy od gory do dołu tak jak na schemacie 

    lista_czasu = [[] for i in range(len(lista))]

    for k in range(len(lista_czasu)):           # uzupelnia pierwsze miejsca list czasu zerami 
        lista_czasu[k].append(0)

    for j in range(1,len(zadanie)+1):       # dla pierwszej listy sumuje wszystki wartosci 
        lista_czasu[0].append(lista_czasu[0][j-1] + lista[0][zadanie[j-1]])
   
    for i in range(1, len(lista)):      # dla kolejnych list sprawdza ktora wartosc jest wieksza i dodaje wartosc z listy
        for j in range(1, len(zadanie)+1):
            lista_czasu[i].append(max(lista_czasu[i-1][j], lista_czasu[i][j-1]) + lista[i][zadanie[j-1]])


    return lista_czasu[-1][-1] # zwraca uzyskany czas

def zamiana (zad, ilosc, typ):           # zamienia zadania w liscie zadan

    i = randint(0,ilosc-1)              # losowa cyfra z zakresu 0 - ilosc-1
    j = randint(0,ilosc-1)              # losowa cyfra z zakresu 0 - ilosc-1

    while(i == j):                  # jezeli cyfry sa takie same ponownie losuje
        i = randint(0,ilosc-1)
        j = randint(0,ilosc-1)
    
    if (typ == 'i'):            # insert - wstawianie w wybrane miejsca
        
        if (j < i):        
            zad.insert(j,zad[i])
            zad.pop(i+1)
        else:  
            zad.insert(j+1,zad[i])
            zad.pop(i)
    elif (typ == 's'):          # swap - zamiana wylosowanych miejsc 

        zad[i], zad[j] = zad[j], zad[i] 

    return zad


def symulowane (lista, zad, ilosc, T, Tk, typ):
    i = 0
    l_czasu = []
    To = T
    while (To > Tk):            # liczy ile jest iteracji
        i +=1
        To = 0.9*To            # 0.85 wspołczynnik temperatury
    
    while (T > Tk):     # dopóki temperaturaa nie spadnie poniżej tk
        

        cmax1  = licz(lista, zad)       # liczy czas dla listy zadan 
        
        zad1 = zad
        zad = zamiana(zad, ilosc, typ)       # zamienia losowe indeksy

        cmax2 = licz(lista, zad)        # liczy czas dla zmodyfikowanej listy zadan
        
        # while (cmax1 == cmax2):         # jezeli cmax1 = cmax2 zamien zadania i policz cmax2 na nowo
        #     zad = zamiana(zad, ilosc, typ)      
        #     cmax2 = licz(lista, zad)        
        
        zad2 = zad

        delta = cmax2 - cmax1           # rożnica policzonych czasów


        if ( delta < 0):                # jesli czas1 > czas2 ( drugie rozwiazanie lepsze od pierwszego)
            cmax1 = cmax2               # przepisuje czas drugi
            zad_zad = zad2
        else:                           
            x = random()                # losowa liczba z przedziału <0,1>
            P = math.exp(-delta/T)       # funkcja prawdopodobieństwa

            if (x <= P):                # jezeli losowa licba < prawdopodobienstwo 
                cmax1 = cmax2           # przyjmuje gorszy czas
                zad_zad = zad2
            else:
                zad_zad=zad1
# =========== Bez prawdopodobienstwa ======= 
 
         
        # x = random()                # losowa liczba z przedziału <0,1>
        # if  ( delta < 0): 
        #     P = math.exp(-delta/T)       # funkcja prawdopodobieństwa
        # else:
        #     P = math.exp(delta/T)
        # if (x <= P):                # jezeli losowa licba < prawdopodobienstwo 
        #     cmax1 = cmax2           # przyjmuje gorszy czas
        #     zad_zad = zad2
        # else:
        #     zad_zad=zad1
                
        T = 0.9*T                      # zmniejszenie temperatury
        l_czasu.append(cmax1)
    ilosc_iteracji = i
    mini = min(l_czasu)
    #print ("Najlepszy czas: ", mini)   
    #print ("Ilosc iteracji: ", ilosc_iteracji)
    return zad_zad, cmax1, mini, ilosc_iteracji        # zwraca czas i liste zadan 

def main():

    lista, ilosc, maszyny = czytaj("text.txt")       # wczytuje liste z pliku 

    T = 100000      # ustawienie temperatury poczatkowej 
    Tk = 0.001       # ustawienie temperatury koncowej 
    
    ile_wywolan = int(input("Ile razy wywolac program: "))      # liczba wywolan 
    forma = int(input("Podaj forme pierwszego rozwiazania: \n 1 - losowe  \n 2 - po koleii \n"))        # forma pierwszego rozwiazania 
    typ_zamiany = input("Podaj typ zamiany: \n s - swap  \n i - insert \n")         # swap czy insert 

    if (forma == 1):
        zad = sample(range(0, ilosc), ilosc)            # losuje liczby bez powtorzen
    elif (forma == 2):
        zad = list(range(0, ilosc))                 # generuje liczby od 0 do ...
    else:
        zad = [17, 4, 1, 16, 2, 5, 11, 8, 14, 9, 19, 12, 7, 13, 18, 10, 3, 6, 0, 15]     # wklejam na sztywno rozwiazanie z neha tylko lista zadan
                                                                                            # musi zazynac sie od 0 a nie od 1 

    if (typ_zamiany == 's'):                # swap
        typ = 's'
    elif (typ_zamiany == 'i'):          # insert
        typ = 'i'
    else:
        print("Niepoprawny typ zamiany !")
    
    plik  = open("wynik.txt", "a+" )            # tworzy plik w ktorym zapisuje wyniki 
    suma = []
    l_czasu = []
    for i in range(0, ile_wywolan):             # ile razy ma sie wywołac program 

        zad, cmax, mini, ilosc_iteracji  = symulowane(lista, zad, ilosc, T, Tk, typ)

        print("zadania: ",zad)
        print("czas: ", cmax)
        
        l_czasu.append(cmax)
        suma.append(cmax)
        tekst = "T.k = 0.0001:" 
        rozmiar_macierzy = str(ilosc) + ' x ' + str(maszyny)
        #plik.write( str(tekst) + str(i+1) + " - " + str(rozmiar_macierzy) + " Czas: " + str(cmax) + "\n")     # zapis do pliku
        
        
    srednia = sum(suma)/ile_wywolan


    min_mini = min(l_czasu)
    
    plik.write( str(tekst) + str(i+1) + " - " + str(rozmiar_macierzy) + "\nCzas średni: " + str(srednia) + "\nCzas najlepszy (z cmax):" + str(min_mini) +"\nCzas najmniejszy: " + str(mini) + "\n" )
    plik.write("Ilość iteracji:" + str(ilosc_iteracji) + "\n=========================================\n\n")
    plik.close()


main()
