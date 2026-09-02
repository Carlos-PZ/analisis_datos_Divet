# 🚀 Análisis de Datos - Clínica Veterinaria Divet

## 📌 Descripción del Proyecto
La clínica veterinaria Divet genera diariamente cientos de registros de ventas y servicios. Este proyecto tiene como objetivo construir un pipeline de datos completo (end-to-end) que transforme estos registros en información accionable. El enfoque principal es doble: (1) entender el comportamiento de compra de los clientes y las necesidades de sus mascotas, y (2) evaluar el desempeño del personal técnico para optimizar la asignación de turnos y recursos.

## 🎯 Objetivos del Proyecto
- **Objetivo 1:** Realizar un análisis exploratorio de datos (EDA) para identificar:
  - Servicios más demandados y su estacionalidad
  - Perfil de pacientes (especie, edad, peso) asociado a cada servicio
  - Productividad y eficiencia por técnico y por sucursal
- **Objetivo 2:** Crear un pipeline de datos modular en Python que:
  - Extraiga y limpie los datos de manera automática
  - Cree variables derivadas (features) para análisis avanzados
  - Genere un conjunto de datos enriquecido listo para visualización
- **Objetivo 3:** Diseñar un panel en Power BI que permita:
  - Visualizar los KPIs operativos
  - Filtrar por sucursal, técnico, período y tipo de servicio
  - Identificar oportunidades de mejora en la operación

## 🛠️ Stack Tecnológico
- **Lenguaje:** Python 3.9+
- **Librerías:** pandas, numpy, matplotlib, seaborn, scikit-learn (ver `requirements.txt`)
- **Entorno de Desarrollo:** Kaggle Notebooks (para EDA y modelado)
- **Visualización:** Power BI (para dashboard interactivo)
- **Control de Versiones:** Git + GitHub

## 📂 Estructura del Proyecto

<img width="476" height="700" alt="imagen" src="https://github.com/user-attachments/assets/e1c166c8-d36c-4c5f-95a2-230bb9e14ffe" />


## 📊 Principales Hallazgos (Ejemplo)
[Aquí puedes poner, cuando los tengas, algunos resultados clave. Por ejemplo:]
- **Volumen de ventas:** Se registraron más de 100,000 transacciones en el período analizado.
- **Perfil de pacientes:** La mayoría de las atenciones son para perros (`Canino`), seguido de gatos (`Felino`).
- **Estacionalidad:** Se observa un pico en atenciones durante los meses de [meses con más ventas].

## 🔄 Cómo Ejecutar el Pipeline
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Carlos-PZ/analisis_datos_Divet.git

2. Instalar las dependencias:
pip install -r requirements.txt
3. Colocar tu archivo CSV en data/raw/
4. Ejecutar el pipeline principal:
python src/main.py
5. Los datos procesados se guardarán en data/processed/ y las figuras en reports/figures/

## Autor: Carlos Pineda Zermeño
- GitHub: [Carlos-PZ](https://github.com/Carlos-PZ)
- LinkedIn: https://www.linkedin.com/in/carlos-pz/
- Kaggle: https://www.kaggle.com/carlospinedaz

## Última actualización
Septiembre 2026
