"""Archivo que contiene las excepciones personalizadas del sistema."""

class ErrorGeneral(Exception):
    """Excepción base para cualquier error del sistema."""
    pass


class ErrorSoftwareNoEncontrado(ErrorGeneral):
    """Se lanza cuando el software buscado no está en la lista."""
    pass


class ErrorNombreInvalido(ErrorGeneral):
    """Se lanza cuando el nombre ingresado está vacío o es inválido."""
    pass


class ErrorVersionInvalida(ErrorGeneral):
    """Se lanza cuando la versión ingresada es incorrecta o está vacía."""
    pass
