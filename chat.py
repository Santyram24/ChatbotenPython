from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections
from nltk_chatbot import pairs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    chat = Chat(pairs.pairs, reflections)
    response = chat.respond(user_message)
    return response

if __name__ == '__main__':
    app.run(debug=True)

