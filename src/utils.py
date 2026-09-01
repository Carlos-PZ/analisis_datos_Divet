"""
Funciones auxiliares genéricas
"""
import os
import pandas as pd
from datetime import datetime

def get_current_date():
    """Retorna fecha actual en formato YYYYMMDD"""
    return datetime.now().strftime("%Y%m%d")

def save_dataframe(df, file_path):
    """Guarda DataFrame en CSV"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f"✅ DataFrame guardado en: {file_path}")
