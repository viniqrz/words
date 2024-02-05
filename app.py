from flask import Flask
from word_repository import WordRepository
from sentence_repository import SentenceRepository

app = Flask(__name__)

word_repository = WordRepository()
sentence_repository = SentenceRepository()

@app.route("/")
def hello_world():
    return sentence_repository.find()