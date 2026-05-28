# TP Integrador - Programación I
import csv
import os
import unicodedata # esta biblioteca permite manipular tildes, símbolos y caracteres especiales de manera uniforme en cadenas de texto.

# El CSV queda en la misma carpeta que este .py (aunque ejecutes desde otra ruta)
CARPETA_PROYECTO = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_PAISES = os.path.join(CARPETA_PROYECTO, "paises.csv")

def normalizar(texto): # función para sacar acentos 
    texto = texto.lower().strip()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto


def parsear_entero_positivo(texto, nombre_campo):
    # Convierte a int y exige valor mayor que cero (mínimo 1).
    valor = int(texto)
    if valor <= 0:
        raise ValueError(f"{nombre_campo} debe ser mayor que cero.")
    return valor


def cargar_paises_desde_csv(nombre_archivo):

    # Lee el CSV con encabezado (nombre, poblacion, superficie, continente) y devuelve
    # una lista de diccionarios: un dict por país, tipos numéricos para población y superficie.

    paises = []

    try:
        with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for numero_fila, fila in enumerate(lector, start=2):
                try:
                    nombre = fila.get("nombre", "").strip()
                    continente = fila.get("continente", "").strip()

                    if not nombre or not continente:
                        raise ValueError("nombre o continente vacío")

                    poblacion = parsear_entero_positivo(
                        fila["poblacion"], "población"
                    )
                    superficie = parsear_entero_positivo(
                        fila["superficie"], "superficie"
                    )

                    paises.append({
                        "nombre": nombre,
                        "poblacion": poblacion,
                        "superficie": superficie,
                        "continente": continente,
                    })

                except (ValueError, KeyError) as e:
                    print(
                        f"Advertencia: fila {numero_fila} del CSV ignorada ({e})."
                    )

    except FileNotFoundError:
        raise FileNotFoundError(
            f"No se encontró el archivo '{nombre_archivo}'."
        )

    return paises


