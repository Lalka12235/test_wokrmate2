import argparse
from average_rating import read_csv_files,generate_average_rating_report,print_report
from pathlib import Path

def parse_arguments():
    """Парсит аргументы командной строки."""
    parser = argparse.ArgumentParser(description="Generate reports from CSV files.")
    parser.add_argument(
        "--files",
        required=True,
        nargs="+",
        type=str,
        help="Paths to CSV files to process"
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=["average-rating"],
        help="Type of report to generate"
    )
    return parser.parse_args()

def main():
    """Основная функция для обработки аргументов и генерации отчёта."""
    try:
        args = parse_arguments()

        for file in args.files:
            if not Path(file).suffix.lower() == '.csv':
                raise ValueError(f"File {file} is not a CSV file")
        
        data = read_csv_files(args.files)
        
        if args.report == "average-rating":
            report = generate_average_rating_report(data)
        else:
            raise ValueError(f"Unknown report type: {args.report}")
        
        print_report(report)
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        exit(1)

if __name__ == '__main__':
    main()