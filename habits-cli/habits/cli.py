import sys
import argparse
from datetime import datetime
from habits.storage import load_data, save_data
from habits.core import calculate_streak

def main():
    parser = argparse.ArgumentParser(description="Habits CLI - Registra tus hábitos de estudio")
    subparsers = parser.add_subparsers(dest="command")

    # Comando create
    create_parser = subparsers.add_parser("create", help="Crea un nuevo hábito")
    create_parser.add_argument("name", type=str, help="Nombre del hábito")

    # Comando done
    done_parser = subparsers.add_parser("done", help="Marca un hábito como completado hoy")
    done_parser.add_argument("name", type=str, help="Nombre del hábito")

    # Comando list
    subparsers.add_parser("list", help="Lista todos los hábitos y sus rachas")

    args = parser.parse_args()

    if args.command == "create":
        handle_create(args.name)
    elif args.command == "done":
        handle_done(args.name)
    elif args.command == "list":
        handle_list()
    else:
        parser.print_help()

def handle_create(name: str):
    if len(name) > 50:
        print("Error: El nombre del hábito no puede superar los 50 caracteres.")
        return

    data = load_data()
    if name in data:
        print(f"Error: El hábito '{name}' ya existe.")
        return

    data[name] = []
    save_data(data)
    print(f"Hábito '{name}' creado con éxito.")

def handle_done(name: str):
    data = load_data()
    if name not in data:
        print(f"Error: El hábito '{name}' no existe.")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    if today in data[name]:
        print(f"El hábito '{name}' ya fue completado hoy.")
        return

    data[name].append(today)
    save_data(data)
    print(f"¡Buen trabajo! '{name}' completado hoy.")

def handle_list():
    data = load_data()
    if not data:
        print("No hay hábitos creados.")
        return

    # Formateo: 20 caracteres para nombre, 10 para racha
    print(f"{'Hábito':<20} | {'Racha':<10}")
    print("-" * 32)
    for name, dates in data.items():
        streak = calculate_streak(dates)
        print(f"{name:<20} | {streak:<10}")

if __name__ == "__main__":
    main()
