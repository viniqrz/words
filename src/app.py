from flask import Flask, jsonify, request
from repository.word_repository import WordRepository
from repository.sentence_repository import SentenceRepository
from use_cases.get_random_word import GetRandomWord
from use_cases.create_word import CreateWord, CreateWordInputDto
from use_cases.get_random_sentence import GetRandomSentence
from use_cases.get_sentences import GetSentences, GetSentencesQueryDto

app = Flask(__name__)

word_repository = WordRepository()
sentence_repository = SentenceRepository()

get_random_word = GetRandomWord(word_repository)
create_word = CreateWord(word_repository)
get_random_sentence = GetRandomSentence(sentence_repository)
get_sentences = GetSentences(sentence_repository)

@app.get("/")
def hello_world():
    return sentence_repository.find()

@app.get("/words/random")
def random_word():
    return jsonify(get_random_word.execute())

@app.get("/sentences/random")
def random_sentence():
    return jsonify(get_random_sentence.execute())

@app.get("/sentences")
def get_sentences_route():
    page = int(request.args.get('page') or 1)
    word = request.args.get('word') or ""
    items_per_page = int(request.args.get('items_per_page') or 10)
    
    valid = GetSentencesQueryDto.validate({
        "take": items_per_page,
        "skip": (page - 1) * items_per_page,
        "word": word
    })
    if (not valid):
        return "Invalid query", 400
    
    dto = GetSentencesQueryDto.from_dict({
        "take": items_per_page,
        "skip": (page - 1) * items_per_page,
        "word": word
    })
    
    return jsonify(get_sentences.execute(dto))

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