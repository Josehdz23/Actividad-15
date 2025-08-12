participantes = {}
def menu():
    print("\n= = = = MENÚ DE OPCIONES = = = =\n1. Agregar participante\n2. Mostrar participantes ordenados por nombre\n3. Mostrar participantes ordenados por edad\n4. Salir")

def ingreso():
    while True:
        try:
            print("= = = = Ingreso de participantes, presione ( 0 ) para regresar al menú principal = = = =")
            n = int(input("\n¿Cuántos participantes desea ingresar?: "))
            if n == 0:
                print("Regresará al menú principal. . .")
                break
            elif n < 0 :
                print("Número inválido para agregar participantes, volviendo al menú principal. . .")
            elif n > 0:
                for i in range(n):
                    print(f"\nPARTICIPANTE #{i + 1}")
                    while True:
                        try:
                            dorsal = int(input("Ingrese el dorsal del participante: "))
                            if dorsal > 0:
                                if dorsal in participantes:
                                    print("El dorsal ya está en uso, pruebe otro")
                                else:
                                    break
                        except Exception as ex:
                            print(f"Ha ocurrido un error: {ex}")
                    while True:
                        nombre = input("Ingrese el nombre del participante: ")
                        if nombre or nombre.isspace():
                            break
                        else:
                            print("Nombre inválido, reintente")
                    while True:
                        try:
                            edad = int(input("Ingrese la edad del participante (15 - 35): "))
                            if edad >= 15:
                                break
                            else:
                                print("La edad no es válida, reintente")
                        except Exception as ex:
                            print(f"Ha ocurrido un error: {ex}")
                    while True:
                        categoria = input("Ingrese la categoría del participante (Juvenil, Adulto, Máster): ").upper()
                        if categoria or categoria.isspace():
                            if ((categoria == "JUVENIL") or (categoria == "ADULTO") or (categoria == "MÁSTER")):
                                break
                            else:
                                print("La categoría ingresada no es válida, reintente")
                        else:
                            print("Nombre inválido, reintente")
                    participantes[dorsal] = {
                        "nombre": nombre,
                        "edad": edad,
                        "categoria": categoria
                    }
            break
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")

def quick_sort_nombre(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x[1]["nombre"] < pivote[1]["nombre"]]
        iguales = [x for x in lista if x[1]["nombre"] == pivote[1]["nombre"]]
        mayores = [x for x in lista[1:] if x[1]["nombre"] > pivote[1]["nombre"]]
        return quick_sort_nombre(menores) + iguales + quick_sort_nombre(mayores)

def quick_sort_edad(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x[1]["edad"] < pivote[1]["edad"]]
        iguales = [x for x in lista if x[1]["edad"] == pivote[1]["edad"]]
        mayores = [x for x in lista[1:] if x[1]["edad"] > pivote[1]["edad"]]
        return quick_sort_nombre(menores) + iguales + quick_sort_nombre(mayores)

def mostrarPorNombre():
    if participantes:
        lista = list(participantes.items())
        ordenada = quick_sort_nombre(lista)
        diccionarioOrdenado = dict(ordenada)
        for clave, datos in diccionarioOrdenado.items():
            print(f"-{datos["nombre"]} (Dorsal: {clave}, Edad: {datos["edad"]}, Categoria: {datos["categoria"]})")
    else:
        print("No hay participantes registrados!!!")

def mostrarPorEdad():
    if participantes:
        lista = list(participantes.items())
        ordenada = quick_sort_edad(lista)
        diccionarioOrdenado = dict(ordenada)
        for clave, datos in diccionarioOrdenado.items():
            print(f"-{datos["nombre"]} (Dorsal: {clave}, Edad: {datos["edad"]}, Categoria: {datos["categoria"]})")
    else:
        print("No hay participantes registrados!!!")

def main():
    while True:
        try:
            menu()
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    ingreso()
                case 2:
                    mostrarPorNombre()
                case 3:
                    mostrarPorEdad()
                case 4:
                    print("\nS A L I E N D O . . .")
                    break
                case _:
                    print("Opción inexistente, reintente")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")
main()