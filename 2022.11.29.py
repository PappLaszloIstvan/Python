import random
"""
a=[]

for i in range(12):
    a.append(random.randint(-20,20))
print(max(a)-min(a))
"""
"""
a=[]

for i in range(10):
    a.append(random.randint(1,100))
print(a)
print(len([x for x in a if x%2==0]))  #A páros számok száma
print(sum([x for x in a if x])) #A lista összege
print(max([x for x in a if x])) #Legnagyobb elem
print(sorted(a)[-2]) #Második legnagyobb elem
"""
"""
osszeg=0
nap=0
while osszeg<=100:
    km=int(input("km: "))
    osszeg+=km
    nap+=1
print("Gratulálok!Elérted a célt!")
print(f"{osszeg-100} km-rel túlteljesítetted a tervet!")
print(f"A túrát {nap} nap alatt teljesítetted!")
"""

"""
#Hány olyan 3 nevű gyerek van
nevek=[]

for i in range(10):
    nevek.append(input("Adj meg egy nevet: "))
print(nevek)
space=0
db=[]
for nev in nevek:
    space=0
    for betu in nev:
        if betu==" ":
            space+=1

    if space==2:
        db.append(nev)
print(len(db))





hossz=[]
for nev in nevek:
    hossz.append(len(nev))
maxhossz=max(hossz)
print(maxhossz)
for nev in range:
    if len(nev)==hossz:
        print(nev)
"""
"""
verseny=[]
print("Adj meg egy nevet és hány km-ig futott")
for i in range(5):
    verseny.append((input(),int(input())))
print(verseny)
print(verseny[1][1])
km=[verseny[0][1]]
for i in range(len(verseny)-1):
    km.append(verseny[i+1][1]-verseny[i][1])
print(km)
maxkm=max(km)
maxii=0
for i in range(len(km)):
    if km[i]==maxkm:
        maxii=i
print(verseny[maxii])
print(maxkm)
"""
import datetime
DATUM=datetime.date.fromisoformat("2022-11-29")
termek=[]
for i in range(5):
    termeknev=input()
    lejar=datetime.date.fromisoformat(input())
    termek.append((termeknev,lejar))
for t, l in termek:
    if l<DATUM:
        print(t)


