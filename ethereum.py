from flask import Flask, url_for, jsonify, request
import requests
import json
app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

url = 'http://[ip]:[port]' #example: 'http://localhost:8545'
#url = 'https://mainnet.infura.io/v3/<api_key>' #infura testing
headers = {'Content-Type': 'application/json',}

@app.route('/xrs/eth_accounts', methods = ['POST'])
def api_eth_accounts():

	data = '{"jsonrpc":"2.0","method":"eth_accounts","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_blockNumber', methods = ['POST'])
def api_eth_blockNumber():

	data = '{"jsonrpc":"2.0","method":"eth_blockNumber","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_call', methods = ['POST'])
def api_eth_call():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 7:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 7'

	From = payload[0]
	to = payload[1]
	gas = payload[2]
	gasPrice = payload[3]
	value = payload[4]
	eth_data = payload[5]
	block_parameter = payload[6]
	data = '{"jsonrpc":"2.0","method":"eth_call","params": [{"from": "'+From+'","to": "'+to+'","gas": "'+gas+'","gasPrice": "'+gasPrice+'","value": "'+value+'","data": "'+eth_data+'"}, "'+block_parameter+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_chainId', methods = ['POST'])
def api_eth_chainId():

	data = '{"jsonrpc":"2.0","method":"eth_chainId","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_estimateGas', methods = ['POST'])
def api_eth_estimateGas():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 6:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 6'

	From = payload[0]
	to = payload[1]
	gas = payload[2]
	gasPrice = payload[3]
	value = payload[4]
	eth_data = payload[5]
	data = '{"jsonrpc":"2.0","method":"eth_estimateGas","params": [{"from": "'+From+'","to": "'+to+'","gas": "'+gas+'","gasPrice": "'+gasPrice+'","value": "'+value+'","data": "'+eth_data+'"}],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_gasPrice', methods = ['POST'])
def api_eth_gasPrice():

	data = '{"jsonrpc":"2.0","method":"eth_gasPrice","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()
	
	
@app.route('/xrs/eth_getBalance', methods = ['POST'])
def api_eth_getBalance():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 2:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 2'

	address = payload[0]
	block_parameter = payload[1]
	data = '{"jsonrpc":"2.0","method":"eth_getBalance","params": ["'+address+'","'+block_parameter+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getBlockByHash', methods = ['POST'])
def api_eth_getBlockByHash():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 2:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 2'

	block_hash = payload[0]
	show_tx_details = payload[1]
	data = '{"jsonrpc":"2.0","method":"eth_getBlockByHash","params": ["'+block_hash+'",'+show_tx_details+'],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getBlockByNumber', methods = ['POST'])
def api_eth_getBlockByNumber():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 2:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 2'

	block_parameter = payload[0]
	show_tx_details = payload[1]
	data = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params": ["'+block_parameter+'",'+show_tx_details+'],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getBlockTransactionCountByHash', methods = ['POST'])
def api_eth_getBlockTransactionCountByHash():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 1:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 1'

	block_hash = payload[0]
	data = '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params": ["'+block_hash+'"],"id":1}'
	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getBlockTransactionCountByNumber', methods = ['POST'])
def api_eth_getBlockTransactionCountByNumber():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 1:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 1'

	block_parameter = payload[0]
	data = '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByNumber","params": ["'+block_parameter+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getCode', methods = ['POST'])
def api_eth_getCode():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 2:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 2'

	address = payload[0]
	block_parameter = payload[1]
	data = '{"jsonrpc":"2.0","method":"eth_getCode","params": ["'+address+'","'+block_parameter+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getLogs', methods = ['POST'])
#def api_eth_getLogs():
#WIP


@app.route('/xrs/eth_getStorageAt', methods = ['POST'])
def api_eth_getStorageAt():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 3:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 3'

	address = payload[0]
	storage_position = payload[1]
	block_parameter = payload[2]
	data = '{"jsonrpc":"2.0","method":"eth_getStorageAt","params": ["'+address+'", "'+storage_position+'","'+block_parameter+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getTransactionByBlockHashAndIndex', methods = ['POST'])
