from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"  # Replace with your actual API key securely
)

@app.route('/')
def home():
    return render_template('deepseek.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']

    # Call the model
    completion = client.chat.completions.create(
        model="deepseek-ai/deepseek-r1",
        messages=[{"role": "user", "content": user_input}],
        temperature=0.6,
        top_p=0.7,
        max_tokens=512,
    )

    response = completion.choices[0].message.content
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
