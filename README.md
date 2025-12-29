# 🏀 NBA Shot Charts Visualizer

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📌 Descripción
Este proyecto es una herramienta de análisis de datos deportivos que extrae coordenadas de tiro en tiempo real desde la **API oficial de la NBA** y genera visualizaciones avanzadas (**Shot Charts**). 

El objetivo es transformar datos crudos de coordenadas $X$ e $Y$ en mapas de calor y gráficos de dispersión que permitan entender el comportamiento ofensivo y la eficiencia de los jugadores de la liga.

## 🚀 Características
- 🔍 **Búsqueda Dinámica:** Obtención de datos de cualquier jugador activo o histórico mediante la `nba_api`.
- 🏟️ **Cancha de Precisión:** Generación de una media cancha de la NBA con medidas oficiales mediante `Matplotlib`.
- 📊 **Análisis de Eficiencia:** Visualización diferenciada entre tiros encestados y fallados.
- 📂 **Exportación:** Capacidad de guardar las visualizaciones en alta calidad (PNG/PDF).

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python
* **Extracción de Datos:** [nba_api](https://github.com/swar/nba_api)
* **Manipulación de Datos:** Pandas
* **Visualización:** Matplotlib & Seaborn

## 🔧 Instalación y Uso
*(Próximamente...)*

```bash
# Clonar el repositorio
git clone [https://github.com/TU_USUARIO/nba-shot-charts-visualizer.git](https://github.com/TU_USUARIO/nba-shot-charts-visualizer.git)

# Instalar dependencias
pip install -r requirements.txt