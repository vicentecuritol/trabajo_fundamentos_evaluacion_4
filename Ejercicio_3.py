#Ejercicio_3
pj_viña = {}
viña_as = [3,6,13,24]
pj_valpo = {}
valpo_as = [1,5,16,3,21]
while True:
    print("""***** SISTEMA DE PASAJES PASAJEBUS *****
                1.- Comprar pasaje a Viña del Mar
                2.- Comprar pasaje a Valparaíso
                3.- Ver asientos disponibles
                4.- Ver lista de pasajeros
                5.- Salir""")
    while True:
        try:
            op = int(input("Seleccione una opción: "))
            if 0 > op or op > 5:
                print("Ingrese digitos numericos del 1 al 5.")
            else:
                break
        except ValueError:
            print("Ingrese números numericos enteros.")
    if op == 1:
        print(f"Asientos disponibles: {viña_as}")
        rut_v = input("Ingrese su RUT: ") 
        if rut_v in pj_viña:
            print("El RUT ya se encuentra registrado.")
        else:
            name = input("Ingrese su nombre: ")
            while True:
                try:
                    asiento = int(input("Escoja su asiento: "))
                    if asiento not in viña_as:
                        print("Asiento ya reservado.")
                    else:
                        viña_as.remove(asiento)
                        print("Compra realizada con exito.\n")
                        break
                except ValueError:
                    print("Ingrese digitos númericos.")
            pj_viña[rut_v] = [name, asiento]
    elif op == 2: 
        print(f"Asientos disponibles: {valpo_as}")
        rut_val = input("Ingrese su RUT: ") 
        if rut_val in pj_valpo:
            print("El RUT ya se encuentra registrado.")
        else:
            name = input("Ingrese su nombre: ")
            while True:
                try:
                    asiento = int(input("Escoja su asiento: "))
                    if asiento not in valpo_as:
                        print("Asiento ya reservado.")
                    else:
                        valpo_as.remove(asiento)
                        print("Compra realizada con exito.\n")
                        break
                except ValueError:
                    print("Ingrese digitos númericos.")
            pj_valpo[rut_val] = [name, asiento]
    elif op == 3:
        print(f"""Asientos disponibles en: 
                  -Viña del mar: {viña_as}
                  -Valparaiso: {valpo_as}
               """)
    elif op == 4:
        print("Lista de pasajeros - Viña del Mar:")
        for rut_v, datos in pj_viña.items():
            print(f"RUT: {rut_v} - Nombre: {datos[0]} - Asiento: {datos[1]}")

        print("\nLista de pasajeros - Valparaíso:")
        for rut_val, datos in pj_valpo.items():
            print(f"RUT: {rut_val} - Nombre: {datos[0]} - Asiento: {datos[1]}")

    elif op == 5:
        print("Gracias por usar PasajeBus.")
        break