def api_eth_getTransactionByBlockHashAndIndex():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 2:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 2'

	block_hash = payload[0]
	tx_index_position = payload[1]
	data = '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params": ["'+block_hash+'","'+tx_index_position+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getTransactionByBlockNumberAndIndex', methods = ['POST'])
def api_eth_getTransactionByBlockNumberAndIndex():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 2:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 2'

	block_parameter = payload[0]
	tx_index_position = payload[1]
	data = '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params": ["'+block_parameter+'","'+tx_index_position+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getTransactionByHash', methods = ['POST'])
def api_eth_getTransactionByHash():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 1:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 1'

	tx_hash = payload[0]
	data = '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params": ["'+tx_hash+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getTransactionCount', methods = ['POST'])
def api_eth_getTransactionCount():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 2:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 2'

	address = payload[0]
	block_parameter = payload[1]
	data = '{"jsonrpc":"2.0","method":"eth_getTransactionCount","params": ["'+address+'","'+block_parameter+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getTransactionReceipt', methods = ['POST'])
def api_eth_getTransactionReceipt():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 1:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 1'

	tx_hash = payload[0]
	data = '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params": ["'+tx_hash+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getUncleByBlockHashAndIndex', methods = ['POST'])
def api_eth_getUncleByBlockHashAndIndex():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 2:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 2'

	block_hash = payload[0]
	uncle_index_position = payload[1]
	data = '{"jsonrpc":"2.0","method":"eth_getUncleByBlockHashAndIndex","params": ["'+block_hash+'","'+uncle_index_position+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getUncleByBlockNumberAndIndex', methods = ['POST'])
def api_eth_getUncleByBlockNumberAndIndex():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 2:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 2'

	block_parameter = payload[0]
	uncle_index_position = payload[1]
	data = '{"jsonrpc":"2.0","method":"eth_getUncleByBlockNumberAndIndex","params": ["'+block_parameter+'","'+uncle_index_position+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getUncleCountByBlockHash', methods = ['POST'])
def api_eth_getUncleCountByBlockHash():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 1:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 1'

	block_hash = payload[0]
	data = '{"jsonrpc":"2.0","method":"eth_getUncleCountByBlockHash","params": ["'+block_hash+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getUncleCountByBlockNumber', methods = ['POST'])
def api_eth_getUncleCountByBlockNumber():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 1:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 1'

	block_parameter = payload[0]    
	data = '{"jsonrpc":"2.0","method":"eth_getUncleCountByBlockNumber","params": ["'+block_parameter+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getWork', methods = ['POST'])
def api_eth_getWork():

	data = '{"jsonrpc":"2.0","method":"eth_getWork","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_hashrate', methods = ['POST'])
def api_eth_hashrate():

	data = '{"jsonrpc":"2.0","method":"eth_hashrate","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_mining', methods = ['POST'])
def api_eth_mining():

	data = '{"jsonrpc":"2.0","method":"eth_mining","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_protocolVersion', methods = ['POST'])
def api_eth_protocolVersion():

	data = '{"jsonrpc":"2.0","method":"eth_protocolVersion","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_sendRawTransaction', methods = ['POST'])
def api_eth_sendRawTransaction():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 1:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 1'

	tx_data = payload[0]
	data = '{"jsonrpc":"2.0","method":"eth_sendRawTransaction","params": ["'+tx_data+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_submitWork', methods = ['POST'])
def api_eth_submitWork():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 3:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 3'

	nonce = payload[0]
	pow_hash = payload[1]
	mix_digest = payload[2]
	data = '{"jsonrpc":"2.0","method":"eth_submitWork","params": ["'+nonce+'","'+pow_hash+'","'+mix_digest+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_syncing', methods = ['POST'])
