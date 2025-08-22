#!/usr/bin/env python3
"""
Aplicación principal para organizar órdenes de compra en PDF.

Este programa ayuda a organizar archivos PDF de órdenes de compra
en una estructura de carpetas basada en solicitantes y proveedores.
"""

import sys
from pathlib import Path

from config import Config
from data_handler import DataHandler
from file_organizer import FileOrganizer
from gui_handler import GUIHandler
from exceptions import (
    FileOrganizerError, 
    DataFileError, 
    MissingColumnsError,
    UserCancellationError
)
from utils import open_folder_in_explorer, get_user_confirmation


class PurchaseOrderOrganizer:
    """Aplicación principal para organizar órdenes de compra."""
    
    def __init__(self):
        """Inicializa la aplicación."""
        self.gui = GUIHandler()
        self.data_handler: DataHandler = None
        self.organizer: FileOrganizer = None
    
    def _print_welcome_message(self) -> None:
        """Imprime el mensaje de bienvenida."""
        print("=== ORGANIZADOR DE ÓRDENES DE COMPRA ===")
        print("Este programa te ayudará a organizar tus órdenes de compra")
        print("en carpetas por ubicación, solicitante y proveedor.\n")
    
    def _validate_data_file(self, file_path: str) -> bool:
        """
        Valida el archivo de datos y muestra vista previa.
        
        Args:
            file_path: Ruta al archivo de datos
            
        Returns:
            True si el archivo es válido, False en caso contrario
        """
        try:
            self.data_handler = DataHandler(file_path)
            self.data_handler.load_data()
            self.data_handler.validate_columns()
            self.data_handler.print_preview()
            return True
            
        except MissingColumnsError as e:
            print(f"\n❌ ERROR: {e}")
            print("El archivo debe contener estas columnas:")
            for col in Config.REQUIRED_COLUMNS:
                print(f"  - {col}")
            return False
            
        except DataFileError as e:
            print(f"\n❌ ERROR: {e}")
            return False
    
    def _execute_organization(self, data_file: str, pdf_dir: str, output_dir: str) -> bool:
        """
        Ejecuta el proceso de organización.
        
        Args:
            data_file: Archivo con los datos
            pdf_dir: Directorio con PDFs
            output_dir: Directorio de salida
            
        Returns:
            True si se completó exitosamente, False en caso contrario
        """
        try:
            print(f"\n=== INICIANDO ORGANIZACIÓN ===")
            print(f"📄 Archivo de datos: {Path(data_file).name}")
            print(f"📁 Carpeta PDFs: {Path(pdf_dir).name}")
            print(f"📁 Carpeta destino: {output_dir}")
            print("-" * 50)
            
            # Crear organizador y ejecutar
            self.organizer = FileOrganizer(data_file, pdf_dir, output_dir)
            stats = self.organizer.organize_files()
            
            # Mostrar resultados
            self.organizer.print_summary()
            self.organizer.print_directory_structure()
            
            print(f"\n{Config.UI_MESSAGES['process_completed']}")
            print(Config.UI_MESSAGES['check_folder'].format(output_dir))
            
            return True
            
        except FileOrganizerError as e:
            print(f"\n❌ ERROR: {e}")
            return False
    
    def _offer_to_open_folder(self, output_dir: str) -> None:
        """
        Ofrece al usuario abrir la carpeta de resultados.
        
        Args:
            output_dir: Directorio de salida
        """
        try:
            if get_user_confirmation(Config.UI_MESSAGES['open_folder_prompt']):
                if open_folder_in_explorer(output_dir):
                    print("📂 Carpeta abierta exitosamente")
                else:
                    print("⚠️  No se pudo abrir la carpeta automáticamente")
        except Exception:
            pass  # Ignorar errores al abrir carpeta
    
    def run(self) -> None:
        """Ejecuta la aplicación principal."""
        try:
            # Mensaje de bienvenida
            self._print_welcome_message()
            
            # Seleccionar archivos y directorios
            data_file, pdf_dir, output_dir = self.gui.select_files_and_directories()
            
            # Validar archivo de datos
            if not self._validate_data_file(data_file):
                print("\n❌ Operación cancelada debido a errores en el archivo")
                return
            
            # Ejecutar organización
            if self._execute_organization(data_file, pdf_dir, output_dir):
                # Ofrecer abrir carpeta de resultados
                self._offer_to_open_folder(output_dir)
            else:
                print("\n❌ La organización no se completó correctamente")
        
        except UserCancellationError:
            print(Config.UI_MESSAGES['operation_cancelled'])
        
        except KeyboardInterrupt:
            print("\n❌ Operación interrumpida por el usuario")
        
        except Exception as e:
            print(f"\n❌ Error inesperado: {str(e)}")
            print("Por favor, verifica los archivos y vuelve a intentar")


def main():
    """Punto de entrada principal de la aplicación."""
    app = PurchaseOrderOrganizer()
    app.run()


if __name__ == "__main__":
    main()
        