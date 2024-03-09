#generar una cantidad de contraseñas indicando el numero de letras simbolos y numeros

import string
import random

totalPasswords = int(input("Cuantas contraseñas necesitas: "))
totalLetras = int(input("Ingrese total letras: ")) 
totalNumeros = int(input("Ingrese total numeros: ")) 
totalSimbolos = int(input("Ingrese total simbolos: ")) 


caracteres = []


caracteres.extend(random.choices(string.digits,k = totalNumeros))
caracteres.extend(random.choices(string.ascii_letters,k = totalLetras))
caracteres.extend(random.choices(string.punctuation ,k = totalSimbolos))


random.shuffle(caracteres)
 
password = ''.join(caracteres)

for i in range(1,totalPasswords + 1) :
    random.shuffle(caracteres)
 
    password = ''.join(caracteres)
   
    print( i, ":  " , password)