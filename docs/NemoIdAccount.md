# NemoIdAccount

Account's hotwallet information.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub** | **str** | This is an identifier for the user that is unique among all NEMO ID accounts | [optional] 
**email** | **str** | The email address of the account | [optional] 
**email_verified** | **bool** | Whether an email has been verified | [optional] 
**name** | **str** | Username | [optional] 
**gender** | **str** | Gender | [optional] 
**birthday** | **str** | Birthday | [optional] 
**profile_picture** | **str** | Link to the profile picture of the account | [optional] 
**public_key** | **str** | The public key used to authenticate the JSON-RPC request | [optional] 
**redirect_uri** | **str** | Redirect URI | [optional] 
**client_id** | **str** | Client ID | [optional] 
**access_token** | **str** | Token used to access the service | [optional] 
**expires_in** | **int** | Time in seconds for the access token's lifespan | [optional] 
**id_token** | **str** | A JWT containing identifying information about the user signed by NEMO ID | [optional] 
**refresh_token** | **str** | Refresh token | [optional] 
**token_type** | **str** | Token type | [optional] 
**google_two_factor_authentication** | **bool** | Whether two-factor authentication is enabled | [optional] 
**fund_password** | **bool** | Whether the fund password is enabled | [optional] 
**signature** | **object** | The signature response from the server, which is used for JSON-RPC requests | [optional] 
**nemo_address** | **str** | The Ethereum address of NemoWallet | [optional] 
**wallet_address** | **list** | The Ethereum addresses of the MetaMask wallets are linked" | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


