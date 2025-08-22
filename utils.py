"""
Utilidades para el organizador de órdenes de compra.
"""

import os
import re
import subprocess
import platform
from pathlib import Path
from typing import Optional

from config import Config


def clean_filename(name: str) -> str:
    """
    Limpia el nombre del archivo/carpeta removiendo caracteres no válidos.
    
    Args:
        name: Nombre a limpiar
        
    Returns:
        Nombre limpio sin caracteres problemáticos
    """
    if not name or name == 'nan':
        return "Sin_nombre"
    
    # Reemplaza caracteres problemáticos por guiones bajos
    cleaned = re.sub(r'[<>:"/\\|?*]', '_', str(name))
    
    # Remueve espacios extra y los reemplaza por uno solo
    cleaned = ' '.join(cleaned.split())
    
    return cleaned.strip() or "Sin_nombre"


def safe_str_conversion(value) -> str:
    """
    Convierte un valor a string de forma segura.
    
    Args:
        value: Valor a convertir
        
    Returns:
        String limpio
    """
    if value is None or str(value).lower() == 'nan':
        return "No_especificado"
    
    return str(value).strip()


def open_folder_in_explorer(folder_path: str) -> bool:
    """
    Abre una carpeta en el explorador de archivos del sistema.
    
    Args:
        folder_path: Ruta de la carpeta a abrir
        
    Returns:
        True si se abrió correctamente, False en caso contrario
    """
    try:
        system = platform.system()
        
        if system == "Windows":
            os.startfile(folder_path)
        elif system == "Darwin":  # macOS
            subprocess.run(["open", folder_path], check=True)
        else:  # Linux y otros
            subprocess.run(["xdg-open", folder_path], check=True)
            
        return True
        
    except Exception as e:
        print(f"No se pudo abrir la carpeta: {e}")
        return False


def count_pdf_files(directory: str) -> int:
    """
    Cuenta los archivos PDF en un directorio.
    
    Args:
        directory: Ruta del directorio
        
    Returns:
        Número de archivos PDF encontrados
    """
    try:
        return len(list(Path(directory).glob(f"*{Config.PDF_EXTENSION}")))
    except Exception:
        return 0


def ensure_directory_exists(directory_path: Path) -> None:
    """
    Asegura que un directorio exista, creándolo si es necesario.
    
    Args:
        directory_path: Ruta del directorio
    """
    directory_path.mkdir(parents=True, exist_ok=True)


def get_user_confirmation(prompt: str, default: str = 'n') -> bool:
    """
    Obtiene confirmación del usuario.
    
    Args:
        prompt: Mensaje a mostrar
        default: Valor por defecto
        
    Returns:
        True si el usuario confirma, False en caso contrario
    """
    try:
        response = input(prompt).lower().strip()
        if not response:
            response = default
            
        return response in ['s', 'si', 'y', 'yes']
    except (KeyboardInterrupt, EOFError):
        return False