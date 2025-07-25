biblioteca = []

def agregar_libros(*titulos):
    for titulo in titulos:
        libro = {
            "titulo": titulo,
            "autor": "",
            "genero": "",
            "año": None
        }
        biblioteca.append(libro)

def asignar_detalles(titulo, autor, genero, año):
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            libro["autor"] = autor
            libro["genero"] = genero
            libro["año"] = año
            break

def mostrar_biblioteca():
    print("\n--- Biblioteca ---")
    for libro in biblioteca:
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Género: {libro['genero']}")
        print(f"Año: {libro['año']}\n")

def buscar_libros(**filtros):
    resultados = biblioteca

    if "genero" in filtros:
        resultados = [l for l in resultados if l["genero"].lower() == filtros["genero"].lower()]
    if "autor" in filtros:
        resultados = [l for l in resultados if l["autor"].lower() == filtros["autor"].lower()]
    if "año_max" in filtros:
        resultados = [l for l in resultados if l["año"] is not None and l["año"] <= filtros["año_max"]]

    print("\n--- Resultados de búsqueda ---")
    for libro in resultados:
        print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año']}, Género: {libro['genero']}")


agregar_libros("cien años de soledad", "El principito", "Don Quijote")
asignar_detalles("El principito", "Antoine de Saint-Exupéry", "Ficción", 1943)
asignar_detalles("Cien años de soledad", "Gabriel Garcia Márquez", "Realismo magico", 1967)
asignar_detalles("Don quijote", "Miguel de cervantes", "Novela", 1605)
mostrar_biblioteca()
buscar_libros(genero="Ficción", año_max=2000)
