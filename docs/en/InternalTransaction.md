# InternalTransaction

Transaction information is provided when requesting a charge or an award.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | The Ethereum address of the user | [optional] 
**tx_hash** | **str** | A unique identifier that is used to track and verify transactions | [optional] 
**amount** | **str** | The number of tokens used in the transaction | [optional] 
**kind** | **int** | The types of transaction may include withdrawals, deposits, and more. [[See status]](./src/nemo_api/status.py) | [optional] 

[[Back to Model list]](./README.md#documentation-for-models) [[Back to API list]](./README.md#documentation-for-api-endpoints) [[Back to README]](./README.md)


