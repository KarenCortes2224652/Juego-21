#Input
import random

#Processing
jugador=random.randint(1,10)
pc=random.randint(1,10)
dan=0
sum=0
i=1
diferencia=dan-sum
while i<= 2:
    sum=sum+jugador
    dan=dan+pc
    i=i+1
print("pc",dan)
print("Jugador",sum)
print("¿Quieres seguir jugando?")
X=int(input("1.Para seguir jugando o 2.Para parar: "))
if X==1: 
    #Sum = es igual a la variable de suma del computador
    while sum<=21 and X!=2:
        d= random.randint(1,10)  
        sum =sum +d 
        print("Jugador",sum)
        if sum>21:
            print("Perdiste")
            break
        print("¿Quieres seguir jugando?")
        X=int(input("1.Para seguir jugando o 2.Para parar: "))
        if sum>21:
            print("Perdiste")
            break
        elif X==2:
            while dan <=sum and dan < 21:
                p=random.randint(1,10)
                dan = dan + p
                print("pc", dan)
            if dan>sum and dan<21:
                if diferencia==1:
                    print("El computador gana por un punto")
                else:
                    print("Gana el computador por" , dan-sum, "Puntos")
            elif dan==sum:
                print("Gana el pc por ser el tallador")
            if dan>21:
                print("El computador perdió")

elif X==2:
    while dan <=sum and dan < 21:
        p=random.randint(1,10)
        dan = dan + p
        print("pc", dan)
    if dan>sum and dan<21:
        if diferencia==1:
            print("El computador gana por un punto")
        else:
            print("Gana el computador por" , dan-sum, "Puntos")
    elif dan==sum:
        print("Gana el pc por ser el tallador")
    if dan>21:
        print("El computador perdió")