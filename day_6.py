def conversor(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# pide al usuario que ingrese la temperatura en grados celsius
celsius = float(input("ingrese la temperatura en grados celsius: "))

# convierte la temperatura a fahrenheit
fahrenheit = conversor(celsius)

# imprime el resultado
print(f"{celsius} grados celsius son {fahrenheit} grados fahrenheit.")
