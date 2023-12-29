from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

# Replace with your actual API key
api_key = "API_KEY_HERE"
client = OpenAI(api_key=api_key)
model_name = "gpt-3.5-turbo-1106"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rephrase', methods=['POST'])
def rephrase():
    if request.method == 'POST':
        sentence = request.form['sentence']

        # Call OpenAI API
        response = client.chat.completions.create(
            model=model_name,
            #response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "Just give me the rephrased sentence"},
                {"role": "user", "content": f"Rephrase the sentence: {sentence}"}
            ]
        )

        rephrased_sentence = response.choices[0].message.content

        return render_template('index.html', sentence=sentence, rephrased_sentence=rephrased_sentence)

if __name__ == '__main__':
    app.run(debug=True)
