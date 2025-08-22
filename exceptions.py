"""

"""


class FileOrganizerError(Exception):
    """Excepción base para errores del organizador de archivos."""
    pass


class DataFileError(FileOrganizerError):
    """Error relacionado con el archivo de datos."""
    pass


class MissingColumnsError(DataFileError):
    """Error cuando faltan columnas requeridas en el archivo de datos."""
    
    def __init__(self, missing_columns):
        self.missing_columns = missing_columns
        super().__init__(f"Faltan columnas requeridas: {missing_columns}")


class PDFDirectoryError(FileOrganizerError):
    """Error relacionado con el directorio de PDFs."""
    pass


class OutputDirectoryError(FileOrganizerError):
    """Error relacionado con el directorio de salida."""
    pass


class UserCancellationError(FileOrganizerError):
    """Error cuando el usuario cancela la operación."""
    pass