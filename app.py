from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

messages = []

# Load chatStr from a file if it exists
try:
    with open("chatstr.txt", "r") as file:
        chatStr = file.read()
except FileNotFoundError:
    chatStr = ""


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # Handle AJAX request
            user_message = request.form['user_message'].strip()
            if user_message != '':
                messages.append({'content': user_message, 'sender': 'user'})
                bot_message = chat(user_message)
                messages.append({'content': bot_message, 'sender': 'bot'})
                return jsonify({'bot_message': bot_message})
        else:
            # Handle regular form submission
            user_message = request.form['user_message'].strip()
            if user_message != '':
                messages.append({'content': user_message, 'sender': 'user'})
                bot_message = chat(user_message)
                messages.append({'content': bot_message, 'sender': 'bot'})
    return render_template('index.html', messages=messages)


def save_chatstr():
    with open("chatstr.txt", "w") as file:
        file.write(chatStr)


def chat(query):
    global chatStr
    openai.api_key = "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"
    chatStr += f"Master: {query}\nJ.A.R.V.I.S.: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    chatStr += f"{response['choices'][0]['text']}\n"
    save_chatstr()  # Save the updated chatStr to the file
    return response["choices"][0]["text"]


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
