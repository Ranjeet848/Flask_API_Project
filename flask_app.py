from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to ChatGPT app!'


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    user_input = request.form['text']
    # Use OpenAI's API to generate a response from ChatGPT
    response = generate_response_from_chatgpt(user_input)
    return response


def generate_response_from_chatgpt(user_input):
    api_key = "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"
    url = "https://api.openai.com/v1/engines/davinci/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "prompt": user_input,
        "engine": "davinci"
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["text"]


if __name__ == '__main__':
    app.run()