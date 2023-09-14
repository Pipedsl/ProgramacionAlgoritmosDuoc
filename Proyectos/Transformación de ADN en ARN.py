#Convertidor ADN a ARN
sequences = "tatgctttcc#tataggtctg#ctattcaatg" #ADN
lista_adn = sequences.split("#") #Separador #
print(lista_adn) 

for adn in lista_adn:
    arn = adn.replace("t","u") #reemplazo t (Timina) por u (Uracil)
    print(f"ADN: {adn} -> ARN: {arn}")