import pytest
from datetime import datetime, timedelta
from habits.core import calculate_streak

def get_date_str(days_ago: int) -> str:
    """Helper to get a date string YYYY-MM-DD based on days from today."""
    date = datetime.now() - timedelta(days=days_ago)
    return date.strftime("%Y-%m-%d")

def test_streak_empty_dates():
    """T7: Hábito sin fechas registradas devuelve racha 0."""
    assert calculate_streak([]) == 0

def test_streak_perfect_sequence():
    """T4: Secuencia perfecta de fechas devuelve el conteo correcto."""
    # Hoy, ayer y anteayer
    dates = [get_date_str(0), get_date_str(1), get_date_str(2)]
    assert calculate_streak(dates) == 3

def test_streak_with_one_day_gap():
    """T5: Hueco de un solo día no resetea la racha (tolerancia)."""
    # Hoy, (hueco ayer), anteayer, hace 3 días
    dates = [get_date_str(0), get_date_str(2), get_date_str(3)]
    # Racha: Hoy (1) + tolerancia (0) + anteayer (1) + hace 3 días (1) = 3
    # Nota: El cálculo de racha cuenta los días COMPLETADOS.
    assert calculate_streak(dates) == 3

def test_streak_with_two_day_gap():
    """T6: Hueco de dos días resetea la racha."""
    # Hoy, (hueco ayer), (hueco anteayer), hace 3 días
    dates = [get_date_str(0), get_date_str(3), get_date_str(4)]
    # Racha solo incluye hoy porque hay un hueco de 2 días antes.
    assert calculate_streak(dates) == 1

def test_streak_not_active():
    """La racha debe romperse si no hay registro hoy o ayer."""
    # Hace 2 días y hace 3 días
    dates = [get_date_str(2), get_date_str(3)]
    assert calculate_streak(dates) == 0

def test_streak_unordered_dates():
    """La racha debe calcularse correctamente independientemente del orden de la lista."""
    dates = [get_date_str(2), get_date_str(0), get_date_str(1)]
    assert calculate_streak(dates) == 3

def test_streak_duplicate_dates():
    """Fechas duplicadas no deben inflar la racha."""
    today = get_date_str(0)
    dates = [today, today, get_date_str(1)]
    assert calculate_streak(dates) == 2
