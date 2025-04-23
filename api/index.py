from flask import Flask , jsonify
app= Flask(__name__)
@app.route("/")
def hello():
    return jsonify(message= "Hello kiran don here!")
@app.route('/favicon.ioc')
def favicon():
    return "Kiran don"

def handler(environ, start_response):
    return app(environ, start_response)

#if __name__ == '__main__':
 #   app.run(debug=True)
