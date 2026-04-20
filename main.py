# TP Integrador - Programación I

import csv

def cargar_paises_desde_csv(nombre_archivo):

    # Lee el CSV con encabezado (nombre, poblacion, superficie, continente) y devuelve
    # una lista de diccionarios: un dict por país, tipos numéricos para población y superficie.

    paises = []

    with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
        # DictReader usa la primera línea del CSV como claves
        lector = csv.DictReader(archivo)

        for fila in lector:
            pais = {
                "nombre": fila["nombre"].strip(),
                "poblacion": int(fila["poblacion"]),
                "superficie": int(fila["superficie"]),
                "continente": fila["continente"].strip(),
            }
            paises.append(pais)

    return paises


def main():
    # Carga inicial del dataset base
    paises = cargar_paises_desde_csv("paises.csv")

    print("Gestión de datos de países — sistema iniciado")
    print(f"Países cargados en memoria: {len(paises)}\n")

    while True:
        print("--- Menú ---")
        print("1) Agregar país")
        print("2) Actualizar población y superficie de un país")
        print("3) Buscar país por nombre")
        print("4) Filtrar países")
        print("5) Ordenar países")
        print("6) Mostrar estadísticas")
        print("0) Salir")

        opcion = input("Opción: ").strip()

        if opcion == "0":
            print("Fin del programa.")
            break

        elif opcion == "1":
            # Alta de país con todos los campos obligatorios (sin vacíos).
            print("Pendiente: agregar país.\n")

        elif opcion == "2":
            # Actualizar solo población y superficie de un país identificado.
            print("Pendiente: actualizar datos.\n")

        elif opcion == "3":
            # Búsqueda por nombre (coincidencia parcial o exacta — a definir en la implementación).
            print("Pendiente: búsqueda.\n")

        elif opcion == "4":
            # Filtrar por continente, rango de población y rango de superficie.
            print("Pendiente: filtros.\n")

        elif opcion == "5":
            # Ordenar por nombre, población o superficie; ascendente o descendente.
            print("Pendiente: ordenamientos.\n")

        elif opcion == "6":
            # Estadísticas (máx/mín población, promedios, cantidad por continente).
            print("Pendiente: estadísticas.\n")

        else:
            print("Opción inválida.\n")


# Solo ejecuta el menú si este archivo es el punto de entrada
if __name__ == "__main__":
    main()
