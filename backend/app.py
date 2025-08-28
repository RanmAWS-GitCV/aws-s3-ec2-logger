import flask
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

counter = 0

@app.route('/increment', methods=['POST'])
def increment():
    global counter
    counter+=1
    return jsonify(count=counter)

@app.route('/decrement', methods=['POST'])
def decrement():
    global counter
    counter-=1
    return jsonify(count=counter)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
