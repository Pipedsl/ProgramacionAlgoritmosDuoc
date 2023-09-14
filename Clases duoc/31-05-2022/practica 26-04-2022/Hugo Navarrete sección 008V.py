guante=3000
comprag=int(input("\n\tIngrese la cantidad de guantes que desea comprar: "))
precio=guante*comprag
if precio>21000:
    print(f"\n\tLa cantidad de guantes son: {comprag}, El precio es: ${precio}, y el envio es gratuito")
elif precio>15000:
    print(f"\n\tLa cantidad de guantes son: {comprag}, El precio es: ${precio}, y el envio tiene un precio de $1000")
    envio=1000
    print(f"\n\tEl precio final es: ${precio} + ${envio} Total: ${precio+envio}\n")
elif precio > 9000:
    print(f"\n\tLa cantidad de guantes son: {comprag}, El precio es: ${precio}, y el envio tiene un precio de $2000")
    envio=2000
    print(f"\n\tEl precio final es: ${precio} + ${envio} Total: ${precio+envio}\n")
else:
    print(f"\n\tLa cantidad de guantes son: {comprag}, El precio es: ${precio}, y el envio tiene un precio de $3000")
    envio=3000
    print(f"\n\tEl precio final es: ${precio} + ${envio} Total: ${precio+envio}\n")