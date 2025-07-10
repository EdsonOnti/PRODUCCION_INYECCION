# 🔧 Automatización de Reportes de Producción con MySQL + Python + Power BI

Este repositorio forma parte de una solución desarrollada internamente para automatizar el análisis de producción en mi lugar de trabajo.  
Incluye conexiones directas a una base de datos local en MySQL, extracción de datos con Python y su posterior análisis en Power BI.

> ⚠️ Proyecto 100% real y en uso. Ha sido desarrollado de forma autodidacta para cubrir múltiples responsabilidades de análisis, conexión y carga de datos que realizo individualmente en mi rol actual.

---

## 📂 Contenido del proyecto

### 1. `conexion_mysql.py`
Archivo modular con una clase desarrollada en Python utilizando **Programación Orientada a Objetos (POO)**.

**Funciones principales:**
- Conexión a base de datos local MySQL
- Ejecución de consultas SQL (`SELECT`, `INSERT`, etc.)
- Exportación de resultados a DataFrames
- Función para cerrar conexiones

> Este archivo actúa como **motor de comunicación entre Python y MySQL**.

---

### 2. `manejo_reporte_produccion.ipynb`
Notebook principal donde se realiza la conexión a la base de datos y se ejecutan los **querys necesarios para análisis de producción**.

**Incluye:**
- Conexión usando `conexion_mysql.py`
- Consultas SQL optimizadas para Power BI
- Limpieza básica y exportación de datos

> Este archivo prepara los datos que luego serán analizados en Power BI mediante archivos `.csv` o conexión directa.

---

### 3. `interfaz_produccion-base_de_datos.ipynb`
Un pequeño extra que agregué para **facilitar el registro manual de datos** mediante una **interfaz gráfica sencilla** creada en Python.

**Funcionalidades:**
- Registro rápido de eventos o reportes
- Inserción directa a la base de datos MySQL
- Interfaz básica construida con `tkinter`

> Aunque es algo simple y personal, esta herramienta me ha permitido ahorrar tiempo en el registro manual de información.

---

## 🛠️ Tecnologías usadas

- **Python**
  - Pandas
  - MySQL Connector
  - Tkinter
- **MySQL (local)**
- **Power BI** (para visualización final)
- **VS Code + Jupyter Notebooks**

---

## 🎯 Objetivo del proyecto

Reducir el trabajo manual al máximo automatizando:
- La conexión y extracción de datos desde MySQL
- El registro y almacenamiento de nuevos datos
- La preparación para análisis visual en Power BI

---

## 💡 Notas finales

Todo el desarrollo fue realizado en mi tiempo laboral como solución integral personal (sin equipo técnico de soporte).  
Lo comparto aquí como parte de mi portafolio y como ejemplo de cómo resolver necesidades reales con herramientas accesibles.

---

## 📬 Contacto

Si quieres saber más sobre este proyecto o colaborar en futuras ideas, ¡no dudes en escribirme por LinkedIn!
https://www.linkedin.com/in/edson-martin-ontiveros-lima-673b5b148/
