import unittest
from datetime import date, timedelta
from habits_cli.core import calculate_streak, validate_habit_name

class TestCore(unittest.TestCase):
    def test_validate_habit_name_valid(self):
        """RF-2: Nombres de hasta 50 caracteres son válidos."""
        self.assertTrue(validate_habit_name("Leer"))
        self.assertTrue(validate_habit_name("A" * 50))

    def test_validate_habit_name_too_long(self):
        """RF-2: Nombres de más de 50 caracteres son inválidos."""
        self.assertFalse(validate_habit_name("A" * 51))

    def test_calculate_streak_empty(self):
        """RF-3: Racha inicial es 0."""
        self.assertEqual(calculate_streak([], date.today()), 0)

    def test_calculate_streak_perfect(self):
        """RF-3: Racha perfecta cuenta todos los días."""
        today = date.today()
        dates = [today, today - timedelta(days=1), today - timedelta(days=2)]
        self.assertEqual(calculate_streak(dates, today), 3)

    def test_calculate_streak_with_tolerance(self):
        """RF-3: Racha se mantiene si no hay dos días consecutivos fallidos."""
        today = date.today()
        # Hoy (S), Ayer (F), Antes de ayer (S) -> Racha: 2
        dates = [today, today - timedelta(days=2)]
        self.assertEqual(calculate_streak(dates, today), 2)

    def test_calculate_streak_broken(self):
        """RF-3: Racha se rompe tras dos días consecutivos fallidos."""
        today = date.today()
        # Hoy (F), Ayer (F), Antes (S) -> Racha: 0 (porque empezó hoy y falló 2 días)
        # Nota: El algoritmo debe mirar hacia atrás desde hoy.
        dates = [today - timedelta(days=2)]
        self.assertEqual(calculate_streak(dates, today), 0)

    def test_calculate_streak_broken_after_start(self):
        """RF-3: Racha se rompe si hay dos fallos después de haber tenido éxitos."""
        today = date.today()
        # Hoy (S), Ayer (F), Antes (F), Antes (S)
        # El ciclo se rompe en el segundo fallo.
        dates = [today, today - timedelta(days=3)]
        self.assertEqual(calculate_streak(dates, today), 1)

if __name__ == "__main__":
    unittest.main()
