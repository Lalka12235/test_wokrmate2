import argparse
from average_rating import AverageRatingReport
from data_reader import DataReader
from pathlib import Path

def parse_arguments():
    """Парсит аргументы командной строки."""
    parser = argparse.ArgumentParser(description="Генерирует отчеты из csv файлов")
    parser.add_argument(
        "--files",
        required=True,
        nargs="+",
        type=str,
        help="Путь до csv файлов для отчета"
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=["average-rating"],
        help="Тип отчета для генерации"
    )
    return parser.parse_args()

def main():
    """Основная функция для обработки аргументов и генерации отчёта."""
    try:
        args = parse_arguments()
        report = AverageRatingReport()
        data_reader = DataReader()

        for file in args.files:
            if not Path(file).suffix.lower() == '.csv':
                raise ValueError(f"Файл {file} не является csv файлом")
        
        data = data_reader.read_csv_files(args.files)
        
        if args.report == "average-rating":
            result = report.generate_report(data)
        else:
            raise ValueError(f"Неизвестный тип отчета: {args.report}")
        
        report.print_report(result)
    
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}")
        exit(1)
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        exit(1)

if __name__ == '__main__':
    main()