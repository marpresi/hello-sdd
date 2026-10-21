import pytest
import os
import json
from habits.storage import load_data, save_data, DATA_FILE

def setup_function():
    # Asegurar que el archivo no exista antes de cada test
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def test_save_and_load_empty():
    data = {}
    save_data(data)
    assert load_data() == {}

def test_save_and_load_with_data():
    data = {"Estudiar": ["2023-10-01", "2023-10-02"]}
    save_data(data)
    assert load_data() == data

def test_load_non_existent_file():
    # DATA_FILE ha sido borrado en setup_function
    assert load_data() == {}

def test_corrupt_json_raises_value_error():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write("{ esto no es un json valido")
    
    with pytest.raises(ValueError, match="está corrupto"):
        load_data()
