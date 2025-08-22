"""
Organizador principal de archivos PDF.
"""

import shutil
from pathlib import Path
from typing import NamedTuple, List
from dataclasses import dataclass

from config import Config
from data_handler import DataHandler
from exceptions import PDFDirectoryError, OutputDirectoryError
from utils import clean_filename, ensure_directory_exists, count_pdf_files

@dataclass
class OrganizationStats:
    """Estadísticas del proceso de organización."""
    folders_created: int = 0
    files_moved: int = 0
    files_not_found: int = 0
    total_records: int = 0

class PDFRecord(NamedTuple):
    """Representa un registro de PDF a organizar."""
    location: str
    requester: str
    invoice: str
    supplier: str

class FileOrganizer:
    """Organizador principal de archivos PDF."""
    def __init__(self, data_file_path: str, pdf_directory: str, output_directory: str):
        self.data_handler = DataHandler(data_file_path)
        self.pdf_directory = Path(pdf_directory)
        self.output_directory = Path(output_directory)
        self.stats = OrganizationStats()
        self._validate_directories()
    def _validate_directories(self) -> None:
        if not self.pdf_directory.exists():
            raise PDFDirectoryError(f"El directorio de PDFs no existe: {self.pdf_directory}")
        if not self.pdf_directory.is_dir():
            raise PDFDirectoryError(f"La ruta de PDFs no es un directorio: {self.pdf_directory}")
        try:
            ensure_directory_exists(self.output_directory)
        except Exception as e:
            raise OutputDirectoryError(f"No se pudo crear el directorio de salida: {e}")
    def _create_directory_structure(self, record: PDFRecord) -> Path:
        location = clean_filename(record.location)
        requester = clean_filename(record.requester)
        supplier = clean_filename(record.supplier)
        location_path = self.output_directory / location
        requester_path = location_path / requester
        supplier_path = requester_path / supplier
        for path, name in [
            (location_path, f"📁 {location}"),
            (requester_path, f"  📁 {location}/{requester}"),
            (supplier_path, f"    📁 {location}/{requester}/{supplier}")
        ]:
            if not path.exists():
                ensure_directory_exists(path)
                print(f"Carpeta creada: {name}")
                self.stats.folders_created += 1
        return supplier_path
    def _copy_pdf_file(self, record: PDFRecord, destination_path: Path) -> bool:
        pdf_filename = f"{record.invoice}{Config.PDF_EXTENSION}"
        source_pdf = self.pdf_directory / pdf_filename
        destination_pdf = destination_path / pdf_filename
        if source_pdf.exists():
            try:
                shutil.copy2(source_pdf, destination_pdf)
                location_clean = clean_filename(record.location)
                requester_clean = clean_filename(record.requester)
                supplier_clean = clean_filename(record.supplier)
                print(f"      📄 Archivo copiado: {pdf_filename} -> "
                      f"{location_clean}/{requester_clean}/{supplier_clean}/")
                self.stats.files_moved += 1
                return True
            except Exception as e:
                print(f"      ❌ Error al copiar {pdf_filename}: {str(e)}")
                return False
        else:
            print(f"      ❓ Archivo no encontrado: {pdf_filename}")
            self.stats.files_not_found += 1
            return False
    def organize_files(self) -> OrganizationStats:
        print("=== INICIANDO ORGANIZACIÓN ===")
        records_data = self.data_handler.get_processed_records()
        self.stats.total_records = len(records_data)
        for location, requester, invoice, supplier in records_data:
            record = PDFRecord(location, requester, invoice, supplier)
            destination_path = self._create_directory_structure(record)
            self._copy_pdf_file(record, destination_path)
        return self.stats
    def print_summary(self) -> None:
        print(f"\n=== RESUMEN ===")
        print(f"Carpetas creadas: {self.stats.folders_created}")
        print(f"Archivos copiados exitosamente: {self.stats.files_moved}")
        print(f"Archivos no encontrados: {self.stats.files_not_found}")
        print(f"Total de registros procesados: {self.stats.total_records}")
    def print_directory_structure(self) -> None:
        print(f"\n=== ESTRUCTURA CREADA ===")
        try:
            for location_dir in sorted(self.output_directory.iterdir()):
                if location_dir.is_dir():
                    print(f"📁 {location_dir.name}/")
                    for requester_dir in sorted(location_dir.iterdir()):
                        if requester_dir.is_dir():
                            print(f"  📁 {requester_dir.name}/")
                            for supplier_dir in sorted(requester_dir.iterdir()):
                                if supplier_dir.is_dir():
                                    pdf_count = count_pdf_files(str(supplier_dir))
                                    print(f"    📁 {supplier_dir.name}/ ({pdf_count} archivos)")
        except Exception as e:
            print(f"Error al mostrar estructura: {e}")