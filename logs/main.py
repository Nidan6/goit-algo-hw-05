import sys
from collections import Counter
from prettytable import PrettyTable

def load_logs(file_path: str) -> list:
    try:

        with open(file_path, 'r', encoding="utf-8") as file:
            log_list = [parse_log_file(line) for line in file]

    except FileNotFoundError:
        print("Не вдалося знайти файл з логами")
    except Exception as e:
        print(f"Помилка при завантаженні логів: {e}")

    return log_list

def parse_log_file(line:str) -> dict:
    try:
        parts = line.split()
        log_data = {
            "date": parts[0],
            "time": parts[1],
            "level": parts[2],
            "message": ' '.join(parts[3:])
        }
        return log_data

    except (IndexError, ValueError) as e:
        print(f"Помилка при парсингу логу: {e}")

def filter_logs_by_level(logs: list, level: str) -> list:
    try:
        result = list(filter(lambda log: log["level"] == level, logs))

        if len(sys.argv) >= 3:
            print(f"Деталі логів для рівня {level}:")
            for item in result:
                print(item["date"], item["time"], "-", item["message"])

        return result

    except (KeyError, TypeError) as e:
        print(f"Помилка при фільтрації логів: {e}")

def count_logs_by_level(logs:list) -> dict:
    try:
        levels = [log["level"] for log in logs]
        count = Counter(levels)
        return count

    except (KeyError, TypeError) as e:
        print(f"Помилка при підрахунку логів: {e}")

def display_log_counts(counts:dict):
    table = PrettyTable(["Рівень логування", "Кількість"])
    table.align["Рівень логування"] = "l"
    table.align["Кількість"] = "r"
    table.padding_width = 1

    for level, count in counts.items():
        table.add_row([level, count])
    print(table)

def main():
    try:
        file_path = sys.argv[1]
        logs = load_logs(file_path)

        counter = count_logs_by_level(logs)
        display_log_counts(counter)

        if len(sys.argv) >= 3:
            filter_logs_by_level(logs, sys.argv[2])
        else:
            filter_logs_by_level(logs, sys.argv[1])
    except IndexError:
        print("Не вдалося знайти файл логу")

if __name__ == '__main__':
    main()