def crear_diccionario(claves, valores):
    # crear un diccionario
    diccionario = {}

    # obtener la longitud mínima entre las dos lista para evitar errores de índice fuera de rango
    longitud_minima = min(len(claves), len(valores))

    # se iteran los indices hasta conseguir la longitud minima
    for i in range(longitud_minima):
        # obtener clave actual
        clave_actual = claves[i]

        # obtener el valor actual
        valor_actual = valores[i]

        # asigna clave y valor al diccionario
        diccionario[clave_actual] = valor_actual


    # devuelve el diccionario
    return diccionario

claves = ['nombre', 'edad', 'ciudad']
valores = ['cesar', 19, 'rambouillet']
mi_diccionario = crear_diccionario(claves, valores)

# imprime el diccionario
print(mi_diccionario)
