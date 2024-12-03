import json
from Clases_Alumno import Alumno

ARCHIVO_JSON = "alumnos.json"


def cargar_datos():
    """Carga los datos desde el archivo JSON."""
    try:
        with open(ARCHIVO_JSON, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. Se iniciará con datos vacíos.")
        return {}


def guardar_datos(datos):
    """Guarda los datos en el archivo JSON."""
    with open(ARCHIVO_JSON, "w") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print(f"Datos guardados en {ARCHIVO_JSON}.")


def alumno_a_dict(alumno):
    """Convierte un objeto Alumno a un diccionario."""
    return {
        "nombre": alumno.nombre,
        "apellido": alumno.apellido,
        "segundo_apellido": alumno.segundo_apellido,
        "fecha_nacimiento": alumno.fecha_nacimiento,
        "notas": alumno.notas,
    }


def agregar_alumno(id_alumno, alumno):
    """Agrega un alumno al archivo JSON."""
    datos = cargar_datos()
    if id_alumno in datos:
        print(f"El ID {id_alumno} ya está registrado.")
    else:
        datos[id_alumno] = alumno_a_dict(alumno)
        guardar_datos(datos)


alumnos = [
    Alumno("Juan", "Pérez", "González", "2005-08-15"),
    Alumno("María", "López", "Ramírez", "2002-05-22"),
    Alumno("Carlos", "Hernández", "Martínez", "2010-03-10"),
    Alumno("Miguel", "Angel", "Fuentes", "2002-07-07"), 
]


for alumno in alumnos:
    agregar_alumno(alumno.id_alumno, alumno)
