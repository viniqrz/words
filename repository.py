import csv

class Repository:
    def __init__(self, file_path, entity):
        self.file_path = file_path
        self.entity = entity

    def find(self):
        with open(self.file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            result = []
            for row in reader:
                entity = self.entity(**row)
                result.append(entity)
            return result