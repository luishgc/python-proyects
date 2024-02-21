import random

numeros = [0,1,2,3,4,5,6,7,8,9]
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
simbolos = ["#","$","%","&","/","()","=","@","|","!","¡","?"]

totalNumeros = int(input("¿Cuantos numeros necesitas en tu contraseña? "))
totalLetras = int(input("¿Cuantas letras?"))
totalSimbolos = int(input("¿Cuantos simbolos?"))


numerosSeleccionados = random.sample(numeros, totalNumeros)
numerosSeleccionadosPulidos = int(''.join(map(str, numerosSeleccionados[:totalNumeros])))
print(numerosSeleccionadosPulidos)

letrasSeleccionadas = random.sample(letras, totalLetras)
letrasSeleccionadasPulidas = ''.join(letrasSeleccionadas)
print(letrasSeleccionadasPulidas)

simbolosSeleccionados = random.sample(simbolos, totalSimbolos)
simbolosSeleccionadosPulidos = ''.join(simbolosSeleccionados)
print(simbolosSeleccionadosPulidos)

passwordTotal = f"{numerosSeleccionadosPulidos}{letrasSeleccionadasPulidas}{simbolosSeleccionadosPulidos}"

print(f"tu contraseña es la siguiente {passwordTotal}")