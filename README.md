# nemo-api
Welcome to nemoverse.io API

APIv2 provides mint, charge, award... operations. There are private APIs which needs authentication.

## Versioning

Trying our best to follow the [semantic versioning](https://semver.org/), while enjoying recent features
provided by programming language and libraries, from 2.0.0, one major versioning difference will be
introduced:

If extra code rewrite is required when you upgrade the SDK, such as:

- some outdated programming language version support is dropped
- API method signature has breaking changes.

**the MAJOR version will be incremented, but the MINOR and PATCH version are still following REST API's
instead of resetting to 0**, so that you can recognize it has some breaking changes, but still getting
the idea of from which REST API version the change is introduced.

For example, the previous REST API and SDK version are both 4.14.0. But if we decide to introduce
some breaking changes in SDK along with REST API 2.0.0 upgrade, then the version of next SDK release
will be 5.15.2(the MAJOR version is incremented to denote breaking changes, but the MINOR and PATCH
version are identical to REST API's instead of resetting them to 0)

If MAJOR version is incremented, make sure you read the release note on
[Releases](https://gitlab.com/nemoverse/nemo_wallet_api_python/-/releases)
page

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

You can install directly using:

```sh
pip install --user nemo-api
```

Then import the package:
```python
import nemo_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import nemo_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

Create a key pair
```sh
# Use the nemoversdk CLI to generate a key pair. The response will be a private key and a public key
nemoversesdk dsa libsodium generate
# oB13FXaa1BiEiDaUGvuj/blJwj6SRl7JjkE/ApeQf08= auVgK8gSvFOgF5zWmQ5wWhFKImyl5/ka59dcRZtzcDA=
```

```python
from __future__ import print_function
import nemo_api

KEY_ID = "<key id>"
PRIVATE_KEY = "<private key>"
PUBLIC_KEY = "<public key>"
HOST = "<host>"
ACCOUNT = "<account>"

configuration = nemo_api.ApiConfiguration(
    key_id=KEY_ID,
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    host = HOST
)

api_client = nemo_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = nemo_api.HotwalletApi(api_client)

try:
    # List currencies for lending
    api_response = api_instance.balance(ACCOUNT)
    print(api_response)
except Exception as e:
    print("Exception when calling HotwalletApi->balance: %s\n" % e)

```

For a more complete API usage example, refer to the demo application in [example](example) directory

## Documentation for API Endpoints

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*HotwalletApi* | [**balance**](docs/HotwalletApi.md#balance) | **POST** /hotwallet/balance | Account's hotwallet information
*HotwalletApi* | [**charge**](docs/HotwalletApi.md#charge) | **POST** /hotwallet/charge | Deduct balance from the user's account
*HotwalletApi* | [**award**](docs/HotwalletApi.md#award) | **POST** /hotwallet/award | Award token to user
*HotwalletApi* | [**get_allowance**](docs/HotwalletApi.md#get_allowance) | **POST** /hotwallet/get_allowance | Get user's approval for the service
*LandApi* | [**mint**](docs/LandApi.md#mint) | **POST** /land/mint | Send a transaction to mint an NFT Land and transfer it to an account, executed by the minter. Get UUID of NFT Land if successful
*LandApi* | [**request_mint**](docs/LandApi.md#request_mint) | **POST** /land/request_mint | Send a transaction to mint an NFT Land and transfer it to an account, executed by the user. Get UUID of NFT Land if successful
*LandApi* | [**mints**](docs/LandApi.md#mints) | **POST** /land/mints | Send batch transaction to mint multiple NFT Land, executed by the minter
*LandApi* | [**request_mints**](docs/LandApi.md#request_mints) | **POST** /land/request_mints | Send batch transaction to mint multiple NFT Land, executed by the user
*LandApi* | [**request_cancelbuys**](docs/LandApi.md#request_cancelbuys) | **POST** /land/request_cancelbuys | Send batch request cancel buy
*MysteryboxApi* | [**mint**](docs/MysteryboxApi.md#mint) | **POST** /mysterybox/mint | Send a transaction to mint an NFT BOX and transfer it to an account, executed by the minter. Get UUID of NFT if successful
*MysteryboxApi* | [**mints**](docs/MysteryboxApi.md#mints) | **POST** /mysterybox/mints | Send batch transaction to mint multiple NFT BOX, executed by the minter
*NemoAccountApi* | [**get_link**](docs/NemoAccountApi.md#get_link) | **POST** /account/get_link | Get a list of Metamask addresses linked to Nemo Wallet
*NemoAccountApi* | [**get_nemo_wallet**](docs/NemoAccountApi.md#get_nemo_wallet) | **POST** /account/get_nemo_wallet | Get the Nemo Wallet address that is linked from the Metamask address
*NemoIdApi* | [**login**](docs/NemoIdApi.md#login) | **POST** /nemoid/login | Login and get NemoIdAccount's information
*NemoIdApi* | [**user_info**](docs/NemoIdApi.md#user_info) | **POST** /nemoid/user_info | Get NemoIdAccount's information
*NemoIdApi* | [**relogin**](docs/NemoIdApi.md#relogin) | **POST** /nemoid/relogin | Relogin and get NemoIdAccount's information
*NftApi* | [**mint**](docs/NftApi.md#mint) | **POST** /nft/mint | Send a transaction to mint an NFT and transfer it to an account, executed by the minter. Get UUID of NFT if successful
*NftApi* | [**request_mint**](docs/NftApi.md#request_mint) | **POST** /nft/request_mint | Send a transaction to mint an NFT and transfer it to an account, executed by the user. Get UUID of NFT if successful
*SubgraphApi* | [**call**](docs/SubgraphApi.md#call) | **POST** /subgraph/call | Execute a GraphQL query on subgraph
*SubgraphApi* | [**getTotalVolume**](docs/SubgraphApi.md#getTotalVolume) | **POST** /subgraph/getTotalVolume | Calculate the total volume of the marketplace on the subgraph


## Documentation For Models

 - [AccountBalance](docs/AccountBalance.md)
 - [HotwalletAllowance](docs/HotwalletAllowance.md)
 - [InternalTransaction](docs/InternalTransaction.md)
 - [NemoIdAccount](docs/NemoIdAccount.md)


## Documentation For Authorization


## apiv2

Authentication with APIv2 private key and public key is created by [libsodium](https://libsodium.gitbook.io) or [libsecp256k1](https://github.com/bitcoin-core/secp256k1)

```bash
ACCESS_ID='/galixcity-testnet/v2/hotwallet/charge'

# UNIX timestamp in milliseconds, GMT+0
# The value is directly proportional to the number of requests made. For example, in systems that generate multiple requests simultaneously, a sequential counter must be used because ACCESS_TIME(request n+1) > ACCESS_TIME(request n).
ACCESS_TIME = $(UNIX timestamp in milliseconds)

# Body parameters in POST, PUT, and PATCH requests
# There are no body parameters in GET or DELETE requests
payload = '{"account": "0x19fbA25cf926d8502025f2E765E5bd2E986c8527","amount": "1000000"}'
message_hash = sha256($ACCESS_ID + ":" + $ACCESS_TIME + ":" + $payload)
private_key = <Private key encode bytes>
# Using ED25519 to create a signature
signature = sodium.crypto_sign($message, $private_key)
ACCESS_SIGNATURE = base64.encode($signature)
ACCESS_KEY_ID=<Receive from server after adding public key>

curl -X POST 'https://api.nemoverse.io/galixcity-testnet/v2/hotwallet/charge' \
    -H 'Access-Time: $ACCESS_TIME' \
    -H 'Access-Signature: $ACCESS_SIGNATURE' \
    -H 'Access-Key-Id: $ACCESS_KEY_ID' \
    -H 'Content-Type: application/json' \
    --data-raw $payload
```


## Author

tech@nemoverse.io


