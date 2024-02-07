from dataclasses import dataclass

@dataclass
class Word():
    id: int
    english: str
    french: str
    spanish: str
    
    def __init__(self, id: int, english: str, french: str, spanish: str):
        self.id = id
        self.english = english 
        self.spanish = spanish
        self.french = french

    @staticmethod
    def from_dict(dict):
        return Word(dict['english'], dict['french'], dict['spanish'])

        
