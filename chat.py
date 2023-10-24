from flask import Flask, render_template, request
from nltk.chat.util import reflections
from nltk_chatbot import pairs  # Asegúrate de que "pairs" sea una lista en tu módulo "nltk_chatbot"
from html import escape
import re


def generate_questions_for_pair(pair):
    input_text, responses = pair
    question_list = []
    for sentence in input_text.split('|'):
        # Eliminar signos de puntuación y errores ortográficos comunes
        sentence = re.sub(r'[¿?,.]', '', sentence)
        sentence = sentence.lower()
        question_list.append(sentence)
    
    return question_list + responses


app = Flask(__name__)

# Generar diccionario de preguntas y respuestas
question_dict = {}
for pair in pairs.pairs:  # Accede a la lista de pares dentro de "pairs"
    questions = generate_questions_for_pair(pair)
    for question in questions:
        question_dict[question] = pair[1]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    
    # Limpiar el mensaje del usuario
    user_message = re.sub(r'[¿?,.]', '', user_message)
    user_message = user_message.lower()
    
    # Buscar una respuesta en el diccionario y renderizar como HTML
    response = question_dict.get(user_message, ["Lo siento, no entiendo tu pregunta."])
    
    # Acceder al primer elemento de la lista y renderizar como HTML
    response = escape(response[0])
    
    return response




if __name__ == '__main__':
    app.run(debug=True)





