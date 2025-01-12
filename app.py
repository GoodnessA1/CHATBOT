import streamlit as st
from flask import Flask, render_template, request, jsonify
from main import chatbot

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['GET', 'POST'])
def get_bot_response():
    userText = request.json.get('message')  # Get the message from the frontend
    bot_response = str(chatbot(userText))
    return jsonify({'response': bot_response})

if __name__ == "__main__":
    app.run(debug=True)