import random
import string

def generar_pass(longitud):
    character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ''.join(random.choice(character) for i in range(longitud))
    return password

longitud_pass = int(input("Por favor, ingrese la longitud del password: "))  
password_generado = generar_pass(longitud_pass)
print("El Password generado es:", password_generado)
