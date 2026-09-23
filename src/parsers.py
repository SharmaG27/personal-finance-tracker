import csv
from src.models import Transaction

class CSVParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        transactions = []
        with open(self.file_path, mode = "r") as file:
            csv.DictReader(file)

