from enum import Enum
import random

# define una clase para las opciones del juego
class Opcion(Enum):
    PIEDRA = 1
    PAPEL = 2
    TIJERAS = 3

def jugar():
    # enlista todas las opciones disponibles en el Enum.
    opciones = list(Opcion)
    # la máquina elige aleatoriamente una de las opciones del Enum.
    eleccion_computadora = random.choice(opciones)
    # pide al usuario que ingrese su elección.
    eleccion_usuario = input("Elige piedra, papel o tijeras: ").strip().lower()
    # mapeo de las entradas de texto a los valores del Enum.
    mapa = {'piedra': Opcion.PIEDRA, 'papel': Opcion.PAPEL, 'tijeras': Opcion.TIJERAS}
    # conviersor de la elección del usuario de texto a Enum usando el mapa.
    usuario = mapa.get(eleccion_usuario)

    # verifica si la entrada del usuario es válida.
    if usuario:
        print(f"La computadora eligió {eleccion_computadora.name.lower()}")
        # compara la elección del usuario y de la computadora para determinar el resultado.
        if usuario == eleccion_computadora:
            print("Empate")
        elif (usuario == Opcion.PIEDRA and eleccion_computadora == Opcion.TIJERAS) or \
             (usuario == Opcion.PAPEL and eleccion_computadora == Opcion.PIEDRA) or \
             (usuario == Opcion.TIJERAS and eleccion_computadora == Opcion.PAPEL):
            print("¡Ganaste!")
        else:
            print("Ganó la computadora")
    else:
        print("Entrada inválida.")
