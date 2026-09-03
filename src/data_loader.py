"""
Módulo para cargar datos desde diferentes fuentes
"""
import pandas as pd
import os

# Columnas que tienen formatos mixtos y deben leerse como texto
COLUMNAS_MIXTAS = (16, 41, 42, 47, 48, 57)
DICT_DTYPE = {col: str for col in COLUMNAS_MIXTAS}

def load_csv(file_path):
    """
    Carga un archivo CSV y maneja columnas con formatos mixtos.
    Args:
        file_path (str): Ruta del archivo CSV
    Returns:
        pd.DataFrame: Datos cargados
    """
    try:
        df = pd.read_csv(
            file_path,
            dtype=DICT_DTYPE,
            low_memory=False
        )
        print(f"✅ Datos cargados: {df.shape[0]:,} filas × {df.shape[1]:,} columnas")
        return df
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo en '{file_path}'")
        return None
    except Exception as e:
        print(f"❌ Error al cargar el archivo: {e}")
        return None

def load_raw_data():
    """
    Carga el dataset específico de la clínica veterinaria.
    """
    file_path = 'data/raw/PruebaDivet.csv'
    return load_csv(file_path)
