# 🏀 NBA Shot Charts Visualizer

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📌 Descripción
Este proyecto es una herramienta avanzada de análisis de datos deportivos que transforma datos crudos de la **API oficial de la NBA** en visualizaciones de alto impacto. 

A diferencia de un shot chart convencional, este visualizador implementa un sistema de **Mapas Híbridos**, permitiendo analizar simultáneamente la **frecuencia de tiro** y la **eficiencia** del jugador en un solo gráfico.

## 🚀 Características Avanzadas
- 🧬 **Hexágonos Híbridos:** Visualización de doble variable donde el **tamaño** del hexágono representa el volumen de tiros y el **color** representa la efectividad (%).
- ⚔️ **Modo Comparativa:** Generación de gráficos "Cara a Cara" (Side-by-Side) para contrastar estilos de juego de diferentes jugadores o épocas.
- 🎨 **Estética Profesional:** Interfaz diseñada en modo oscuro (Gris Carbón `#333333`) para maximizar el contraste de los datos.
- 🖼️ **Headshot Integration:** Integración dinámica de fotos oficiales de los jugadores mediante procesamiento de imágenes con `Pillow`.
- 📏 **Cancha Geométrica:** Recreación precisa de la duela de la NBA basada en el sistema de coordenadas de la API.


## 🛠️ Tecnologías Utilizadas
* **Extracción de Datos:** [nba_api](https://github.com/swar/nba_api)
* **Procesamiento de Datos:** `Pandas` & `NumPy`
* **Visualización:** `Matplotlib` (Uso avanzado de Patches y RegularPolygons)
* **Manejo de Imágenes:** `Pillow` (PIL)

## 📂 Estructura del Proyecto
- `src/fetcher.py`: Lógica de extracción y filtrado de datos de la API.
- `src/court.py`: Definición geométrica de la cancha.
- `src/main.py`: Orquestador principal y lógica de renderizado híbrido.


## 📝 Nota Técnica: ¿Por qué Hexágonos Híbridos?
En el análisis de datos moderno, el volumen sin eficiencia es engañoso. Un hexágono grande y rojo indica una zona de ineficiencia (muchos tiros, pocos aciertos), mientras que uno pequeño y verde indica una zona de alta eficiencia pero baja frecuencia. Este proyecto permite identificar de un vistazo la verdadera "zona de confort" de un jugador.

## 🔧 Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/nba-shot-charts-visualizer.git](https://github.com/TU_USUARIO/nba-shot-charts-visualizer.git)
   cd nba-shot-charts-visualizer
