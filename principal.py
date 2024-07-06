from funciones import registrar_prestamo, listar_prestamos, imprimir_hoja

prestamo = []


while True: #se crea un nucle de menu
    print("\nbienvenido a la biblioteca de prestamos")
    print("1. Registrar prestamos")
    print("2. Listar prestamos")
    print("3. Imprimir hoja de prestamos")
    print("4. Salir del programa")
    opcion = input("Seleccione una opción segun su numero correspondiente: ")

    if opcion == '1':
        registrar_prestamo(prestamo) #se llama a la funcion del archivo funciones.py 
    elif opcion == '2':
        listar_prestamos(prestamo)
    elif opcion == '3':
        imprimir_hoja(prestamo)
    elif opcion == '4':
        exit
    else:
        print("Opción no válida. Intente de nuevo.")
