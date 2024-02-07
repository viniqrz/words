from repository.word_repository import WordRepository
from entity.word import Word

class GetRandomWord():
    def __init__(self, word_repository: WordRepository):
        self.word_repository = word_repository

    def execute(self) -> Word:
        return self.word_repository.random()
