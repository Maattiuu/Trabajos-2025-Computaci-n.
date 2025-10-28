import random #  importar el modulo random para numeros aleatorios

numero_secreto = random.randint(1,10) #genera numeros del 1-10
intento = int(input("Adivina un numero del 1-10"))

if intento == numero_secreto:
    print("Correcto maquina de fuego")
else:
    print(f"Incorrecto chamaco. El numero era {numero_secreto}.")