#!/usr/bin/env python3
"""
Script de instalación para el Organizador de Órdenes de Compra.
"""
from pathlib import Path
from setup_script import setup, find_packages


# Leer el archivo README para la descripción larga
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Leer requirements.txt para las dependencias
requirements = []
try:
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
except FileNotFoundError:
    requirements = ['pandas>=1.5.0', 'openpyxl>=3.0.9']

setup(
    name="purchase-order-organizer",
    version="2.0.0",
    author="Tu Nombre",
    author_email="tu.email@ejemplo.com",
    description="Sistema modular para organizar archivos PDF de órdenes de compra",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/purchase-order-organizer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: X11 Applications :: GTK",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
            'black>=21.0',
            'flake8>=3.8',
            'mypy>=0.800',
        ],
        'test': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'purchase-order-organizer=purchase_order_organizer.main:main',
            'poo=purchase_order_organizer.main:main',  # Comando corto
        ],
    },
    include_package_data=True,
    package_data={
        'purchase_order_organizer': ['*.txt', '*.md'],
    },
    keywords=[
        'pdf', 'organizer', 'files', 'purchase-orders', 
        'automation', 'business', 'office', 'documents'
    ],
    project_urls={
        'Bug Reports': 'https://github.com/tu-usuario/purchase-order-organizer/issues',
        'Source': 'https://github.com/tu-usuario/purchase-order-organizer',
        'Documentation': 'https://github.com/tu-usuario/purchase-order-organizer/wiki',
    },
)