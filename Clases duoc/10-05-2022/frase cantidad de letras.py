#saber cantidad de letras en una frase con while
from stat import FILE_ATTRIBUTE_REPARSE_POINT


frase= input("Introduce una frase: ")
letra= input("Ingrese una letra: ")
contador = 0
for i in frase:
    if i == letra:
        contador+=1
print(f"la letra {letra} aparece {str(contador)} veces en la frase {frase}")