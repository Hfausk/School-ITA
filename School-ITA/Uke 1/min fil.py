import random


def addere():

    Tall1= int (input("skriv tall 1"))
    Tall2= int (input("skriv tall 2"))

    summen= Tall1+Tall2

    print("summen av tallene = " +str (summen))

def multiplisere():
    svar1 = int(input("skriv tall 1:"))
    svar2 = int(input("skriv tall 2:"))

    sum= svar1*svar2

    print("produktet av de 2 tallene = "+ str (sum))

def terningkast():
    terning1= 0
    terning2= 0
    terningTotal = 0

    while terningTotal!=12:
        input("trykk for å kaste")
        terning1 = random.randint(1,6)
        terning2 = random.randint(1,6)
        terningTotal = terning1+terning2
        print("Du fikk ",terningTotal)

def telling():
    for i in range(70):
        print(i)
        if i ==35:
            print("du er halvveis")
        if i%7==0:    
            print("*")

frukt=["Eple","Pære","citron","melon"]

frukt.append("plomme")
nfrukt=input("skriv frukt: ")
frukt.append(nfrukt)

print(frukt)






print("velg hva du vil gjøre: \n1. addere: \n2. muliplisere \n3. terning \n4. Telling til 70 ")
svar= int (input("hva vil du gjøre?"))

if svar ==1:
    addere()
elif svar ==2:
    multiplisere()
elif svar==3:
    terningkast()
elif svar==4:
    telling()

