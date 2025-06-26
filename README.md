# trabajo_fundamentos_evaluacion_4
asientos_vina = list(range(1, 15))  # Por ejemplo, 10 asientos del 1 al 10
asientos_valpo = list(range(1, 15))

pasajeros_vina = {}     # RUT: (Nombre, Asiento)
pasajeros_valpo = {}    # RUT: (Nombre, Asiento)

def mostrar_menu():
    print("\n***** SISTEMA DE PASAJES PASAJEBUS *****")
    print("1.- Comprar pasaje a Viña del Mar")
    print("2.- Comprar pasaje a Valparaíso")
    print("3.- Ver asientos disponibles")
    print("4.- Ver lista de pasajeros")
    print("5.- Salir")

def mostrar_asientos_disponibles(destino):
    if destino == "Viña del Mar":
        print(f"Asientos disponibles para Viña del Mar: {asientos_vina}")
    elif destino == "Valparaíso":
        print(f"Asientos disponibles para Valparaíso: {asientos_valpo}")

def comprar_pasaje(destino):
    if destino == "Viña del Mar":
        asientos = asientos_vina
        pasajeros = pasajeros_vina
    else:
        asientos = asientos_valpo
        pasajeros = pasajeros_valpo

    mostrar_asientos_disponibles(destino)

    rut = input("Ingrese su RUT: ")
    if rut in pasajeros:
        print("Ya tiene un pasaje registrado para este destino.")
        return

    nombre = input("Ingrese su nombre: ")
    try:
        asiento = int(input("Ingrese el número de asiento deseado: "))
    except ValueError:
        print("Número de asiento inválido.")
        return

    if asiento not in asientos:
        print("El asiento no está disponible.")
        return

    pasajeros[rut] = (nombre, asiento)
    asientos.remove(asiento)
    print(f"Pasaje registrado correctamente para {nombre} en asiento {asiento} a {destino}.")

def ver_lista_pasajeros():
    print("\nLista de pasajeros a Viña del Mar:")
    for rut, (nombre, asiento) in pasajeros_vina.items():
        print(f"RUT: {rut}, Nombre: {nombre}, Asiento: {asiento}")

    print("\nLista de pasajeros a Valparaíso:")
    for rut, (nombre, asiento) in pasajeros_valpo.items():
        print(f"RUT: {rut}, Nombre: {nombre}, Asiento: {asiento}")


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        comprar_pasaje("Viña del Mar")
    elif opcion == "2":
        comprar_pasaje("Valparaíso")
    elif opcion == "3":
        mostrar_asientos_disponibles("Viña del Mar")
        mostrar_asientos_disponibles("Valparaíso")
    elif opcion == "4":
        ver_lista_pasajeros()
    elif opcion == "5":
        print("Gracias por usar PasajeBus.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")

