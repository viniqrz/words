from repository.repository import Repository
from entity.sentence import Sentence

class SentenceRepository(Repository):
    def __init__(self):
        super().__init__('sentences.csv', Sentence)
