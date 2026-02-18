import funciones

def menu():
    while True:
        print("1. Agregar")
        print("2. Mostrar")
        print("3. Buscar")
        print("4. Eliminar")
        print("5. Estadisticas")
        print("6. Salir")

        op = input("Opcion")
        
        if op == "1":
            funciones.agregar_juego()
        elif op == "2":
            funciones.mostrar_juegos()
        elif op == "3":
            funciones.buscar_juegos()
        elif op == "4":
            funciones.eliminar_juegos()
        elif op == "5":
            funciones.estadisticas()
        elif op == "6":
            break
        else:
            print("Opcion Invalida")

menu()