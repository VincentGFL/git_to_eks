from flask import Flask
#from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World 2"

app.run(host='0.0.0.0', port=5000, debug=True)
# serve (app, host='0.0.0.0', port=5000)