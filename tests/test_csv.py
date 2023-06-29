import csv
import os


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_csv():
    csv_use = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources/username.csv')
    with open(csv_use, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(csv_use, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        rows = list(csvreader)
        assert len(rows) == 2
        assert rows[0] == ['Anna', 'Pavel', 'Peter']
        assert rows[1] == ['Alex', 'Serj', 'Yana']
