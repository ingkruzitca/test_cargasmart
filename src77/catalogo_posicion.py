
# catalogo_futbol.py

class Equipo:
    def __init__(self):
        # Diccionario: {nombre_jugador: posicion}
        self.jugadores = {}

    def agregar_jugador(self, nombre, posicion):
        if nombre in self.jugadores:
            print(f"El jugador '{nombre}' ya existe. Se actualizará su posición.")
        self.jugadores[nombre] = posicion
        print(f"Jugador '{nombre}' agregado/actualizado como '{posicion}'.")

    def listar_jugadores(self):
        if not self.jugadores:
            print("No hay jugadores en el catálogo.")
            return
        print("\n--- Lista de jugadores ---")
        for nombre, posicion in self.jugadores.items():
            print(f"{nombre} -> {posicion}")
        print("--------------------------\n")

    def buscar_jugador(self, nombre):
        if nombre in self.jugadores:
            print(f"{nombre} juega como {self.jugadores[nombre]}.")
        else:
            print(f"No se encontró al jugador '{nombre}'.")

    def eliminar_jugador(self, nombre):
        if nombre in self.jugadores:
            del self.jugadores[nombre]
            print(f"Jugador '{nombre}' eliminado.")
        else:
            print(f"No existe el jugador '{nombre}'.")


def menu():
    equipo = Equipo()

    while True:
        print("""
--- Menú ---
1. Agregar jugador
2. Listar jugadores
3. Buscar jugador
4. Eliminar jugador
5. Salir
""")
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                nombre = input("Nombre del jugador: ")
                posicion = input("Posición (ej: defensa, mediocampo, delantero, portero): ")
                equipo.agregar_jugador(nombre, posicion)

            case "2":
                equipo.listar_jugadores()

            case "3":
                nombre = input("Nombre del jugador a buscar: ")
                equipo.buscar_jugador(nombre)

            case "4":
                nombre = input("Nombre del jugador a eliminar: ")
                equipo.eliminar_jugador(nombre)

            case "5":
                print("Saliendo...")
                break

            case _:
                print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    menu()