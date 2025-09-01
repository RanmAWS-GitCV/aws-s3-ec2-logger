import flask
from flask import Flask, jsonify, request, send_from_directory
import boto3

app = Flask(__name__)

dynamodb = boto3.client('dynamodb', region_name = 'eu-west-2')

rmp = 0

def get_rmp():
    global rmp
    response = dynamodb.get_item(
        TableName = 'Ranmapoints_Table',
        Key={'id': {'N': '1'}})
    rmp = int(response['Item']['RMP']['N'])

def set_rmp():
    global rmp
    response = dynamodb.put_item(
        TableName='Ranmapoints_Table',
        Item={
            'id': {'N': '1'},
            'RMP': {'N': str(rmp)}
        }
    )

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/balance', methods=['GET'])
def balance():
    global rmp
    get_rmp()
    return jsonify(count=rmp)

@app.route('/increment', methods=['POST'])
def increment():
    global rmp
    get_rmp()
    rmp+=1
    set_rmp()
    return jsonify(count=rmp)

@app.route('/decrement', methods=['POST'])
def decrement():
    global rmp
    get_rmp()
    rmp-=1
    set_rmp()
    return jsonify(count=rmp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
