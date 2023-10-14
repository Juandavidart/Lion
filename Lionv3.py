import random
import string
import secrets

def generar_contraseña_avanzada(longitud, nivel_de_complejidad="fuerte"):
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    especiales = string.punctuation

    niveles = {
        "debil": (mayusculas + minusculas, 10),
        "fuerte": (mayusculas + minusculas + numeros + especiales, 30),
        "cifrado": (mayusculas + minusculas + numeros + especiales, 30)
    }

    if nivel_de_complejidad not in niveles:
        raise ValueError("Nivel de complejidad no válido")

    caracteres_permitidos, longitud_media = niveles[nivel_de_complejidad]

    mayusculas_repetidas = ''.join(secrets.choice(mayusculas) for _ in range(2))
    minusculas_repetidas = ''.join(secrets.choice(minusculas) for _ in range(2))
    numeros_especiales = ''.join(secrets.choice(numeros + especiales) for _ in range(2))

    longitud_media = longitud - 6

    contrasena_media = ''.join(secrets.choice(caracteres_permitidos) for _ in range(longitud_media))

    contrasena = mayusculas_repetidas + numeros_especiales + contrasena_media + numeros_especiales + minusculas_repetidas

    contrasena = ''.join(random.sample(contrasena, len(contrasena)))

    return contrasena

def generar_contraseñas(num_contraseñas, longitud, nivel_de_complejidad="fuerte"):
    contraseñas_generadas = []
    for _ in range(num_contraseñas):
        contraseña_generada = generar_contraseña_avanzada(longitud, nivel_de_complejidad)
        contraseñas_generadas.append(contraseña_generada)
    return contraseñas_generadas

def mostrar_contraseñas(contraseñas_generadas):
    print("\nContraseñas generadas:")
    for i, contraseña in enumerate(contraseñas_generadas):
        print(f"Contraseña {i + 1}: {contraseña}")

# Dibujo ASCII
print("┼┼┼┼┼┼┼┼▓▓▓▓┼┼┼")
print("┼╔═▒▒▒▒▓▄░░▄▓┼┼")
print("┼▀┼▒▒▒▓▓▒──▒▓▓┼")
print("┼┼┼▒▌▒▐┼▓▓▓▓┼┼┼")
print("            Lion v3.0\n")

# Elegir el nivel de complejidad
nivel = input("Elija el nivel de complejidad (debil, fuerte, cifrado): ")

if nivel in ["debil", "fuerte", "cifrado"]:
    num_contraseñas = int(input("Elija el número de contraseñas a generar: "))
    longitud = int(input("Elija la longitud de las contraseñas: "))
    
    contraseñas_generadas = generar_contraseñas(num_contraseñas, longitud, nivel)
    
    mostrar_contraseñas(contraseñas_generadas)
else:
    print("Nivel de complejidad no válido. Elija entre 'debil', 'fuerte' o 'cifrado'.")