# Aplicación de Cálculo de Áreas con PyQt6 (POO)

## Descripción
Aplicación de escritorio desarrollada en Python usando PyQt6 y Programación Orientada a Objetos (POO). Permite calcular el área de figuras geométricas (Círculo, Triángulo, Rectángulo y Cuadrado) mediante una interfaz gráfica interactiva.

---

## Estructura del Proyecto

proyecto/
    src/
        logica/              # Lógica de negocio (clases para cálculos)
            areas.py         # Implementación en POO para cálculo de áreas
        vista/               # Archivos de interfaz gráfica
            main_window.ui   # Archivo de diseño en Qt Designer
            ui_main.py       # Código Python generado con pyuic6
    app.py                   # Punto de entrada principal de la aplicación
    README.md                # Documentación del proyecto

---

## Requisitos

- Python 3.8 o superior
- PyQt6

---

## Instalación

1. Clonar el repositorio:

    git clone https://github.com/RICARD0-TU/calculadora-areas-pyqt.git

2. Instalar dependencias:

    pip install PyQt6

---

## Uso

Para ejecutar la aplicación:

    python app.py

Se abrirá la ventana principal donde podrás seleccionar la figura geométrica, ingresar los valores correspondientes y calcular el área.

---

## Funcionalidades

- Menú con opciones para seleccionar figura geométrica.
- Validación de entradas (solo valores positivos).
- Visualización del resultado en la interfaz gráfica.
- Opción para salir con atajo Ctrl+Q.

---

## Autor

RICARDO DAVID TUCTO UBALDO - 7212049@continental.edu.pe
---

