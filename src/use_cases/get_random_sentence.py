from repository.sentence_repository import SentenceRepository
from entity.sentence import Sentence

class GetRandomSentence():
    
    def __init__(self, sentence_repository: SentenceRepository):
        self.sentence_repository = sentence_repository

    def execute(self) -> Sentence:
        return self.sentence_repository.random()
