import random
from datetime import datetime
import json

class Alumno:
    def __init__(self, nombre, apellido, segundo_apellido, fecha_nacimiento):
        self.id_alumno = self.generar_id()
        self.nombre = nombre
        self.apellido = apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.notas = {
            "PIMDA": 0,
            "SISIN": 0,
            "ENDES": 0,
            "PROG": 0,
            "LGM": 0,
            "DASP": 0,
            "SASP": 0,
            "INGLÉS": 0,
            "BDD": 0
        }

    def generar_id(self):
        """Genera un ID numérico único de 9 cifras"""
        return random.randint(100000000, 999999999)

    def atributos(self):
        print(f"ID: {self.id_alumno}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Segundo Apellido: {self.segundo_apellido}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento}")

    def es_mayor_de_edad(self):
        try:
            fecha_nacimiento = datetime.strptime(self.fecha_nacimiento, "%Y-%m-%d")
            edad = (datetime.now() - fecha_nacimiento).days // 365
            return edad >= 18
        except ValueError:
            print("Usa YYYY-MM-DD.")
            return False

    def poner_notas(self, asignatura, nota):
        if asignatura in self.notas:
            self.notas[asignatura] = nota
        else:
            print(f"La asignatura {asignatura} no existe")

    def mostrar_notas(self):
        if self.notas:
            print("Notas del alumno:")
            for asignatura, nota in self.notas.items():
                estado = nota if nota is not None else "Sin asignar"
                print(f"{asignatura}: {estado}")
        else:
            print("No hay notas asignadas")

def mostrar_datos_y_mayoria(alumno):
    alumno.atributos()
    print("Es mayor de edad?:", "Sí" if alumno.es_mayor_de_edad() else "No")
    print()


def asignar_notas(lista_alumnos):
    if not lista_alumnos:
        print("La lista de alumnos está vacía")
        return
    
    while True:
        alumno = buscar_alumno_por_nombre(lista_alumnos)
        if alumno:
            print(f"\nIngresando notas para: {alumno.nombre} {alumno.apellido}")
            for asignatura in alumno.notas.keys():
                while True:
                    try:
                        nota = input(f"Ingrese la nota para {asignatura} (entre 0 y 10): ")
                        if nota.strip() == "":
                            print(f"{asignatura} omitida.")
                            break
                        nota = float(nota)
                        if 0 <= nota <= 10:
                            alumno.poner_notas(asignatura, nota)
                            break
                        else:
                            print("La nota debe estar entre 0 y 10.")
                    except ValueError:
                        print("Nota no válida. Por favor ingresa un número.")

            continuar = input("¿Deseas asignar notas a otro alumno? (sí/no): ").lower()
            if continuar != "sí":
                print("Terminando la asignación de notas.")
                break
        else:
            print("Alumno no encontrado.")
            continuar = input("¿Deseas intentar con otro alumno? (sí/no): ").lower()
            if continuar != "sí":
                break

def buscar_alumno_por_nombre(lista_alumnos):
    if not lista_alumnos:
        print("No hay alumnos en la lista.")
        return None
    nombre = input("\nEscribe el nombre del alumno: ")
    for alumno in lista_alumnos:
        if alumno.nombre.lower() == nombre.lower():
            return alumno
    print("Alumno no encontrado.")
    return None

def guardar_datos_json(lista_alumnos):
    """Guarda los datos de los alumnos en un archivo JSON."""
    datos = {}
    for alumno in lista_alumnos:
        datos[alumno.id_alumno] = {
            "nombre": alumno.nombre,
            "apellido": alumno.apellido,
            "segundo_apellido": alumno.segundo_apellido,
            "fecha_nacimiento": alumno.fecha_nacimiento,
            "notas": alumno.notas
        }
    
    with open("alumnos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print("Datos guardados en alumnos.json.")

alumnos = [
    Alumno("Juan", "Pérez", "González", "2005-08-15"),
    Alumno("María", "López", "Ramírez", "2002-05-22"),
    Alumno("Carlos", "Hernández", "Martínez", "2010-03-10"),
    Alumno("Miguel", "Angel", "Fuentes", "2002-07-07"),
    Alumno("Fran", "Sánchez", "García", "2002-07-07"), 

]

print("Datos de los alumnos:")
for alumno in alumnos:
    mostrar_datos_y_mayoria(alumno)


asignar_notas(alumnos)
guardar_datos_json(alumnos)
