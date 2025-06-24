asiento = [1,2,4,5]
registro_pasaje = {}
while True:
    print("""
    ***** SISTEMA DE PASAJE PASAJEBUS *****
        1.- Ver asientos disponibles
        2.- Comprar pasaje
        3.- Ver pasajeros reistrados
        4.- Salir
        """)
    while True:
        try:
            op = int(input("ingrese una opcion: "))
            if 0 >= op or op > 4:
                print("ingrese valores del 1-3")
                continue
            else:
                break
        except ValueError:
            print("debe ingresar un numero positivo entero")
            continue
        
    if op == 1:
        print(f"asientos disponibles: {asiento}")
    elif op == 2:
        if len(asiento) == 0:
            print("lo sentimos, no quedan entradas disponibles en este momento")
            break
        while True:
            try:
                rut = input("ingrese su RUT: ")
                if len(rut) == 9:
                    if rut in registro_pasaje:
                        print("este rut ya esta registrado")
                        continue
                compra = int(input(f"que numero de asiento desea comprar, estos estan disponibles({asiento}): "))
                if compra <= 0:
                    print("ingrese valores positivos")
                    continue
                elif compra in asiento:
                    registro_pasaje[rut] = asiento
                    asiento.remove(compra)
                    print("felicidades, has comprado una entrada")
                    break
                else:
                    print("ingrese una de los asientos disponibles")
                    continue
            except ValueError:
                print("debe ingresar valores validos enteros")
    elif op == 3:
        if not registro_pasaje:
            print("No hay pasajeros registrados")
        else:
            print("\n--- Lista de Pasajeros ---")
            for rut, asiento in registro_pasaje.items():
                print(f"RUT: {rut}, Asiento: {asiento}")    
    elif op == 4:
        break
