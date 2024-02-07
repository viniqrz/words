from dataclasses import dataclass

@dataclass
class Sentence():
    id: int
    language: str
    text: str
    words: list
    
    valid_languages = ['english', 'french', 'spanish']
    
    def __init__(self, id: int, language: str, text: str):
        self.id = id
        self.language = language
        self.text = text
        self.words = text.split(' ')

    def set_words(self, words):
        self.words = words
        
    @staticmethod
    def from_dict(dict):
        return Sentence(dict['language'], dict['text'])

        
