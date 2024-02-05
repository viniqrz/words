from repository import Repository
from sentence import Sentence

class SentenceRepository(Repository):
    def __init__(self):
        super().__init__('sentences.csv', Sentence)
