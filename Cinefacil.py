# cinefacil.py

# Funciones disponibles
funciones_disponibles = [
    {"pelicula": "Avengers: Endgame", "horario": "15:00"},
    {"pelicula": "Spider-Man: No Way Home", "horario": "18:00"},
    {"pelicula": "Encanto", "horario": "20:00"},
]

# Precio por entrada
precio_entrada = 35.00

# Lista para almacenar reservas
reservas = []

def mostrar_funciones():
    print("\nFunciones disponibles:")
    for i, funcion in enumerate(funciones_disponibles, 1):
        print(f"{i}. {funcion['pelicula']} - {funcion['horario']}")

def realizar_reserva():
    nombre = input("Ingrese su nombre: ")
    mostrar_funciones()
    eleccion = int(input("Seleccione el número de la función deseada: ")) - 1

    if eleccion < 0 or eleccion >= len(funciones_disponibles):
        print("Opción no válida.")
        return

    cantidad = int(input("¿Cuántos boletos desea comprar?: "))
    total = cantidad * precio_entrada

    reserva = {
        "cliente": nombre,
        "pelicula": funciones_disponibles[eleccion]["pelicula"],
        "horario": funciones_disponibles[eleccion]["horario"],
        "cantidad": cantidad,
        "total": total
    }

    reservas.append(reserva)

    print("\n--- RESUMEN DE RESERVA ---")
    print(f"Cliente: {nombre}")
    print(f"Película: {reserva['pelicula']}")
    print(f"Horario: {reserva['horario']}")
    print(f"Entradas: {cantidad}")
    print(f"Total a pagar: Q{total:.2f}")
   

def mostrar_reservas():
    if not reservas:
        print("No hay reservas registradas.")
        return

    print("\n--- TODAS LAS RESERVAS ---")
    for r in reservas:
        print(f"{r['cliente']} - {r['pelicula']} - {r['horario']} - {r['cantidad']} entradas - Q{r['total']:.2f}")

# Menú principal
def menu():
    while True:
        print("\n--- CineFácil ---")
        print("1. Realizar reserva")
        print("2. Ver todas las reservas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            realizar_reserva()
        elif opcion == "2":
            mostrar_reservas()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
