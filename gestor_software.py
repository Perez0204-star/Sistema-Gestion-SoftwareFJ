"""Módulo que maneja toda la lógica del sistema de gestión de software."""

import json  # Permite trabajar con archivos JSON
import os    # Permite validar rutas y existencia de archivos

from excepciones import (
    ErrorSoftwareNoEncontrado,
    ErrorNombreInvalido,
    ErrorVersionInvalida
)

class GestorSoftware:
    """Clase encargada de gestionar los registros de software."""

    def __init__(self, ruta_archivo):
        """Constructor que recibe la ruta del archivo donde se guardan los datos."""
        self.ruta_archivo = ruta_archivo  # Guarda la ruta del archivo JSON

        # Verifica si el archivo existe; si no existe, lo crea vacío.
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, "w") as archivo:
                json.dump([], archivo)  # Crea una lista vacía en el archivo

    def cargar_datos(self):
        """Carga y retorna el contenido del archivo JSON."""
        with open(self.ruta_archivo, "r") as archivo:
            return json.load(archivo)  # Retorna la lista de software guardado

    def guardar_datos(self, datos):
        """Guarda la lista de software en el archivo JSON."""
        with open(self.ruta_archivo, "w") as archivo:
            json.dump(datos, archivo, indent=4)  # Guarda con formato bonito

    def agregar_software(self, nombre, version):
        """Agrega un nuevo software al archivo."""

        if not nombre:
            raise ErrorNombreInvalido("El nombre del software no puede estar vacío.")

        if not version:
            raise ErrorVersionInvalida("La versión del software no puede estar vacía.")

        datos = self.cargar_datos()  # Carga lista actual
        nuevo_registro = {"nombre": nombre, "version": version}  # Crea diccionario

        datos.append(nuevo_registro)  # Agrega a la lista
        self.guardar_datos(datos)     # Guarda cambios en el archivo

    def buscar_software(self, nombre):
        """Busca un software por nombre y lo retorna si existe."""

        datos = self.cargar_datos()  # Carga los registros

        # Recorre cada software
        for software in datos:
            if software["nombre"].lower() == nombre.lower():
                return software  # Retorna si hay coincidencia

        # Si no se encontró, lanza excepción
        raise ErrorSoftwareNoEncontrado(f"No se encontró el software: {nombre}")

    def listar_software(self):
        """Retorna una lista con todo el software registrado."""
        return self.cargar_datos()  # Simplemente devuelve la lista completa
