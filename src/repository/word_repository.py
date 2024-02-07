from repository.repository import Repository
from entity.word import Word

class WordRepository(Repository):
    def __init__(self):
        super().__init__('words.csv', Word)
        
