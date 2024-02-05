from dataclasses import dataclass

@dataclass
class Word():
    english: str
    french: str
    spanish: str
    
    def __init__(self, english, french, spanish):
        self.english = english 
        self.spanish = spanish
        self.french = french

    @staticmethod
    def from_dict(dict):
        return Word(dict['english'], dict['french'], dict['spanish'])

        
