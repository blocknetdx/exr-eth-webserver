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


# Error Handling
@app.errorhandler(400)
def bad_request_error(error):
    response = jsonify({
        'code': 1004,
        'error': 'Bad Request: Incorrect or no data parameters present'
    })
    return response


@app.errorhandler(500)
def internal_server_error(error):
    response = jsonify({
        'code': 1002,
        'error': 'Internal Server Error: failed to connect to Ethereum Node'
    })
    return response


@app.errorhandler(401)
def unauthorized_error(error):
    response = jsonify({
        'code': 1001,
        'error': 'Unauthorized User Access'
    })
    return response


# API
def api_eth_accounts():
    data = '{"jsonrpc":"2.0","method":"eth_accounts","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def api_eth_blockNumber():
    data = '{"jsonrpc":"2.0","method":"eth_blockNumber","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def api_eth_call(payload):
    payload_count = len(payload)

    if len(payload) == 7:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 7'
        })
        return payload_error

    From = payload[0]
    to = payload[1]
    gas = payload[2]
    gasPrice = payload[3]
    value = payload[4]
    eth_data = payload[5]
    block_parameter = payload[6]
    data = '{"jsonrpc":"2.0","method":"eth_call","params": [{"from": "' + From + '","to": "' + to + '","gas": "' + gas + '","gasPrice": "' + gasPrice + '","value": "' + value + '","data": "' + eth_data + '"}, "' + block_parameter + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_chainId():
    data = '{"jsonrpc":"2.0","method":"eth_chainId","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def api_eth_estimateGas(payload):
    payload_count = len(payload)

    if len(payload) == 6:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 6'
        })
        return payload_error

    From = payload[0]
    to = payload[1]
    gas = payload[2]
    gasPrice = payload[3]
    value = payload[4]
    eth_data = payload[5]
    data = '{"jsonrpc":"2.0","method":"eth_estimateGas","params": [{"from": "' + From + '","to": "' + to + '","gas": "' + gas + '","gasPrice": "' + gasPrice + '","value": "' + value + '","data": "' + eth_data + '"}],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_gasPrice():
    data = '{"jsonrpc":"2.0","method":"eth_gasPrice","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def api_eth_getBalance(payload):
    payload_count = len(payload)

    if len(payload) == 2:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 2'
        })
        return payload_error

    address = payload[0]
    block_parameter = payload[1]
    data = '{"jsonrpc":"2.0","method":"eth_getBalance","params": ["' + address + '","' + block_parameter + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_getBlockByHash(payload):
    payload_count = len(payload)

    if len(payload) == 2:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 2'
        })
        return payload_error

    block_hash = payload[0]
    show_tx_details = payload[1]
    data = '{"jsonrpc":"2.0","method":"eth_getBlockByHash","params": ["' + block_hash + '",' + show_tx_details + '],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_getBlockByNumber(payload):
    payload_count = len(payload)

    if len(payload) == 2:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 2'
        })
        return payload_error

    block_parameter = payload[0]
    show_tx_details = payload[1]
    data = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params": ["' + block_parameter + '",' + show_tx_details + '],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_getBlockTransactionCountByHash(payload):
    payload_count = len(payload)

    if len(payload) == 1:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 1'
        })
        return payload_error

    block_hash = payload[0]
    data = '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params": ["' + block_hash + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


@app.route('/xrs/eth_getBlockTransactionCountByNumber', methods=['POST'])
def api_eth_getBlockTransactionCountByNumber(payload):
    payload_count = len(payload)

    if len(payload) == 1:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 1'
        })
        return payload_error

    block_parameter = payload[0]
    data = '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByNumber","params": ["' + block_parameter + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_getCode(payload):
    payload_count = len(payload)

    if len(payload) == 2:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 2'
        })
        return payload_error

    address = payload[0]
    block_parameter = payload[1]
    data = '{"jsonrpc":"2.0","method":"eth_getCode","params": ["' + address + '","' + block_parameter + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


# def api_eth_getLogs():
# WIP

