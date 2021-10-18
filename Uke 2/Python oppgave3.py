tall1=14
Tall2=7
Tall3=11

if tall1>Tall2:
    print("tall1 er størst")
elif tall1<Tall2:
    print("tall2 er størst")


num_list=[tall1,Tall2,Tall3]
num_list.sort(key=int)
print("tallet som er størst er:", num_list[2])