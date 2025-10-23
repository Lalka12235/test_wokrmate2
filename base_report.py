from abc import ABC, abstractmethod

class Report(ABC):
    """Базовый класс для всех отчётов."""

    @abstractmethod
    def generate_report(self, data):
        """Генерирует отчёт из данных."""
        pass

    def print_report(self, report_data):
        """Выводит отчёт в виде таблицы с нумерацией."""
        from tabulate import tabulate
        if not report_data:
            print("No data to display.")
            return
        print(tabulate(report_data, headers="keys", tablefmt="grid", showindex=range(1, len(report_data)+1)))
