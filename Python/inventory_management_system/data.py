import csv
import os

class DataManager:
    def __init__(self):
        self.data_folder = "data"
        self.file_path = os.path.join(self.data_folder, "inventory.csv")
        self.inventory = []
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["Name", "Quantity", "Price", "Category"])
                writer.writeheader()

    def load_data(self):
        if not os.path.exists(self.file_path):
            return
        with open(self.file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            self.inventory = list(reader)

    def save_data(self):
        with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Quantity", "Price", "Category"])
            writer.writeheader()
            writer.writerows(self.inventory)