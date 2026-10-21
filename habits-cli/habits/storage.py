import json
import os
from typing import Dict, List

DATA_FILE = "data.json"

def load_data() -> Dict[str, List[str]]:
    """
    Carga los datos desde el archivo JSON. 
    Si el archivo no existe, devuelve un diccionario vacío.
    Si el archivo está corrupto, lanza un ValueError.
    """
    if not os.path.exists(DATA_FILE):
        return {}
    
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error: El archivo {DATA_FILE} está corrupto y no se puede leer.") from e

def save_data(data: Dict[str, List[str]]) -> None:
    """
    Guarda el diccionario de datos en el archivo JSON.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
