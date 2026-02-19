import datos
import csv
import os

def exportar_csv():
    """
    Genera un archivo CSV con los datos de los juegos. Usa la libreria 'os' para asegurar que el archivo se cree en la ruta correcta.
    """
    # Determinamos la ruta absoluta del archivo para evitar que se pierda en el PC
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_completa = os.path.join(ruta_actual, "juegos.csv")

    print(f"\nIntentando crear el archivo en: {ruta_completa}")
    
    try:
        # Abrimos el archivo en modo escritura
        with open(ruta_completa, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            # Escribimos el encabezado del archivo
            writer.writerow(["ID", "Nombre", "Precio"])
            # Escribimos la lista de cada juego
            for juego in datos.juegos:
                writer.writerow([
                    juego["id"],
                    juego["nombre"],
                    juego["precio"]
                ])
        print(f"Archivo juegos.csv generado correctamente en: {ruta_completa}")
    except Exception as e:
        print(f"Error al crear el archivo: {e}")

def agregar_juego():
    """
    Agrega un juego validando que el ID sea unico, utilizando la estructura de datos 'set'.
    """
    id_juego = input("ID: ")

    # Validacion de ID unico usando el SET de datos.py
    if id_juego in datos.ids_usados:
        print("ID ya existente")
        return
    # En caso de que el usuario no escriba ningun ID, se informa al usuario y se cancela el registro
    elif id_juego == "":
        print("ID no puede estar vacio")
        return
    nombre = input("Nombre: ")
    genero = input("Genero: ")
    # Usamos try/except para tener en cuenta errores si el usuario ingresa letras en el precio
    try:
        precio = float(input("Precio: "))
    except:
        print("Precio Invalido")
        return
    # Creamos la lista con los datos solicitados
    juego = {
        "id" : id_juego,
        "nombre" : nombre,
        "genero" : genero,
        "precio" : precio,
    }
    # Agregamos el juego a la lista de datos y registramos el ID
    datos.juegos.append(juego)
    datos.ids_usados.add(id_juego)
    # En caso de actualizar datos, se actualiza el archivo CSV
    exportar_csv()
    print("Juego agregado y archivo actualizado")

def mostrar_juegos():
    """
    Muestra todos los juegos registrados en la lista de datos.
    """
    if len(datos.juegos) == 0:
        print("No hay juegos registrados")
        return
    for juego in datos.juegos:
        print("------------------------------")
        print(f"ID: {juego['id']}")
        print(f"Nombre: {juego['nombre']}")
        print(f"Genero: {juego['genero']}")
        print(f"Precio: ${juego['precio']:.3f}") # Formato a 3 decimales
        print("------------------------------")

def buscar_juegos():
    """
    Busca un juego especifico por su ID.
    """
    id_buscar = input("ID a buscar: ")
    encontrado = False

    for juego in datos.juegos:
        if juego["id"] == id_buscar:
            print("Juego encontrado:")
            print(f"Nombre: {juego['nombre']}")
            print(f"Genero: {juego['genero']}")
            print(f"Precio: {juego['precio']}")
            encontrado = True
            break

    if not encontrado:
        print("Juego no encontrado")

def eliminar_juegos():
    """
    Elimina un juego de la lista usando el ID, liberandolo del set para un nuevo registro.
    """
    id_eliminar = input("ID a eliminar: ")
    for juego in datos.juegos:
        if juego["id"] == id_eliminar:
            datos.juegos.remove(juego)
            datos.ids_usados.remove(id_eliminar) # Se utiliza para poder reutilizar el ID
            print("Juego eliminado correctamente")
            return
    print("Juego no encontrado")

def estadisticas():
    """
    Analiza la lista de juegos del usuario para generar estadisticas tales como calcular el total de registros, el promedio de precios, el juego mas caro y el mas barato.
    """
    # Validacion inicial, si la lista se encuentra vacia, no se puede realizar la lista de estadisticas
    if len(datos.juegos) == 0:
        print("No hay juegos registrados")
        return
    total = len(datos.juegos)
    suma_precio = 0
    mas_caro = datos.juegos[0]
    mas_barato = datos.juegos[0]
    # Analizamos la lista del usuario
    for juego in datos.juegos:
        # Se suma el precio de todos los juegos de la lista y se calculo el promedio de estos
        suma_precio += juego["precio"]
        # Se presenta el juego mas caro presentado en la lista, en caso de agregar otro, esta lista se actualiza
        if juego["precio"] > mas_caro["precio"]:
            mas_caro = juego
        # Se presenta el juego mas barato presentado en la lista, en caso de agregar otro, esta lista se actualiza
        if juego["precio"] < mas_barato["precio"]:
            mas_barato = juego
    # Se muestran los resultados finales de la lista de estadisticas
    print("\nEstadisticas: ")
    print(f"Total de juegos: {total}")
    print(f"Precio promedio: {suma_precio / total}")
    print(f"Juego mas caro: {mas_caro['nombre']} (${mas_caro['precio']})")
    print(f"Juego mas barato: {mas_barato['nombre']} (${mas_barato['precio']})")