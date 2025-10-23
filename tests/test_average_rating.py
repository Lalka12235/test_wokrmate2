import pytest
from average_rating import AverageRatingReport
from tests.conftest import temp_csv,temp_invalid_csv,get_average_rating_report,get_data_reader


@pytest.xfail('Файл не существует')
def test_read_csv_files_nonexistent(get_data_reader):
    """Тестирует обработку несуществующего файла."""
    with pytest.raises(FileNotFoundError, match="Файл nonexistent.csv не существует"):
        get_data_reader.read_csv_files(["nonexistent.csv"])


def test_read_csv_files(temp_csv,get_data_reader):
    """Тестирует чтение CSV файла."""
    data = get_data_reader.read_csv_files([temp_csv])
    assert len(data) == 3
    assert data[0][0] == 'apple'
    assert data[0][1] == 4.9
    assert data[1][0] == 'samsung'
    assert data[2][0] == 'xiaomi'

@pytest.xfail('Некорректные данные')
def test_read_csv_files_invalid_data(temp_invalid_csv):
    """Тестирует обработку некорректных данных."""
    data = get_data_reader.read_csv_files([temp_invalid_csv])
    assert len(data) == 0


def test_generate_average_rating_report(temp_csv,get_data_reader,get_average_rating_report):
    """Тестирует генерацию отчёта average-rating."""
    data = get_data_reader.read_csv_files([temp_csv])
    report = get_average_rating_report.generate_report(data)
    assert len(report) == 3
    assert report['apple'] == 4.9
    assert report['samsung'] == 4.8
    assert report['xiaomi'] == 4.6
