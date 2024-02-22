lista = ["ciao","cane","s","gatto", "paperino"]
lista2= []

for element in lista:
    lista2.append(len(element))

primo = lista2[0]
contatore = 1
while (contatore < len(lista2)):
    if (primo == lista2[contatore]):
        print ("Elemento uguale trovato")
        break
    contatore=contatore+1
