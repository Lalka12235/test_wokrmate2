from tabulate import tabulate
from base_report import Report


class AverageRatingReport(Report):
    
    def generate_report(self, data_from_csv):
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
    
    def print_report(self,report: dict):
        """Выводит отчёт в виде таблицы в консоль."""
        if not report:
            print("No data to display.")
            return
        headers = ["brand", "rating"]
        table = [[brand, rating] for brand, rating in report.items()]
        print(tabulate(table, headers=headers, tablefmt="grid",showindex=range(1, len(table)+1)))