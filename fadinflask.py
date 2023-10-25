import os
from flask import Flask, request, jsonify

app = Flask(__name__)
port = int(os.environ.get('FLASK_RUN_PORT', 80))

@app.route('/', methods=['GET'])
def sayHello():
    return "Hello Fadin v2!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)