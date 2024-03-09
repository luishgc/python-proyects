
listaAplicantes = []
estado = input("Bienvenido a la subasta deseas partisipar si/no: ")
montoMayor = 0

def agregarAplicante(nombre, monto):
    nuevoAplicante = {
        "nombre":nombre,
        "monto":monto
    }

    listaAplicantes.append(nuevoAplicante)

while estado == "si":
    nombre = input("Ingrese su nombre: ")
    monto = int(input("Ingrese su oferta: "))
    agregarAplicante(nombre, monto)
    estado = input("Deseas continuar con la subasta? ")
    if estado == "no":
        for i in listaAplicantes:
            if i["monto"] > montoMayor:
                montoMayor = i["monto"]
                ganador = i["nombre"]

        break

print(f"El ganador de la subasta fue {ganador} con una oferta de {montoMayor}.00 soles Felicitaciones!!")