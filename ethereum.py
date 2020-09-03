from flask import Flask, url_for, jsonify, request
import requests
import json
import os

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

# Set url ENV 'eurl' to your Ethereum Node RPC Endpoint
# Eg: http://[ip]:[port]
# Eg: Infura support https://mainnet.infura.io/v3/<api_key>
url = os.environ['eurl']

# All requests require this header
headers = {'Content-Type': 'application/json', }
disallowed_methods = ['eth_accounts', 'db_putString', 'db_getString', 'db_putHex', 'db_getHex']


# Error Handling
@app.errorhandler(400)
def bad_request_error(error):
    print(error)
    response = jsonify({
        'code': 1004,
        'error': 'Bad Request: Incorrect or no data parameters present'
    })
    return response


@app.errorhandler(500)
def internal_server_error(error):
    response = jsonify({
        'code': 1002,
        'error': 'Internal Server Error'
    })
    return response


@app.errorhandler(401)
def unauthorized_error(error):
    response = jsonify({
        'code': 1001,
        'error': 'Unauthorized User Access'
    })
    return response


def other_call(requestjson):
    method = requestjson['method']
    print('requestjson: {}'.format(json.dumps(requestjson)))
    if method == 'passthrough' or method == 'eth_pass':
        requestjson = requestjson['params']
        method = requestjson['method']

    if method in disallowed_methods:
        return jsonify({
            'code': 1026,
            'error': 'Disallowed'
        })

    if 'jsonrpc' not in requestjson:
        requestjson['jsonrpc'] = '2.0'
    if 'id' not in requestjson:
        requestjson['id'] = 1
    if 'params' not in requestjson:
        requestjson['params'] = []

    data = json.dumps(requestjson)
    print('headers: {}'.format(headers))
    #print('data: {}'.format(data['params']))
    response = requests.post(url, headers=headers, data=data)
    print('response: {} headers: {} data: {} json: {}'.format(response, headers, data, response.json()))
    return response.json()


@app.route('/', methods=['POST'])
def main():
    payload = request.json
    print('payload: {}'.format(payload))
    return other_call(payload)


# Web Server is listening on 0.0.0.0:80
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
