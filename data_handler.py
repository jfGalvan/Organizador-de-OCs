"""
Manejo de datos para el organizador de órdenes de compra.
"""

from pathlib import Path
from typing import Dict, List, Tuple
import pandas as pd

from config import Config
from exceptions import DataFileError, MissingColumnsError
from utils import safe_str_conversion


class DataHandler:
    """Maneja la lectura y validación de archivos de datos."""
    
    def __init__(self, file_path: str):
        """
        Inicializa el manejador de datos.
        
        Args:
            file_path: Ruta al archivo de datos
        """
        self.file_path = Path(file_path)
        self.dataframe: pd.DataFrame = None
        
    def load_data(self) -> pd.DataFrame:
        """
        Carga los datos del archivo.
        
        Returns:
            DataFrame con los datos cargados
            
        Raises:
            DataFileError: Si hay un error al cargar el archivo
        """
        try:
            if self.file_path.suffix.lower() == '.csv':
                self.dataframe = pd.read_csv(self.file_path)
            elif self.file_path.suffix.lower() in ['.xlsx', '.xls']:
                self.dataframe = pd.read_excel(self.file_path)
            else:
                raise DataFileError(f"Formato de archivo no soportado: {self.file_path.suffix}")
            
            print(f"Archivo leído correctamente. Registros encontrados: {len(self.dataframe)}")
            return self.dataframe
            
        except Exception as e:
            raise DataFileError(f"Error al leer el archivo {self.file_path}: {str(e)}")
    
    def validate_columns(self) -> None:
        """
        Valida que el archivo tenga las columnas requeridas.
        
        Raises:
            MissingColumnsError: Si faltan columnas requeridas
        """
        if self.dataframe is None:
            self.load_data()
        
        missing_columns = [
            col for col in Config.REQUIRED_COLUMNS 
            if col not in self.dataframe.columns
        ]
        
        if missing_columns:
            raise MissingColumnsError(missing_columns)
    
    def get_data_preview(self) -> Dict:
        """
        Obtiene una vista previa de los datos.
        
        Returns:
            Diccionario con información estadística de los datos
        """
        if self.dataframe is None:
            self.load_data()
        
        return {
            'total_records': len(self.dataframe),
            'columns': list(self.dataframe.columns),
            'unique_requesters': self.dataframe['Nombre del Solicitante'].nunique(),
            'unique_suppliers': self.dataframe['Name'].nunique(),
            'unique_locations': self.dataframe['Memo'].nunique() if 'Memo' in self.dataframe.columns else 0
        }
    
    def get_processed_records(self) -> List[Tuple[str, str, str, str]]:
        """
        Obtiene los registros procesados para la organización.
        
        Returns:
            Lista de tuplas (ubicación, solicitante, factura, proveedor)
        """
        if self.dataframe is None:
            self.load_data()
        
        self.validate_columns()
        
        records = []
        for _, row in self.dataframe.iterrows():
            ubicacion = safe_str_conversion(row['Memo'])
            solicitante = safe_str_conversion(row['Nombre del Solicitante'])
            factura = safe_str_conversion(row['Factura'])
            proveedor = safe_str_conversion(row['Name'])
            
            records.append((ubicacion, solicitante, factura, proveedor))
        
        return records
    
    def print_preview(self) -> None:
        """Imprime una vista previa de los datos."""
        try:
            preview = self.get_data_preview()
            
            print("=== VISTA PREVIA DE DATOS ===")
            print(f"Total de registros: {preview['total_records']}")
            print(f"Columnas encontradas: {preview['columns']}")
            print(f"\nEstadísticas:")
            print(f"- Solicitantes únicos: {preview['unique_requesters']}")
            print(f"- Proveedores únicos: {preview['unique_suppliers']}")
            print(f"- Ubicaciones únicas: {preview['unique_locations']}")
            
        except Exception as e:
            print(f"❌ Error al mostrar vista previa: {str(e)}")
            raise