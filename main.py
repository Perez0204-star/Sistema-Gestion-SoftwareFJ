"""Archivo principal del sistema de gestión."""

from gestor_software import GestorSoftware  # Importa la clase principal
from excepciones import (                   # Importa excepciones personalizadas
    ErrorGeneral,
    ErrorSoftwareNoEncontrado,
    ErrorNombreInvalido,
    ErrorVersionInvalida
)

def mostrar_menu():
    """Muestra el menú principal en pantalla."""
    print("\n=== Sistema de Gestión de Software ===")
    print("1. Agregar software")
    print("2. Buscar software")
    print("3. Listar todos")
    print("4. Salir")

def main():
    """Función principal del programa."""
    gestor = GestorSoftware("datos/software.json")  # Crea el gestor con la ruta del archivo

    while True:
        mostrar_menu()  # Muestra el menú en cada ciclo
        opcion = input("Seleccione una opción: ")  # Pide la opción al usuario

        try:
            if opcion == "1":
                nombre = input("Nombre del software: ")  # Pide nombre
                version = input("Versión del software: ")  # Pide versión
                gestor.agregar_software(nombre, version)  # Llama método para agregar
                print("Software agregado correctamente.")

            elif opcion == "2":
                nombre = input("Nombre del software a buscar: ")
                resultado = gestor.buscar_software(nombre)  # Busca el software
                print("Resultado encontrado:", resultado)

            elif opcion == "3":
                lista = gestor.listar_software()  # Obtiene la lista completa
                print("Listado de software:", lista)

            elif opcion == "4":
                print("Saliendo del sistema...")
                break  # Termina el bucle y cierra el programa

            else:
                print("Opción no válida. Intente de nuevo.")

        except ErrorGeneral as e:
            print("Ocurrió un error:", str(e))

if __name__ == "__main__":
    main()  # Llama la función principal
