from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('deepseek.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    # Placeholder response for demonstration purposes
    response = f"Received: {user_input}"
    return jsonify({'response': response})

if __name__ == '__main__':
   app.run(debug=True)
