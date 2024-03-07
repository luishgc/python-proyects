#adivinar la palabra, mostrar espacios en blanco de la lista de palabras a adivinar, si la palabra existe ir rellenando la palabra 


import random

palabras = ["cusco","arequipa","lima","ica"]
palabraRandom = random.choice(palabras)
palabraVacia = "_" * len(palabraRandom)
palabraLista = list(palabraVacia)
intentos = 1
while True:
    letra = input("Ingresa letra: ").lower()
    if letra in palabraRandom:
        for i in range(len(palabraRandom)):
            if palabraRandom[i] == letra:
                palabraLista[i] = letra
        print("Adivina la palabra: "+"".join(palabraLista))
        if "_" not in palabraLista:
            print("Felicitaciones")
            break                             
    else:
        print("Intenta con otra letra")
    intentos += 1
print("Lo conseguiste en: ", intentos, "intentos")

            