def main():
    # Carga inicial del dataset base
    try:
        paises = cargar_paises_desde_csv(ARCHIVO_PAISES)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

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

        elif opcion == "1": # Agregar país
            print("\n--- Registrar Nuevo País ---")
            
           # se pide y se valida el nombre
            nombre_nuevo = input("Ingrese el nombre del país: ").strip()
            if not nombre_nuevo:
                print("Error: El nombre es obligatorio.")
            else:
                # Verifica que el pais no se encuentre en la lista (mismo criterio que buscar/actualizar)
                existe = False
                for p in paises:
                    if normalizar(p["nombre"]) == normalizar(nombre_nuevo):
                        existe = True
                        break
                
                if existe:
                    print(f"El país '{nombre_nuevo}' ya existe.\n")
                else:
                    # si el pais no esta en la lista, pide y valida los otros datos
                    try:
                        pob_input = input("Ingrese la población: ").strip()
                        sup_input = input("Ingrese la superficie: ").strip()
                        continente_nuevo = input("Ingrese el continente: ").strip()

                        # se verifica que todos los campos esten completos
                        if not pob_input or not sup_input or not continente_nuevo:
                            print("Error: Todos los campos deben estar completos.")
                        else:
                            poblacion_nuevo = parsear_entero_positivo(
                                pob_input, "La población"
                            )
                            superficie_nuevo = parsear_entero_positivo(
                                sup_input, "La superficie"
                            )

                            nuevo_pais = {
                                "nombre": nombre_nuevo,
                                "poblacion": poblacion_nuevo,
                                "superficie": superficie_nuevo,
                                "continente": continente_nuevo
                            }

                            try:
                                with open(ARCHIVO_PAISES, "a", newline="", encoding="utf-8") as archivo:
                                    escritor = csv.writer(archivo)
                                    escritor.writerow([
                                        nombre_nuevo,
                                        poblacion_nuevo,
                                        superficie_nuevo,
                                        continente_nuevo,
                                    ])
                                paises.append(nuevo_pais)
                                print("El país se agregó correctamente.\n")
                            except OSError:
                                print(
                                    "Error: no se pudo guardar en el CSV. "
                                    "El país no fue agregado.\n"
                                )

                    except ValueError as e:
                        print(f"Error: {e}")
            
            

        elif opcion == "2":  # Actualizar solo población y superficie de un país identificado.
            try:
                print("\n--- Actualizar datos de Población y Superficie de un país ---")
                nombre_actualizar = input(
                    "Ingrese el nombre del país a actualizar: "
                ).strip()

                pais_encontrado = None
                for p in paises:
                    if normalizar(p["nombre"]) == normalizar(nombre_actualizar):
                        pais_encontrado = p
                        break

                if pais_encontrado is None:
                    print(f"El país '{nombre_actualizar}' no se encuentra en la lista.\n")
                else:
                    pob_input = input("Nueva población: ").strip()
                    sup_input = input("Nueva superficie: ").strip()

                    nueva_poblacion = parsear_entero_positivo(
                        pob_input, "La población"
                    )
                    nueva_superficie = parsear_entero_positivo(
                        sup_input, "La superficie"
                    )

                    pais_encontrado["poblacion"] = nueva_poblacion
                    pais_encontrado["superficie"] = nueva_superficie

                    with open(ARCHIVO_PAISES, "w", newline="", encoding="utf-8") as archivo:
                        escritor = csv.writer(archivo)
                        escritor.writerow(
                            ["nombre", "poblacion", "superficie", "continente"]
                        )
                        for p in paises:
                            escritor.writerow([
                                p["nombre"],
                                p["poblacion"],
                                p["superficie"],
                                p["continente"],
                            ])

                    print("Los datos se actualizaron correctamente.\n")

            except ValueError as e:
                print(f"Error: {e}\n")

        elif opcion == "3": # Búsqueda por nombre (coincidencia parcial o exacta).
            try: 
                print("\n--- Busque un país por su nombre ---")
                nombre_buscar = input("Ingrese el país que quiere buscar: ").strip()
                
                busqueda= False
                for p in paises:
                    if normalizar(nombre_buscar) in normalizar(p["nombre"]):
                        busqueda = True
                        # Busca los datos del pais y los imprime
                        print("\nPaís encontrado:")
                        print(f"Nombre: {p['nombre']}")
                        print(f"Población: {p['poblacion']}")
                        print(f"Superficie: {p['superficie']}")
                        print(f"Continente: {p['continente']}\n")
                        
                        
                
                if not busqueda:
                    print("No se encontro el país.\n")
                    
            except Exception as e: # Error Exception, para errores no previstos.
                print("Error en la búsqueda:", e)        

        elif opcion == "4": # Filtrar países
            while True:
                print("\n--- Filtrar países ---")
                print("1) Por Continente: ")
                print("2) Por rango de población")
                print("3) Por rango de superficie")
                print("0) Para salir del menú")

                ingreso = input("Opción: ").strip()

                if ingreso == "0":
                    break
                

                elif ingreso == "1":
                    continente_buscar = input("Ingrese el continente: ").strip()
                    
                    
                    busqueda = False
                    for p in paises:
                        if normalizar(continente_buscar) in normalizar(p["continente"]):
                            print(f"País: {p['nombre']}")
                            busqueda = True
                            
                    if not busqueda:
                        print("No se encontraron coincidencias.")

                elif ingreso == "2":
                    try:
                        min_pob = int(input("Población mínima: "))
                        max_pob = int(input("Población máxima: "))
                        if min_pob > max_pob:
                            print("Error: La población mínima no puede ser mayor que la máxima.")
                        else:
                            busqueda = False
                            for p in paises:
                                if min_pob <= p["poblacion"] <= max_pob:
                                    print(f"{p['nombre']} - {p['poblacion']}")
                                    busqueda = True

                            if not busqueda:
                                print("No hay países en ese rango.")

                    except ValueError:
                        print("Error: Ingrese solo números enteros para la población.")

                elif ingreso == "3":
                    try:
                        min_sup = int(input("Superficie mínima: "))
                        max_sup = int(input("Superficie máxima: "))
                        if min_sup > max_sup:
                            print("Error: La superficie mínima no puede ser mayor que la máxima.")
                        else:
                            busqueda = False
                            for p in paises:
                                if min_sup <= p["superficie"] <= max_sup:
                                    print(f"{p['nombre']} - {p['superficie']}")
                                    busqueda = True

                            if not busqueda:
                                print("No hay países en ese rango.")

                    except ValueError:
                        print("Error: Ingrese solo números enteros para la superficie.")
                
                else:
                    print("Opción no válida.")

        elif opcion == "5":  # Ordenar por nombre, población o superficie; ascendente o descendente.
            # submenú: el usuario elige criterio y orden; la lista original no se modifica
            while True:
                print("\n--- Ordenar países ---")
                print("1) Por nombre")
                print("2) Por población")
                print("3) Por superficie")
                print("0) Para salir del menú")

                ingreso = input("Opción: ").strip()

                if ingreso == "0":
                    break

                elif ingreso in ("1", "2", "3"):
                    # 1 = de menor a mayor, 2 = de mayor a menor
                    print("1) Ascendente")
                    print("2) Descendente")
                    orden = input("Orden: ").strip()

                    if orden not in ("1", "2"):
                        print("Opción no válida.")
                    elif not paises:
                        print("No hay países cargados.\n")
                    else:
                        # reverse=True en sorted() invierte el orden (descendente)
                        descendente = orden == "2"

                        # sorted() devuelve una lista nueva; paises queda igual que antes
                        if ingreso == "1":
                            # key indica por qué campo comparar; normalizar() ignora mayúsculas y tildes
                            lista_ordenada = sorted(
                                paises,
                                key=lambda p: normalizar(p["nombre"]),
                                reverse=descendente,
                            )
                        elif ingreso == "2":
                            lista_ordenada = sorted(
                                paises,
                                key=lambda p: p["poblacion"],
                                reverse=descendente,
                            )
                        else:
                            lista_ordenada = sorted(
                                paises,
                                key=lambda p: p["superficie"],
                                reverse=descendente,
                            )

                        # muestra el resultado del ordenamiento sin guardarlo en el CSV
                        print("\n--- Listado ordenado ---")
                        for p in lista_ordenada:
                            print(
                                f"{p['nombre']} | Población: {p['poblacion']} | "
                                f"Superficie: {p['superficie']} | Continente: {p['continente']}"
                            )
                        print()

                else:
                    print("Opción no válida.")

        elif opcion == "6":  # Estadísticas (máx/mín población, promedios, cantidad por continente).
            print("\n--- Estadísticas ---")

            if not paises:
                print("No hay países cargados.\n")
            else:
                # se asume el primero como referencia y se compara con el resto
                pais_mayor = paises[0]
                pais_menor = paises[0]
                total_poblacion = 0
                total_superficie = 0

                # en un solo recorrido: máximo, mínimo y sumas para los promedios
                for p in paises:
                    if p["poblacion"] > pais_mayor["poblacion"]:
                        pais_mayor = p
                    if p["poblacion"] < pais_menor["poblacion"]:
                        pais_menor = p
                    total_poblacion += p["poblacion"]
                    total_superficie += p["superficie"]

                # promedio = suma de todos los valores / cantidad de países
                promedio_poblacion = total_poblacion / len(paises)
                promedio_superficie = total_superficie / len(paises)

                print(f"País con mayor población: {pais_mayor['nombre']} ({pais_mayor['poblacion']})")
                print(f"País con menor población: {pais_menor['nombre']} ({pais_menor['poblacion']})")
                print(f"Promedio de población: {promedio_poblacion:.2f}")
                print(f"Promedio de superficie: {promedio_superficie:.2f}")

                print("\nCantidad de países por continente:")
                # diccionario: clave = continente, valor = cuántos países tiene
                cantidad_por_continente = {}
                for p in paises:
                    continente = p["continente"]
                    if continente in cantidad_por_continente:
                        cantidad_por_continente[continente] += 1
                    else:
                        cantidad_por_continente[continente] = 1

                # .items() devuelve cada par continente-cantidad para mostrarlo
                for continente, cantidad in cantidad_por_continente.items():
                    print(f"  {continente}: {cantidad}")

                print()

        else:
            print("Opción inválida.\n")


# Solo ejecuta el menú si este archivo es el punto de entrada
if __name__ == "__main__":
    main()
