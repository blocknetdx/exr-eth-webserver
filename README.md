# ethereum-webserver

* For use with Blocknet's XRouter Proxy Container (https://hub.docker.com/r/blocknetdx/xrouterproxy/)

---

# Docker Setup (Blocknet XRouter Proxy Container w/ Ethereum Web Server Container (Blocknet Service Node required)

* Install Docker

* Create proxy container config `uwsgi.ini` and place in a directory that can be shared with the blocknetdx/xrouterproxy docker container
  * Edit config template `uwsgi.ini` from this repo to your local settings
  * Set `URL_CustomXCloudPlugin_HOSTIP` and `URL_CustomXCloudPlugin_PORT` to your local settings
  
* Download xrouterproxy image: `docker pull blocknetdx/xrouterproxy:0.3.3` (or latest tag)

* Start xrouterproxy container: `docker run -d --name xrproxy -p 9090:80 -v=/location/of/uwsgi/config/file/directory:/opt/uwsgi/conf blocknetdx/xrouterproxy:0.3.3`
  * Start container: `docker start xrproxy`
  * Stop container: `docker stop xrproxy`

* Download .zip or use Git (https://github.com/Aderks/ethereum-webserver.git)
  * Extract locally
  
* Edit `ethereum.py` and point `url = 'http://[ip]:[port]'` to your Ethereum node
  * Infura support: `url = 'https://mainnet.infura.io/v3/<api_key>'`
  
* Open a CLI and change directory to where `ethereum-webserver` is located

* Build image: `docker build -t ethereum-webserver C:\ethereum-webserver`
  * Edit `Dockerfile` `EXPOSE 5000` if you changed the port in ethereum.py `app.run()`

* Start etherum-webserver container: `docker run -d --name eth-webserver -p 5000:5000 ethereum-webserver:latest`
  * Change `-p 5000:5000` if port was changed in ethereum.py
  * Start container: `docker start eth-webserver`
  * Stop container: `docker stop eth-webserver`

* cURL examples:
  * `curl -H "Accept: application/json" -H "Content-Type: application/json" -d '["0xc94770007dda54cF92009BFF0dE90c06F603a09f","latest"]' 127.0.0.1:9090/xrs/eth_getBalance`

  * `curl -H "Accept: application/json" -H "Content-Type: application/json" -d '[]' 127.0.0.1:9090/xrs/eth_blockNumber`

---

# Non-Docker Setup (Flask Web Server only, Blocknet Service Node not required)

* Download .zip or use Git (https://github.com/Aderks/ethereum-webserver.git)
  * Extract locally
  
* Edit `ethereum.py` and point `url = 'http://[ip]:[port]'` to your Ethereum node
  * Infura support: `url = 'https://mainnet.infura.io/v3/<api_key>'`
  
* Install required dependencies: `pip install -r requirements.txt`
  
* Run `ethereum.py` to start the Flask Web Server

* cURL example: `curl -H "Accept: application/json" -H "Content-Type: application/json" -d '[]' 127.0.0.1:5000/xrs/eth_blockNumber`

---

**To Do:**

* Optional parameters
* XR payments
