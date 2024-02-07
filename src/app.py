from flask import Flask, jsonify, request
from repository.word_repository import WordRepository
from repository.sentence_repository import SentenceRepository
from use_cases.get_random_word import GetRandomWord
from use_cases.create_word import CreateWord, CreateWordInputDto
from use_cases.get_random_sentence import GetRandomSentence

app = Flask(__name__)

word_repository = WordRepository()
sentence_repository = SentenceRepository()

get_random_word = GetRandomWord(word_repository)
create_word = CreateWord(word_repository)
get_random_sentence = GetRandomSentence(sentence_repository)

@app.get("/")
def hello_world():
    return sentence_repository.find()

@app.get("/words/random")
def random_word():
    return jsonify(get_random_word.execute())

@app.get("/sentences/random")
def random_sentence():
    return jsonify(get_random_sentence.execute())

@app.post("/words")
def handle_create_word():
    body = request.get_json()

    valid = CreateWordInputDto.validate(body)
    if (not valid):
        return "Invalid word", 400
    
    dto = CreateWordInputDto.from_dict(body)

    return jsonify(create_word.execute(dto))

@app.post("/sentences")
def create_sentence():
    return "Not implemented"