import string

alfabeto = string.ascii_letters
print("Indica que quieres hacer: \n A: Encriptar \n B: desencriptar")
pasoUno = input()
palabra = ""
clave = int()

def encriptar(palabra, clave):  
    palabra = input("ingrese palabra: ")
    clave = int(input("Ingrese clave: "))     
    encriptado = ""
    for i in palabra:
    
        if i in alfabeto:
            indice = alfabeto.index(i)
            indiceEncriptado = (indice + clave) % 26
            encriptado += alfabeto[indiceEncriptado]    
        else:
            encriptado += i   

    return encriptado

def desencriptar(palabra, clave):
    palabra = input("ingrese palabra encriptada: ")
    clave = int(input("Ingrese clave: "))
    encriptado = ""
    for i in palabra:
    
        if i in alfabeto:
            indice = alfabeto.index(i)
            indiceEncriptado = (indice - clave) % 26
            encriptado += alfabeto[indiceEncriptado]
    
        else:
            encriptado += i           

    return encriptado
    



if pasoUno == "A":
    
    print("Encriptada: ",encriptar(palabra, clave))
elif pasoUno == "B":
    print("Desencriptada: ",desencriptar(palabra, clave))
else:
    print("Selcciona A ó B")




