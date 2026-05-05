# TP Integrador - Programación I
import csv
import unicodedata # esta biblioteca permite manipular tildes, símbolos y caracteres especiales de manera uniforme en cadenas de texto.

def normalizar(texto): # función para sacar acentos 
    texto = texto.lower().strip()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto


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

        elif opcion == "1": # Agregar país
            print("\n--- Registrar Nuevo País ---")
            
           # se pide y se valida el nombre
            nombre_nuevo = input("Ingrese el nombre del país: ").strip()
            if not nombre_nuevo:
                print("Error: El nombre es obligatorio.")
            else:
                # Verifica que el pais no se encuentre en la lista
                existe = False
                for p in paises:
                    if p["nombre"].lower() == nombre_nuevo.lower():
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
                            # si los datos los fueron ingresados correctamente
                            poblacion_nuevo = int(pob_input)
                            superficie_nuevo = int(sup_input)

                            # se guarda en el diccionario
                            nuevo_pais = {
                                "nombre": nombre_nuevo,
                                "poblacion": poblacion_nuevo,
                                "superficie": superficie_nuevo,
                                "continente": continente_nuevo
                            }
                            
                            paises.append(nuevo_pais)
                            with open("paises.csv", "a", newline="", encoding="utf-8") as archivo:
                                escritor = csv.writer(archivo)
                                escritor.writerow([nombre_nuevo, poblacion_nuevo, superficie_nuevo, continente_nuevo])
                            
                            print("El país se agregó correctamente.\n")

                    except ValueError:
                        print("Error: La población y superficie deben ser números enteros.")
            
            

        elif opcion == "2":# Actualizar solo población y superficie de un país identificado.
            try:
            
                print("\n--- Actualizar datos de Población y Superficie de un país ---")
                nombre_actualizar= input("Ingrese el nombre del país a actualizar: ")
            # verifica que el pais  este en la lista
                encontrado = False
                for p in paises:
                    if p["nombre"].strip().lower() == nombre_actualizar.lower():
                        encontrado = True
                        
                        
                        p["poblacion"] = int(input("Nueva población: "))
                        p["superficie"] = int(input("Nueva superficie: "))
                        break
                
                if not encontrado:
                        print (f"El país {nombre_actualizar} no se encuentra en la lista.")
                    
                else: # reescribe la info en el archivo
                    with open("paises.csv", "w",newline="", encoding="utf-8") as archivo:
                        escritor = csv.writer(archivo)
                        escritor.writerow(["nombre", "poblacion", "superficie", "continente"])        

                        for p in paises:
                            escritor.writerow([
                            p["nombre"],
                            p["poblacion"],
                            p["superficie"],
                            p["continente"]
                            ])    
                        
                        print("Los datos se actualizaron correctamente.\n")
                        
                        
                        
            except ValueError:
                print("Error: La población y la superficie deben ser números enteros.\n")

        elif opcion == "3": # Búsqueda por nombre (coincidencia parcial o exacta).
            try: 
                print("\n--- Busque un país por su nombre ---")
                nombre_buscar = input("Ingrese el país que quiere buscar: ").strip()
                
                busqueda= False
                for p in paises:
                    if nombre_buscar in p["nombre"].lower(): # de esta manera la busqueda puede ser parcial
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
