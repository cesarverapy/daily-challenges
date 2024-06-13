def contar_vocales(cadena):
    # se definen las vocales al inicio
    vocales = "aeiouAEIOU"

  # contador de las vocales al inicio
    contador = 0
    
    # recorre cada letra en la cadena
    for letra in cadena:
        # si es una vocal aumenta el contador
        if letra in vocales:
            contador += 1
    
    # imprime 
    print(f"el número de vocales en la cadena es: {contador}")

cadena = input("introduce una cadena de texto: ")
contar_vocales(cadena)
