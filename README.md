# Trabajo Práctico Integrador — Programación I

**Carrera:** Tecnicatura Universitaria en Programación a Distancia (UTN)  
**Materia:** Programación I  
**Tema:** Gestión de datos de países en Python (filtros, ordenamientos y estadísticas)

## Integrantes

- Schnaible Nadia
- Traficante Leandro

## Descripción

Aplicación de consola desarrollada en Python 3 que gestiona información de países: **nombre**, **población**, **superficie (km²)** y **continente**. Los datos se cargan desde un archivo CSV, se mantienen en memoria como una lista de diccionarios y se pueden consultar, filtrar, ordenar y analizar mediante un menú interactivo.

El programa valida entradas del usuario, muestra mensajes claros de éxito o error y persiste los cambios (altas y actualizaciones) en `paises.csv`.

## Requisitos

- Python 3.x
- Archivo `paises.csv` en la misma carpeta que el script (incluido en el repositorio)

## Cómo ejecutar

Desde la carpeta del proyecto (o desde cualquier ruta; el programa ubica el CSV automáticamente):

```bash
python main_schnaible.py
```

Al iniciar, se muestra la cantidad de países cargados y el menú principal.

## Menú principal

| Opción | Función                                                               |
| ------ | --------------------------------------------------------------------- |
| 1      | Agregar un país (todos los campos obligatorios)                       |
| 2      | Actualizar población y superficie de un país existente                |
| 3      | Buscar país por nombre (coincidencia parcial o exacta)                |
| 4      | Filtrar por continente, rango de población o rango de superficie      |
| 5      | Ordenar por nombre, población o superficie (ascendente o descendente) |
| 6      | Mostrar estadísticas del dataset                                      |
| 0      | Salir                                                                 |

## Archivos del proyecto

| Archivo             | Rol                                  |
| ------------------- | ------------------------------------ |
| `main_schnaible.py` | Programa principal (menú y lógica)   |
| `paises.csv`        | Dataset base y persistencia de datos |

## Ejemplos de uso

### Inicio

```
Gestión de datos de países — sistema iniciado
Países cargados en memoria: 10

--- Menú ---
1) Agregar país
...
Opción: 3
```

### Buscar país (opción 3)

Entrada: `arg`  
Salida (ejemplo):

```
País encontrado:
Nombre: Argentina
Población: 45376763
Superficie: 2780400
Continente: América
```

### Filtrar por continente (opción 4 → 1)

Entrada: `america`  
Salida (ejemplo): lista de países cuyo continente coincide (sin distinguir mayúsculas ni tildes).

### Ordenar por población descendente (opción 5 → 2 → 2)

Salida (ejemplo): listado ordenado de mayor a menor población, sin modificar el archivo CSV.

### Estadísticas (opción 6)

Salida (ejemplo):

```
País con mayor población: China (1412000000)
País con menor población: Australia (26100000)
Promedio de población: ...
Promedio de superficie: ...

Cantidad de países por continente:
  América: 4
  Asia: 2
  ...
```

### Validaciones (ejemplos)

- Campos vacíos al agregar: `Error: Todos los campos deben estar completos.`
- Población o superficie ≤ 0: `Error: La población debe ser mayor que cero.`
- País duplicado: `El país '...' ya existe.`
- Rango inválido en filtros: `Error: La población mínima no puede ser mayor que la máxima.`

## Estructura del CSV

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
...
```

## Enlaces (completar al entregar)

- **Repositorio GitHub:** https://github.com/leandrotraficante/UTN-TUPaD-P1-TPI-Schnaible-Traficante
- **Video demostración (10–15 min, público):** https://youtu.be/8om5lKeMwEs

