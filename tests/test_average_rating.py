import pytest
from average_rating import read_csv_files, generate_average_rating_report
from tests.conftest import temp_csv,temp_invalid_csv


def test_read_csv_files_nonexistent():
    """Тестирует обработку несуществующего файла."""
    with pytest.raises(FileNotFoundError, match="File nonexistent.csv does not exist"):
        read_csv_files(["nonexistent.csv"])

def test_read_csv_files(temp_csv):
    """Тестирует чтение CSV файла."""
    data = read_csv_files([temp_csv])
    assert len(data) == 3
    assert data[0][0] == 'apple'
    assert data[0][1] == 4.9
    assert data[1][0] == 'samsung'
    assert data[2][0] == 'xiaomi'

def test_read_csv_files_invalid_data(temp_invalid_csv):
    """Тестирует обработку некорректных данных."""
    data = read_csv_files([temp_invalid_csv])
    assert len(data) == 0

def test_generate_average_rating_report(temp_csv):
    """Тестирует генерацию отчёта average-rating."""
    data = read_csv_files([temp_csv])
    report = generate_average_rating_report(data)
    assert len(report) == 3
    assert report['apple'] == 4.9
    assert report['samsung'] == 4.8
    assert report['xiaomi'] == 4.6
