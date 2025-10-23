import csv
from pathlib import Path
from tabulate import tabulate


def read_csv_files(files: list[Path]) -> list[list[str]]:
    """Читает данные из CSV файлов и возвращает список словарей."""
    data = []
    for file in files:
        file_path = Path(file)
        if not file_path.exists():
            raise FileNotFoundError(f"File {file_path} does not exist")
        if not file_path.is_file():
            raise ValueError(f"Path {file_path} is not a file")
        with file_path.open('r',encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                brand = row.get('brand')
                rating_str = row.get('rating')
                if not brand or not rating_str:
                    continue
                try:
                    rating = float(rating_str)
                except ValueError:
                    continue
                data.append([brand, rating])
    
    return data


def generate_average_rating_report(data_from_csv: list[list[str]]):
    """Генерирует отчёт average-rating: средний рейтинг по брендам."""
    report = {}
    for info in data_from_csv:
        brand,rating = info
        if brand not in report:
            report[brand] = [rating]
        else:
            report[brand].append(rating)

    sort_data = []
    for key,val in report.items():
        temp = round(sum(val) / len(val),2)
        sort_data.append((key,temp))
    
    sort_data = sorted(sort_data)
    return dict(sort_data)
    
    
def print_report(report: dict):
    """Выводит отчёт в виде таблицы в консоль."""
    if not report:
        print("No data to display.")
        return
    headers = ["brand", "rating"]
    table = [[brand, rating] for brand, rating in report.items()]
    print(tabulate(table, headers=headers, tablefmt="grid",showindex=range(1, len(table)+1)))