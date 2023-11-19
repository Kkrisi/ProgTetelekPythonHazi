
import math



#1-	Számold meg, hogy hány darab 7-tel osztható szám van 1-1000 között!
def Elso():
	szamlalo = 0
	for i in range(1,1000,1):
		if i % 7 == 0:
			szamlalo += 1
	return szamlalo









#2-	Számold meg, hogy hány darab 12-vel osztható szám van 2000-20000 között!
def Masodik():
	szamlalo = 0
	for i in range(2001,20000,1):
		if i % 12 == 0:
			szamlalo += 1
	return szamlalo














#3-	Írd ki az első 20 3-mal osztható szám négyzetének összegét!
def Harmadik():
	osszeg = 0
	i = 0
	while i != 20:
		if i % 3 == 0:
			osszeg += (i*i)
		i += 1
	return osszeg












#4-	Keresd meg egy szám egész osztóit!
def EgeszOsztok():
	szam = int(input("Kérek egy egész számot: "))
	i = 1
	lista = []
	while i <= szam:
		if szam % i == 0:
			lista.append(i)
		i += 1
	return szam,lista






##5-	Keresd meg egy szám legnagyobb egész osztóját!
def LegnagyobbOszto():
	szam = int(input("Kérek egy egész számot: "))
	i = 1
	lista = []
	while i <= szam:
		if szam % i == 0:
			lista.append(i)
		i += 1
	return szam,max(lista)











#6-	Vizsgáljuk meg, hogy egy adott szám prímszám-e!
def PrimSzam():
	szam = int(input("Kérek egy egész számot: "))
	i = 1
	if szam>2 and szam % 2 == 0 or szam>3 and szam % 3 == 0 or szam>5 and szam % 5 == 0 or szam == 1:
		valasz = f"A {szam} szám nem prím"
	else:
		i = 5
		while i * i <= szam:
			if szam % i == 0 or szam % (i + 2) == 0:
				valasz = f"A {szam} szám nem prím"
				break
			i += 6
		valasz = f"A {szam} szám prím"
	return valasz










#7-	Számold meg, hogy hány négyzetszám van 0-100000 között!
def Negyzetszam1():
	szamlalo = 0
	for i in range(1,100001):
		if str(math.sqrt(i))[-2:] == ".0":
			szamlalo += 1
	return szamlalo










#8-	Számold meg, hogy hány négyzetszám van 10000-100000 között!
def Negyzetszam2():
	szamlalo = 0
	for i in range(10001,100001):
		if str(math.sqrt(i))[-2:] == ".0":
			szamlalo += 1
	return szamlalo











#9-	Add össze, hogy mennyi a 0-10000 közötti négyzetszámok összege!
def Negyzetszam3():
	osszeg = 0
	for i in range(1,10001):
		if str(math.sqrt(i))[-2:] == ".0":
			osszeg += math.sqrt(i)
	return osszeg





























































