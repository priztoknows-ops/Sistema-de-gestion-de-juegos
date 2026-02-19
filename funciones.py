import datos

def agregar_juego():
    id_juego = input("ID: ")

    if id_juego in datos.ids_usados:
        print("ID ya existente")
        return
    elif id_juego == "":
        print("ID no puede estar vacio")
        return
    nombre = input("Nombre: ")
    genero = input("Genero: ")
    try:
        precio = float(input("Precio: "))
    except:
        print("Precio Invalido")
        return
    juego = {
        "id" : id_juego,
        "nombre" : nombre,
        "genero" : genero,
        "precio" : precio,
    }
    datos.juegos.append(juego)
    datos.ids_usados.add(id_juego)
    print("Juego Agregado correctamente")

def mostrar_juegos():
    if len(datos.juegos) == 0:
        print("No hay juegos registrados")
        return
    for juego in datos.juegos:
        print("------------------------------")
        print(f"ID: {juego['id']}")
        print(f"Nombre: {juego['nombre']}")
        print(f"Genero: {juego['genero']}")
        print(f"Precio: ${juego['precio']:.3f}")
        print("------------------------------")

def buscar_juegos():
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
    id_eliminar = input("ID a eliminar: ")
    for juego in datos.juegos:
        if juego["id"] == id_eliminar:
            datos.juegos.remove(juego)
            datos.ids_usados.remove(id_eliminar)
            print("Juego eliminado correctamente")
            return
    print("Juego no encontrado")

def estadisticas():
    if len(datos.juegos) == 0:
        print("No hay juegos registrados")
        return
    total = len(datos.juegos)
    suma_precio = 0
    mas_caro = datos.juegos[0]
    mas_barato = datos.juegos[0]
    for juego in datos.juegos:
        suma_precio += juego["precio"]
        if juego["precio"] > mas_caro["precio"]:
            mas_caro = juego
        if juego["precio"] < mas_barato["precio"]:
            mas_barato = juego
    print("\nEstadisticas: ")
    print(f"Total de juegos: {total}")
    print(f"Precio promedio: {suma_precio / total}")
    print(f"Juego mas caro: {mas_caro['nombre']} (${mas_caro['precio']}")
    print(f"Juego mas barato: {mas_barato['nombre']} (${mas_barato['precio']}")
    