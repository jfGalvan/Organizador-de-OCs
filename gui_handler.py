"""
Manejo de la interfaz gráfica para selección de archivos y carpetas.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from typing import Tuple, Optional

from config import Config
from exceptions import UserCancellationError
from utils import count_pdf_files


class GUIHandler:
    """Maneja la interfaz gráfica para selección de archivos."""
    
    def __init__(self):
        """Inicializa el manejador de GUI."""
        self.root = None
    
    def _initialize_root(self) -> None:
        """Inicializa la ventana root de tkinter."""
        if self.root is None:
            self.root = tk.Tk()
            self.root.withdraw()  # Ocultar ventana principal
    
    def _cleanup_root(self) -> None:
        """Limpia y destruye la ventana root."""
        if self.root:
            try:
                self.root.destroy()
                self.root = None
            except:
                pass
    
    def select_data_file(self) -> str:
        """
        Permite al usuario seleccionar el archivo de datos.
        
        Returns:
            Ruta del archivo seleccionado
            
        Raises:
            UserCancellationError: Si el usuario cancela la operación
        """
        self._initialize_root()
        
        print(Config.UI_MESSAGES['select_data_file'])
        
        file_path = filedialog.askopenfilename(
            title="Selecciona el archivo con los datos",
            filetypes=Config.SUPPORTED_DATA_FILES
        )
        
        if not file_path:
            raise UserCancellationError("No se seleccionó archivo de datos")
        
        print(Config.UI_MESSAGES['file_selected'].format(Path(file_path).name))
        return file_path
    
    def select_pdf_directory(self) -> str:
        """
        Permite al usuario seleccionar el directorio con PDFs.
        
        Returns:
            Ruta del directorio seleccionado
            
        Raises:
            UserCancellationError: Si el usuario cancela la operación
        """
        print(f"\n{Config.UI_MESSAGES['select_pdf_folder']}")
        
        directory = filedialog.askdirectory(
            title="Selecciona la carpeta con los PDFs originales"
        )
        
        if not directory:
            raise UserCancellationError("No se seleccionó directorio de PDFs")
        
        pdf_count = count_pdf_files(directory)
        print(Config.UI_MESSAGES['folder_selected'].format(Path(directory).name))
        print(Config.UI_MESSAGES['pdfs_found'].format(pdf_count))
        
        return directory
    
    def select_output_directory(self) -> str:
        """
        Permite al usuario seleccionar el directorio de salida.
        
        Returns:
            Ruta del directorio de salida (con subdirectorio creado)
            
        Raises:
            UserCancellationError: Si el usuario cancela la operación
        """
        print(f"\n{Config.UI_MESSAGES['select_output_folder']}")
        
        directory = filedialog.askdirectory(
            title="Selecciona la carpeta donde crear la estructura organizada"
        )
        
        if not directory:
            raise UserCancellationError("No se seleccionó directorio de salida")
        
        # Crear subdirectorio para la organización
        output_path = Path(directory) / Config.OUTPUT_FOLDER_NAME
        print(Config.UI_MESSAGES['output_folder'].format(output_path))
        
        return str(output_path)
    
    def select_files_and_directories(self) -> Tuple[str, str, str]:
        """
        Permite al usuario seleccionar todos los archivos y directorios necesarios.
        
        Returns:
            Tupla con (archivo_datos, directorio_pdfs, directorio_salida)
            
        Raises:
            UserCancellationError: Si el usuario cancela cualquier selección
        """
        print("=== SELECCIÓN DE ARCHIVOS Y CARPETAS ===\n")
        
        try:
            # Seleccionar archivo de datos
            data_file = self.select_data_file()
            
            # Seleccionar directorio de PDFs
            pdf_directory = self.select_pdf_directory()
            
            # Seleccionar directorio de salida
            output_directory = self.select_output_directory()
            
            return data_file, pdf_directory, output_directory
            
        except UserCancellationError:
            print(Config.UI_MESSAGES['operation_cancelled'])
            raise
        except Exception as e:
            error_msg = f"Error en la selección: {str(e)}"
            messagebox.showerror("Error", error_msg)
            raise UserCancellationError(error_msg)
        finally:
            self._cleanup_root()
    
    def show_error(self, title: str, message: str) -> None:
        """
        Muestra un mensaje de error en una ventana.
        
        Args:
            title: Título del mensaje
            message: Contenido del mensaje
        """
        self._initialize_root()
        try:
            messagebox.showerror(title, message)
        finally:
            self._cleanup_root()
    
    def show_info(self, title: str, message: str) -> None:
        """
        Muestra un mensaje informativo en una ventana.
        
        Args:
            title: Título del mensaje
            message: Contenido del mensaje
        """
        self._initialize_root()
        try:
            messagebox.showinfo(title, message)
        finally:
            self._cleanup_root()