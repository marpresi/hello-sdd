from datetime import datetime, timedelta
from typing import List

def calculate_streak(dates: List[str]) -> int:
    """
    Calcula la racha de días consecutivos para un hábito.
    Regla: Un hueco de 1 día es tolerado. Un hueco de 2 días resetea la racha.
    
    Args:
        dates: Lista de fechas en formato ISO (YYYY-MM-DD), no necesariamente ordenadas.
    
    Returns:
        El número de días de la racha actual.
    """
    if not dates:
        return 0

    # Convertir a set de objetos date para evitar duplicados y facilitar búsqueda
    date_set = {datetime.strptime(d, "%Y-%m-%d").date() for d in dates}
    sorted_dates = sorted(list(date_set), reverse=True)
    
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    
    # La racha debe estar conectada con hoy o ayer para ser considerada activa
    if sorted_dates[0] > yesterday:
        check_date = sorted_dates[0]
    elif sorted_dates[0] == yesterday:
        check_date = sorted_dates[0]
    else:
        return 0

    streak = 0
    while True:
        if check_date in date_set:
            streak += 1
            check_date -= timedelta(days=1)
        else:
            # Es un hueco. Verificamos si el día anterior existe para tolerar este hueco.
            if (check_date - timedelta(days=1)) in date_set:
                # Toleramos el hueco (1 día) y seguimos
                check_date -= timedelta(days=1)
            else:
                # Hueco de 2 días o más: la racha se rompe.
                break
                
    return streak