def api_eth_syncing():

	data = '{"jsonrpc":"2.0","method":"eth_syncing","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_newBlockFilter', methods = ['POST'])
def api_eth_newBlockFilter():

	data = '{"jsonrpc":"2.0","method":"eth_newBlockFilter","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_newFilter', methods = ['POST'])
def api_eth_newFilter():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 4:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 4'

	fromBlock = payload[0]
	toBlock = payload[1]
	address = payload[2]
	topics = payload[3]
	data = '{"jsonrpc":"2.0","method":"eth_newFilter","params":[{"fromBlock":"'+fromBlock+'","toBlock":"'+toBlock+'","address":"'+address+'","topics":'+topics+'}],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_newPendingTransactionFilter', methods = ['POST'])
def api_eth_newPendingTransactionFilter():

	data = '{"jsonrpc":"2.0","method":"eth_newPendingTransactionFilter","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getFilterChanges', methods = ['POST'])
def api_eth_getFilterChanges():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 1:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 1'

	filter_id = payload[0]
	data = '{"jsonrpc":"2.0","method":"eth_getFilterChanges","params": ["'+filter_id+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_getFilterLogs', methods = ['POST'])
def api_eth_getFilterLogs():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 1:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 1'

	filter_id = payload[0]
	data = '{"jsonrpc":"2.0","method":"eth_getFilterLogs","params": ["'+filter_id+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_uninstallFilter', methods = ['POST'])
def api_eth_uninstallFilter():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 1:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 1'

	filter_id = payload[0]
	data = '{"jsonrpc":"2.0","method":"eth_uninstallFilter","params": ["'+filter_id+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/eth_subscribe', methods = ['POST'])
#def api_eth_subscribe():
#WIP


@app.route('/xrs/eth_unsubscribe', methods = ['POST'])
def api_eth_unsubscribe():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 1:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 1'

	subscription_id = payload[0]
	data = '{"jsonrpc":"2.0","method":"eth_unsubscribe","params": ["'+subscription_id+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/net_listening', methods = ['POST'])
def api_net_listening():

	data = '{"jsonrpc":"2.0","method":"net_listening","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/net_peerCount', methods = ['POST'])
def api_net_peerCount():

	data = '{"jsonrpc":"2.0","method":"net_peerCount","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/net_version', methods = ['POST'])
def api_net_version():

	data = '{"jsonrpc":"2.0","method":"net_version","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/web3_clientVersion', methods = ['POST'])
def api_web3_clientVersion():

	data = '{"jsonrpc":"2.0","method":"web3_clientVersion","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/web3_sha3', methods = ['POST'])
def api_web3_sha3():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 1:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 1'

	sha3_data = payload[0]
	data = '{"jsonrpc":"2.0","method":"web3_sha3","params": ["'+sha3_data+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/parity_subscribe', methods = ['POST'])
#def api_parity_subscribe():
#WIP


@app.route('/xrs/parity_unsubscribe', methods = ['POST'])
def api_parity_unsubscribe():

	payload = request.json
	payload_count = len(payload)

	if len(payload) == 1:
		print (payload)
	else:
		return 'Error: Received parameters count '+str(payload_count)+' do not match expected 1'

	subscription_id = payload[0]
	data = '{"jsonrpc":"2.0","method":"parity_unsubscribe","params": ["'+subscription_id+'"],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/parity_allTransactionHashes', methods = ['POST'])
def api_parity_allTransactionHashes():

	data = '{"jsonrpc":"2.0","method":"parity_allTransactionHashes","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


@app.route('/xrs/parity_allTransactions', methods = ['POST'])
def api_parity_allTransactions():

	data = '{"jsonrpc":"2.0","method":"parity_allTransactions","params": [],"id":1}'

	response = requests.post(url, headers=headers, data=data)
	return response.json()


if __name__ == '__main__':
	#app.run()
	app.run(host= '0.0.0.0')
