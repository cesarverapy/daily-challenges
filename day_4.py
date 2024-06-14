def ordenar_lista():
    # solicita al usuario que ingrese una lista de numeros
    entrada_usuario = input("ingrese una lista de números")
    
    # convierte cadena en una lista de numeros
    lista_numeros = [int(numero) for numero in entrada_usuario.split(',')]
    
    # ordena la lista en orden ascendente
    lista_numeros.sort()
    
    # imprime lista ordenada
    print("lista ordenada en orden ascendente:", lista_numeros)

# llama a la función
ordenar_lista()
