from pathlib import Path
import csv


class DataReader:
    @staticmethod
    def read_csv_files(files: list[str]) -> list[list[str]]:
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
