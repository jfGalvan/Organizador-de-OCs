"""
Organizador de Órdenes de Compra

Un sistema modular para organizar archivos PDF de órdenes de compra
en estructuras de directorios basadas en ubicación, solicitante y proveedor.
"""

__version__ = "2.0.0"
__author__ = "Tu Nombre"
__email__ = "tu.email@ejemplo.com"

# Importaciones principales para facilitar el uso del paquete
from main import PurchaseOrderOrganizer, main
from file_organizer import FileOrganizer
from data_handler import DataHandler
from gui_handler import GUIHandler
from config import Config

# Excepciones principales
from exceptions import (
    FileOrganizerError,
    DataFileError,
    MissingColumnsError,
    PDFDirectoryError,
    OutputDirectoryError,
    UserCancellationError
)

__all__ = [
    'PurchaseOrderOrganizer',
    'FileOrganizer', 
    'DataHandler',
    'GUIHandler',
    'Config',
    'main',
    # Excepciones
    'FileOrganizerError',
    'DataFileError',
    'MissingColumnsError',
    'PDFDirectoryError',
    'OutputDirectoryError',
    'UserCancellationError'
]