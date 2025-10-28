import random

nombre = input("¿Como te llamas?")
estado = random.choice(["Feliz😁", "triste 😢", "enojado🤬", "relajado 😌","cansado😴", "embriagado 🥴", "enfermo🤧", "con frio 🥶", "con calor 🥵" "con nauseas🤢" ])
print(f"Hola ¨{nombre}, tu estado de animo hoy es: {estado}")