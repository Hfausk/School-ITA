a=[1,1,2,3,5,8,13,21,34,55,89]
print(a)
NumL= len(a)

tallListe=int(a)
TallOver5= tallListe>5
a.append(TallOver5)
print(a)

for i in range(NumL):
    if a[i]<=5:
        print("Tall mindre enn 5=",a[i])

for i in range(NumL):
    if a[i]%2==0:
        print("Tall som er partall=",a[i])


for i in range(NumL):
    if a[i]>5:
        print("Tall som er Større en 5=",a[i])