def api_eth_getStorageAt(payload):
    payload_count = len(payload)

    if len(payload) == 3:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 3'
        })
        return payload_error

    address = payload[0]
    storage_position = payload[1]
    block_parameter = payload[2]
    data = '{"jsonrpc":"2.0","method":"eth_getStorageAt","params": ["' + address + '", "' + storage_position + '","' + block_parameter + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_getTransactionByBlockHashAndIndex(payload):
    payload_count = len(payload)

    if len(payload) == 2:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 2'
        })
        return payload_error

    block_hash = payload[0]
    tx_index_position = payload[1]
    data = '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params": ["' + block_hash + '","' + tx_index_position + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_getTransactionByBlockNumberAndIndex(payload):
    payload_count = len(payload)

    if len(payload) == 2:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 2'
        })
        return payload_error

    block_parameter = payload[0]
    tx_index_position = payload[1]
    data = '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params": ["' + block_parameter + '","' + tx_index_position + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_getTransactionByHash(payload):
    payload_count = len(payload)

    if len(payload) == 1:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 1'
        })
        return payload_error

    tx_hash = payload[0]
    data = '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params": ["' + tx_hash + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_getTransactionCount(payload):
    payload_count = len(payload)

    if len(payload) == 2:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 2'
        })
        return payload_error

    address = payload[0]
    block_parameter = payload[1]
    data = '{"jsonrpc":"2.0","method":"eth_getTransactionCount","params": ["' + address + '","' + block_parameter + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_getTransactionReceipt(payload):
    payload_count = len(payload)

    if len(payload) == 1:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 1'
        })
        return payload_error

    tx_hash = payload[0]
    data = '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params": ["' + tx_hash + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_getUncleByBlockHashAndIndex(payload):
    payload_count = len(payload)

    if len(payload) == 2:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 2'
        })
        return payload_error

    block_hash = payload[0]
    uncle_index_position = payload[1]
    data = '{"jsonrpc":"2.0","method":"eth_getUncleByBlockHashAndIndex","params": ["' + block_hash + '","' + uncle_index_position + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_getUncleByBlockNumberAndIndex(payload):
    payload_count = len(payload)

    if len(payload) == 2:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 2'
        })
        return payload_error

    block_parameter = payload[0]
    uncle_index_position = payload[1]
    data = '{"jsonrpc":"2.0","method":"eth_getUncleByBlockNumberAndIndex","params": ["' + block_parameter + '","' + uncle_index_position + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_getUncleCountByBlockHash(payload):
    payload_count = len(payload)

    if len(payload) == 1:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 1'
        })
        return payload_error

    block_hash = payload[0]
    data = '{"jsonrpc":"2.0","method":"eth_getUncleCountByBlockHash","params": ["' + block_hash + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_getUncleCountByBlockNumber(payload):
    payload_count = len(payload)

    if len(payload) == 1:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 1'
        })
        return payload_error

    block_parameter = payload[0]
    data = '{"jsonrpc":"2.0","method":"eth_getUncleCountByBlockNumber","params": ["' + block_parameter + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_getWork():
    data = '{"jsonrpc":"2.0","method":"eth_getWork","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def api_eth_hashrate():
    data = '{"jsonrpc":"2.0","method":"eth_hashrate","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def api_eth_mining():
    data = '{"jsonrpc":"2.0","method":"eth_mining","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def api_eth_protocolVersion():
    data = '{"jsonrpc":"2.0","method":"eth_protocolVersion","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def api_eth_sendRawTransaction(payload):
    payload_count = len(payload)

    if len(payload) == 1:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 1'
        })
        return payload_error

    tx_data = payload[0]
    data = '{"jsonrpc":"2.0","method":"eth_sendRawTransaction","params": ["' + tx_data + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_submitWork(payload):
    payload_count = len(payload)

    if len(payload) == 3:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 3'
        })
        return payload_error

    nonce = payload[0]
    pow_hash = payload[1]
    mix_digest = payload[2]
    data = '{"jsonrpc":"2.0","method":"eth_submitWork","params": ["' + nonce + '","' + pow_hash + '","' + mix_digest + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_syncing():
    data = '{"jsonrpc":"2.0","method":"eth_syncing","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def api_eth_newBlockFilter():
    data = '{"jsonrpc":"2.0","method":"eth_newBlockFilter","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def api_eth_newFilter(payload):
    payload_count = len(payload)

    if len(payload) == 4:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 4'
        })
        return payload_error

    fromBlock = payload[0]
    toBlock = payload[1]
    address = payload[2]
    topics = payload[3]
    data = '{"jsonrpc":"2.0","method":"eth_newFilter","params":[{"fromBlock":"' + fromBlock + '","toBlock":"' + toBlock + '","address":"' + address + '","topics":' + topics + '}],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_newPendingTransactionFilter():
    data = '{"jsonrpc":"2.0","method":"eth_newPendingTransactionFilter","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def api_eth_getFilterChanges(payload):
    payload_count = len(payload)

    if len(payload) == 1:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 1'
        })
        return payload_error

    filter_id = payload[0]
    data = '{"jsonrpc":"2.0","method":"eth_getFilterChanges","params": ["' + filter_id + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_getFilterLogs(payload):
    payload_count = len(payload)

    if len(payload) == 1:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 1'
        })
        return payload_error

    filter_id = payload[0]
    data = '{"jsonrpc":"2.0","method":"eth_getFilterLogs","params": ["' + filter_id + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_eth_uninstallFilter(payload):
    payload_count = len(payload)

    if len(payload) == 1:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 1'
        })
        return payload_error

    filter_id = payload[0]
    data = '{"jsonrpc":"2.0","method":"eth_uninstallFilter","params": ["' + filter_id + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


# def api_eth_subscribe():
# WIP

