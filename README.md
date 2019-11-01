# ethereum-webserver

* For use with Blocknet's XRouter Proxy Container (https://hub.docker.com/r/blocknetdx/xrouterproxy/)

**Example calls:**

* `curl -H "Accept: application/json" -H "Content-Type: application/json" -d '["0xc94770007dda54cF92009BFF0dE90c06F603a09f","latest"]' 127.0.0.1:9090/xrs/eth_getBalance`

* `curl -H "Accept: application/json" -H "Content-Type: application/json" -d '[]' 127.0.0.1:9090/xrs/eth_blockNumber`

**To do:**

* HTTP error handling
* Optional parameters
