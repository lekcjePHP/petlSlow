


janekData = {"francuzki": [1,2,3,4,4,5], "przedmioty":["polski", "matematyka", "historia", "francuzki"], "waga":70}
krychaData = {"niemiecki": [5,2,1,2,4,5], "przedmioty":["polski", "matematyka", "historia", "niemiecki"], "waga":55}
zenobiuszData = {"niemiecki": [5,2,1,2,4,5], "przedmioty":["polski", "matematyka", "historia", "niemiecki"], "waga":60}
krzychoData = {"koreanski": [5,2,1,2,4,5], "przedmioty":["polski", "matematyka", "historia", "koreanski"], "waga":65}
rychoData = {"suahili": [5,2,1,2,4,5], "historia":[5,2,3,4,6,2,1], "przedmioty":["polski", "matematyka", "historia", "suahili"], "waga":80}


slownik = {"janek": janekData, "krycha":krychaData, "zenobiusz":zenobiuszData, "krzycho":krzychoData, "rycho":rychoData}

"""
suma = 0

for ocena in slownik["zenobiusz"]["niemiecki"]:
	suma = suma + ocena
	#print(ocena)

liczbaOcen = len(slownik["zenobiusz"]["niemiecki"])

print(suma/liczbaOcen)
"""

def liczSrednia(imie, przedmiot):
	suma = 0
	for ocena in slownik[imie][przedmiot]:
		suma = suma + ocena
	liczbaOcen = len(slownik[imie][przedmiot])	
	print(suma/liczbaOcen)

liczSrednia("rycho", "historia")
liczSrednia("janek", "francuzki")
liczSrednia("krzycho", "koreanski")
#print(slownik["zenobiusz"]["niemiecki"])