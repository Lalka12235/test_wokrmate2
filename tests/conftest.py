import pytest
import csv
from app.average_rating import AverageRatingReport
from app.data_reader import DataReader


@pytest.fixture
def temp_csv(tmp_path):
    """Создаёт временный CSV файл для тестов."""
    file_path = tmp_path / "test.csv"
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'brand', 'price', 'rating'])
        writer.writerow(['iphone 15 pro', 'apple', '999', '4.9'])
        writer.writerow(['galaxy s23 ultra', 'samsung', '1199', '4.8'])
        writer.writerow(['redmi note 12', 'xiaomi', '199', '4.6'])
    return str(file_path)

@pytest.fixture
def temp_invalid_csv(tmp_path):
    """Создаёт временный CSV файл с некорректными данными."""
    file_path = tmp_path / "invalid.csv"
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'brand', 'price', 'rating'])
        writer.writerow(['test', 'apple', '999', 'invalid'])
        writer.writerow(['test', '', '999', '4.5'])
        writer.writerow(['test', 'samsung', '999', ''])
    return str(file_path)

@pytest.fixture
def get_data_reader():
    return DataReader()

@pytest.fixture
def get_average_rating_report():
    return AverageRatingReport()