from repository.word_repository import WordRepository
from entity.word import Word

class CreateWordInputDto():
    def __init__(self, english: str, spanish: str, french: str):
        self.english = english
        self.spanish = spanish
        self.french = french

    @staticmethod
    def from_dict(dict):
        return CreateWordInputDto(dict['english'], dict['spanish'], dict['french'])

    @staticmethod
    def validate(dict: dict) -> bool:
        return dict["english"] != None and dict["spanish"] != None and dict["french"] != None \
            and dict["english"] != "" and dict["spanish"] != "" and dict["french"] != "" \
            and len(dict["english"]) <= 100 and len(dict["spanish"]) <= 100 and len(dict["french"]) <= 100

class CreateWord():
    
    def __init__(self, word_repository: WordRepository):
        self.word_repository = word_repository

    def execute(self, dto: CreateWordInputDto) -> Word:
        already_exists = self.word_repository.find_by_key('english', dto.english)
        if already_exists: raise Exception
        
        id = self.word_repository.get_next_id()
        word = Word(id, dto.english, dto.spanish, dto.french)
        self.word_repository.create(word)
        return word