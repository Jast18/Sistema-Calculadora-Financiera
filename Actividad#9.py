#Administrador de una coleccion de libros utilizando diccionarios, listas args kwargs 
# Jonathan Soto 1533825

def agregar_libros(*titulos):
    biblioteca = []
    for titulo in titulos:
        biblioteca.append(titulo)
    return biblioteca

def asignar_detalles(titulo, autor, genero, año):
    Libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "año": año
    }
    return Libro

def mostrar_biblioteca():
    biblioteca = []
    biblioteca.append(asignar_detalles("El Mundo de Sofia", "Gabriel Garcia Marquez", "Realismo mágico", 1967))
    biblioteca.append(asignar_detalles("1948", "George Orwell", "Distropía", 1949))
    biblioteca.append(asignar_detalles)

def buscar_libros(**filtros):
    biblioteca = mostrar_biblioteca()
    resultados = []
    for libro in biblioteca:
        coincide = True
        for clave, valor in  filtros.items():
            if clave in libro and libro[clave] != valor:
                coincide = False
                break
        if coincide:
            resultados.append(libro)
    return resultados

# Ejemplo de uso:
biblioteca = agregar_libros("El Mundo de Sofia", 1948, "1948")
print("Biblioteca: ", biblioteca)
print("Detalles del libro: ", asignar_detalles())

