def asistencia(codes):
    cod = input("\n-- Verificación de Boletos --\n\nIngrese el código de su ticket: ")

    if cod in codes:
        index = codes.index(cod)
        print("\nEl boleto asociado al código",codes.pop(index),"es auténtico. ¡Disfrute su partido!\n")
        return codes
    else:
        x = input("\nEste código es inválido., ¿Desea ingresar otro código?\n\n    1. Sí\n    2. No\n\nIngrese una opción: ")

        while x != "1" and x != "2":
            x = input("Seleccione un valor de la lista dada: ")

        if x == "1":
            return asistencia(codes)
        elif x == "2":
            return codes
        
        