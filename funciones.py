#funcion para registar los prestamos
def registrar_prestamo(prestamos):
    nombre = input("ingrese su nombre completo: ") #al llegar a este punto y los siguentes el programa le pide al usuario que ingrese los datos necesarios
    idlibro = input("ingrese la ID del libro: ")
    fechaR = input("ingrese la fecha de recibo d/m/a: ")
    fechaD = input("ingrese la fecha de devolución d/m/a:   ")

#se guarda los datos en diccionario que contenga toda la informacion
    prestamo = {
        'nombre': nombre,
        'id del libro': idlibro,
        'fecha de recibo': fechaR,
        'fecha de devolucion': fechaD
    }
    
    prestamos.append(prestamo) #prestamos.append... agrega los datos al ingresados al diccionario
    print("prestamo registrado exitosamente.")


def listar_prestamos(prestamos): #funcion para listar los ´prestamos registrados anteriormente
    if not prestamos: #se abre una funcion de deciciones por si en la funcion prestamos no existe informacion
        print("no hay préstamos registrados.")
        return #retorno

    for prestamo in prestamos: #se imprime todos los datos registrados
        print(' ')
        print(f"Nombre: {prestamo['nombre']}")
        print(f"ID del libro: {prestamo['id del libro']}")
        print(f"fecha de recibo: {prestamo['fecha de recibo']}")
        print(f"fecha de devolución: {prestamo['fecha de devolucion']}")
        print("")


def imprimir_hoja(prestamos):
    if not prestamos: #se abre una funcion de deciciones por si en la funcion prestamos no existe informacion
        print("no existen prestamos registrados")
        return

    with open("listado_de_prestamos.txt", "w") as file:  #se crea el documento txt #se le otorga el permiso de escritura
        for prestamo in prestamos:
            file.write(f"nombre: {prestamo['nombre']}\n") 
            file.write(f"ID del libro: {prestamo['id del libro']}\n")
            file.write(f"fecha de recibo: {prestamo['fecha de recibo']}\n")
            file.write(f"fecha de devolución: {prestamo['fecha de devolucion']}\n")
            file.write("\n")
    
    print("documento txt creado con exito")

def salir():
    print('saliendo del programa... ')

