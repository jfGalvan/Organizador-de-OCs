# 📁 Organizador de Órdenes de Compra

Un sistema modular y robusto para organizar archivos PDF de órdenes de compra en estructuras de directorios basadas en ubicación, solicitante y proveedor.

## 🚀 Características

- **Interfaz gráfica amigable** para selección de archivos y carpetas
- **Validación automática** de datos y columnas requeridas
- **Estructura jerárquica** organizada por ubicación → solicitante → proveedor
- **Manejo robusto de errores** con mensajes informativos
- **Estadísticas detalladas** del proceso de organización
- **Código modular** fácil de mantener y extender

## 📋 Requisitos

- Python 3.7 o superior
- pandas
- openpyxl (para archivos Excel)
- tkinter (incluido en Python estándar)

## 🛠️ Instalación

1. Clona o descarga el proyecto
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## 📖 Uso

### Ejecución básica

```bash
python -m purchase_order_organizer
```

### Uso como módulo

```python
from purchase_order_organizer import PurchaseOrderOrganizer

app = PurchaseOrderOrganizer()
app.run()
```

### Uso avanzado

```python
from purchase_order_organizer import FileOrganizer, DataHandler

# Crear manejador de datos
data_handler = DataHandler("datos.xlsx")
data_handler.load_data()
data_handler.print_preview()

# Organizar archivos
organizer = FileOrganizer("datos.xlsx", "pdfs/", "output/")
stats = organizer.organize_files()
organizer.print_summary()
```

## 📊 Formato de Datos

El archivo de datos (CSV/Excel) debe contener las siguientes columnas:

| Columna | Descripción | Ejemplo |
|---------|-------------|---------|
| `Memo` | Ubicación o departamento | "Oficina Central" |
| `Nombre del Solicitante` | Persona que solicita | "Juan Pérez" |
| `Factura` | Número de factura (nombre del PDF) | "FAC001" |
| `Name` | Nombre del proveedor | "Proveedor ABC" |

## 🗂️ Estructura de Salida

```
ordenes_organizadas/
├── Oficina_Central/
│   ├── Juan_Perez/
│   │   ├── Proveedor_ABC/
│   │   │   ├── FAC001.pdf
│   │   │   └── FAC002.pdf
│   │   └── Proveedor_XYZ/
│   │       └── FAC003.pdf
│   └── Maria_Rodriguez/
│       └── Proveedor_DEF/
│           └── FAC004.pdf
└── Sucursal_Norte/
    └── Carlos_Lopez/
        └── Proveedor_GHI/
            └── FAC005.pdf
```

## 🏗️ Arquitectura

```
purchase_order_organizer/
├── __init__.py              # Inicialización del paquete
├── main.py                  # Aplicación principal
├── config.py                # Configuración
├── exceptions.py            # Excepciones personalizadas
├── utils.py                 # Utilidades generales
├── data_handler.py          # Manejo de datos
├── file_organizer.py        # Organizador principal
└── gui_handler.py           # Interfaz gráfica
```

### Componentes principales

- **`PurchaseOrderOrganizer`**: Clase principal que coordina todo el proceso
- **`DataHandler`**: Maneja la lectura y validación de archivos de datos
- **`FileOrganizer`**: Organiza los archivos PDF según la estructura deseada
- **`GUIHandler`**: Maneja la interfaz gráfica para selección de archivos
- **`Config`**: Contiene toda la configuración de la aplicación

## 🔧 Configuración

Puedes modificar la configuración en `config.py`:

```python
class Config:
    # Columnas requeridas en el archivo de datos
    REQUIRED_COLUMNS = [
        'Nombre del Solicitante', 
        'Factura', 
        'Name', 
        'Memo'
    ]
    
    # Nombre de la carpeta de salida
    OUTPUT_FOLDER_NAME = "ordenes_organizadas"
    
    # Extensión de archivos PDF
    PDF_EXTENSION = ".pdf"
```

## 📝 Logging

El programa proporciona información detallada durante la ejecución:

- ✅ Archivos y carpetas procesados exitosamente
- ❌ Errores y archivos no encontrados
- 📊 Estadísticas finales del proceso
- 🗂️ Estructura de directorios creada

## 🚨 Manejo de Errores

- **Validación de archivos**: Verifica que existan las columnas requeridas
- **Validación de directorios**: Asegura que los directorios sean accesibles
- **Nombres seguros**: Limpia caracteres no válidos en nombres de archivos
- **Recuperación graceful**: Continúa procesando aunque algunos archivos fallen

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Añade nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

Si encuentras algún problema o tienes sugerencias:

1. Revisa la documentación
2. Busca en los issues existentes
3. Crea un nuevo issue con detalles del problema

---

**¡Feliz organización de archivos! 📁✨**