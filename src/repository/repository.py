import csv
from random import randrange

class Repository:
    def __init__(self, file_path, entity):
        self.file_path = file_path
        self.entity = entity
        
    def map_to_entity(self, row):
        return self.entity(**row)

    def find(self):
        with open(self.file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            result = []
            for row in reader:
                entity = self.map_to_entity(row)
                result.append(entity)
            return result
        
    def count(self):
        with open(self.file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return len(list(reader))
        
    def find_by_id(self, id):
        return self.find_by_key("id", str(id))

    def get_next_id(self):
        return self.max_id() + 1
    
    def random(self):
        count = self.count()
        if count < 2: return self.find_by_id(1)
        id = randrange(1, count)
        res = self.find_by_id(id)
    
        if (res is None):
            return self.random()
        
        return res
    
    def find_by_key(self, key, value):
        with open(self.file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[key] == value:
                    return self.map_to_entity(row)
            return None
    
    def max_id(self):
        with open(self.file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return max([int(row['id']) for row in reader])
        
    def create(self, entity):
        with open(self.file_path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=entity.__dict__.keys())
            writer.writerow(entity.__dict__)

    def delete(self, id):
        with open(self.file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
        with open(self.file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in rows:
                if row['id'] != id:
                    writer.writerow(row)