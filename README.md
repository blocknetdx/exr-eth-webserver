# ethereum-webserver (Nginx & uWSGI)

* For use with Blocknet's XRouter Proxy Container (https://hub.docker.com/r/blocknetdx/xrouterproxy/)

# **Ethereum Web Server running through Blocknet's XRouter Proxy**

## **Prerequisites**

* Parity or Geth Ethereum Node 
   * Archival node is preferred
   * If full node is used some calls will not work
   * Infura support is available
* Docker installed
* Blocknet Service Node

## **Ethereum Web Server Setup**

* Download .zip or use Git (https://github.com/Aderks/ethereum-webserver.git)
  * Extract locally
  * Directory structure: `Dockerfile, ethereum.py, requirements.txt, start.sh`
  
* Edit `ethereum.py` and point `url = 'http://[ip]:[port]'` to your Ethereum node
  * Infura support: `url = 'https://mainnet.infura.io/v3/<api_key>'`
  
* Open a CLI and change directory to where `ethereum-webserver` is located

* Build image: `docker build --build-arg cores=8 -t ethereum-webserver .`
  * Change `--build-arg cores=` to adjust # of processes

* Run etherum-webserver container: `docker run -d --name ethereum-webserver -p 80:80 ethereum-webserver:latest`
  
* Quick commands:  
  * Start container: `docker start ethereum-webserver`
  * Stop container: `docker stop ethereum-webserver`
  * View logs: `docker logs ethereum-webserver`
  * Tail logs: `docker logs -f ethereum-webserver`
  * Gain access inside container: `docker exec -it ethereum-webserver /bin/bash`

## **Blocknet XRouter Proxy Setup**

* Download xrouterproxy image: `docker pull blocknetdx/xrouterproxy:0.3.3` (or latest tag)

* Create xrproxy container config `uwsgi.ini` and place in a directory that can be shared with the blocknetdx/xrouterproxy docker container
  * Edit config template `xrproxy_uwsgi.ini` from this repo to your local settings
    * Set `SERVICENODE_PRIVKEY=` (retrieve from `servicenodestatus`)
    * Set `URL_CustomXCloudPlugin_HOSTIP=` & `URL_CustomXCloudPlugin_PORT=` to your local settings
  * Rename [xrproxy_uwsgi.ini](https://github.com/Aderks/ethereum-webserver/blob/master/xrproxy_uwsgi.ini) to `uwsgi.ini`

* Run xrouterproxy container: `docker run -d --name xrproxy -p 9090:80 -v=/location/of/uwsgi/config/file/directory:/opt/uwsgi/conf blocknetdx/xrouterproxy:0.3.3`

* Quick Commands:
  * Start container: `docker start xrproxy`
  * Stop container: `docker stop xrproxy`

* cURL examples:
  * `curl -H "Accept: application/json" -H "Content-Type: application/json" -d '["0xc94770007dda54cF92009BFF0dE90c06F603a09f","latest"]' 127.0.0.1:9090/xrs/eth_getBalance`

  * `curl -H "Accept: application/json" -H "Content-Type: application/json" -d '[]' 127.0.0.1:9090/xrs/eth_blockNumber`

---

# Non-Docker Setup (Flask Web Server only, Blocknet Service Node not required)
**Recommended for developmental use only**

* Download .zip or use Git (https://github.com/Aderks/ethereum-webserver.git)
  * Extract locally
  
* Edit `ethereum.py` and point `url = 'http://[ip]:[port]'` to your Ethereum node
  * Infura support: `url = 'https://mainnet.infura.io/v3/<api_key>'`
  
* Install required dependencies: `pip install -r requirements.txt`
  
* Run `ethereum.py` to start the Flask Web Server

* cURL example: `curl -H "Accept: application/json" -H "Content-Type: application/json" -d '[]' 127.0.0.1:80/xrs/eth_blockNumber`

---

**To Do:**

* ETH calls: `eth_getLogs`, `eth_subscribe`, `parity_subscribe`
* Optional parameters: `eth_call`, `eth_estimateGas`, `eth_getLogs`, `eth_newFilter`
* XR payments