def api_eth_unsubscribe(payload):
    payload_count = len(payload)

    if len(payload) == 1:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 1'
        })
        return payload_error

    subscription_id = payload[0]
    data = '{"jsonrpc":"2.0","method":"eth_unsubscribe","params": ["' + subscription_id + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_net_listening():
    data = '{"jsonrpc":"2.0","method":"net_listening","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def api_net_peerCount():
    data = '{"jsonrpc":"2.0","method":"net_peerCount","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def api_net_version():
    data = '{"jsonrpc":"2.0","method":"net_version","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def api_web3_clientVersion():
    data = '{"jsonrpc":"2.0","method":"web3_clientVersion","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def api_web3_sha3(payload):
    payload_count = len(payload)

    if len(payload) == 1:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 1'
        })
        return payload_error

    sha3_data = payload[0]
    data = '{"jsonrpc":"2.0","method":"web3_sha3","params": ["' + sha3_data + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_parity_subscribe():
    pass


def api_parity_unsubscribe(payload):
    payload_count = len(payload)

    if len(payload) == 1:
        print(payload)
    else:
        payload_error = jsonify({
            'code': 1025,
            'error': 'Received parameters count ' + str(payload_count) + ' do not match expected 1'
        })
        return payload_error

    subscription_id = payload[0]
    data = '{"jsonrpc":"2.0","method":"parity_unsubscribe","params": ["' + subscription_id + '"],"id":1}'

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except:
        return bad_request_error


def api_parity_allTransactionHashes():
    data = '{"jsonrpc":"2.0","method":"parity_allTransactionHashes","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def api_parity_allTransactions():
    data = '{"jsonrpc":"2.0","method":"parity_allTransactions","params": [],"id":1}'

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def switchcase(requestjson):
    switcher = {
        'eth_blockNumber': api_eth_blockNumber,
        'eth_call': api_eth_call,
        'eth_chainId': api_eth_chainId,
        'eth_estimateGas': api_eth_estimateGas,
        'eth_gasPrice': api_eth_gasPrice,
        'eth_getBalance': api_eth_getBalance,
        'eth_getBlockByHash': api_eth_getBlockByHash,
        'eth_getBlockByNumber': api_eth_getBlockByNumber,
        'eth_getBlockTransactionCountByHash': api_eth_getBlockTransactionCountByHash,
        'eth_getBlockTransactionCountByNumber': api_eth_getBlockTransactionCountByNumber,
        'eth_getCode': api_eth_getCode,
        'eth_getStorageAt': api_eth_getStorageAt,
        'eth_getTransactionByBlockHashAndIndex': api_eth_getTransactionByBlockHashAndIndex,
        'eth_getTransactionByBlockNumberAndIndex': api_eth_getTransactionByBlockNumberAndIndex,
        'eth_getTransactionByHash': api_eth_getTransactionByHash,
        'eth_getTransactionCount': api_eth_getTransactionCount,
        'eth_getTransactionReceipt': api_eth_getTransactionReceipt,
        'eth_getUncleByBlockHashAndIndex': api_eth_getUncleByBlockHashAndIndex,
        'eth_getUncleByBlockNumberAndIndex': api_eth_getUncleByBlockNumberAndIndex,
        'eth_getUncleCountByBlockHash': api_eth_getUncleCountByBlockHash,
        'eth_getUncleCountByBlockNumber': api_eth_getUncleCountByBlockNumber,
        'eth_getWork': api_eth_getWork,
        'eth_hashrate': api_eth_hashrate,
        'eth_mining': api_eth_mining,
        'eth_protocolVersion': api_eth_protocolVersion,
        'eth_sendRawTransaction': api_eth_sendRawTransaction,
        'eth_submitWork': api_eth_submitWork,
        'eth_syncing': api_eth_syncing,
        'eth_newBlockFilter': api_eth_newBlockFilter,
        'eth_newFilter': api_eth_newFilter,
        'eth_newPendingTransactionFilter': api_eth_newPendingTransactionFilter,
        'eth_getFilterChanges': api_eth_getFilterChanges,
        'eth_getFilterLogs': api_eth_getFilterLogs,
        'eth_uninstallFilter': api_eth_uninstallFilter,
        'eth_unsubscribe': api_eth_unsubscribe,
        'net_listening': api_net_listening,
        'net_peerCount': api_net_peerCount,
        'net_version': api_net_version,
        'web3_clientVersion': api_web3_clientVersion,
        'web3_sha3': api_web3_sha3,
        'parity_allTransactionHashes': api_parity_allTransactionHashes,
        'parity_allTransactions': api_parity_allTransactions,
    }

    func = switcher.get(requestjson['method'], {})
    params = requestjson['params']

    if len(params) > 0:
        return func(params)
    else:
        return func()


@app.route('/', methods=['POST'])
def main():
    payload = request.json

    return switchcase(payload)


# Web Server is listening on 0.0.0.0:80
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
