def validInsee(insee, cle):
    # http://fr.wikipedia.org/wiki/Numero_de_Securite_sociale#Unicit.C3.A9
    # gestion numeros corses
    insee = insee.replace('A', 0)
    insee = insee.replace('B', 0)
    reste = int(insee) % 97
    return ((97 - reste) == int(cle))

