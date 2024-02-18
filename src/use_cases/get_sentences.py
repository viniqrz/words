from repository.sentence_repository import SentenceRepository
from repository.repository import Where, ilike
from entity.sentence import Sentence

class GetSentencesQueryDto:
    def __init__(self, take: int, skip: int, word: str):
        self.take = take
        self.skip = skip
        self.word = word
        
    @staticmethod
    def validate(data: dict) -> bool:
        return "take" in data and "skip" in data and "word" in data
    
    @staticmethod
    def from_dict(data: dict) -> "GetSentencesQueryDto":
        return GetSentencesQueryDto(data["take"], data["skip"], data["word"])

class GetSentences():
    def __init__(self, sentence_repository: SentenceRepository):
        self.sentence_repository = sentence_repository

    def execute(self, query: GetSentencesQueryDto) -> "list[Sentence]":
        return self.sentence_repository.find(query.take, query.skip, Where(
            lambda x:
                query.word.lower() in [word.lower() for word in x["text"].split(" ")]
        ))
