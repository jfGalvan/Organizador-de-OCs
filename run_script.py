#!/usr/bin/env python3
"""
Script de ejecución simple para el Organizador de Órdenes de Compra.

Este archivo permite ejecutar la aplicación directamente sin necesidad
de instalar el paquete. Útil para desarrollo y pruebas rápidas.

Uso:
    python run.py
"""

import sys
from pathlib import Path

# Añadir el directorio actual al path para importar el módulo
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

try:
    from main import main
    if __name__ == "__main__":
        main()
    
except KeyboardInterrupt:
    print("\n❌ Ejecución interrumpida por el usuario")
    sys.exit(0)
    
except Exception as e:
    print(f"❌ Error inesperado: {e}")
    sys.exit(1)