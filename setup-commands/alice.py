import flask
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

counter = 0

@app.route('/click', methods=['POST'])
def click():
    global counter
    counter+=1
    return jsonify(count=counter)

if __name__ == '__main__':
    app.run(debug=True)
