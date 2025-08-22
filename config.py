"""
Configuración para el organizador de órdenes de compra.
"""

from typing import List

class Config:
    """Configuración de la aplicación."""
    # Columnas requeridas en el archivo de datos
    REQUIRED_COLUMNS: List[str] = [
        'Nombre del Solicitante', 
        'Factura', 
        'Name', 
        'Memo'
    ]
    # Tipos de archivo soportados
    SUPPORTED_DATA_FILES = [
        ("Archivos Excel", "*.xlsx *.xls"),
        ("Archivos CSV", "*.csv"),
        ("Todos los archivos", "*.*")
    ]
    # Configuración de directorios
    OUTPUT_FOLDER_NAME = "ordenes_organizadas"
    # Configuración de archivos
    PDF_EXTENSION = ".pdf"
    # Configuración de UI
    UI_MESSAGES = {
        'select_data_file': "1. Selecciona el archivo con los datos (CSV o Excel)...",
        'select_pdf_folder': "2. Selecciona la carpeta donde están los PDFs originales...",
        'select_output_folder': "3. Selecciona donde quieres crear la estructura organizada...",
        'operation_cancelled': "❌ Operación cancelada por el usuario",
        'file_selected': "✅ Archivo seleccionado: {}",
        'folder_selected': "✅ Carpeta seleccionada: {}",
        'pdfs_found': "   PDFs encontrados: {}",
        'output_folder': "✅ Carpeta de destino: {}",
        'process_completed': "✅ PROCESO COMPLETADO",
        'check_folder': "Revisa la carpeta organizada en: {}",
        'open_folder_prompt': "¿Deseas abrir la carpeta de resultados? (s/n): "
    }
