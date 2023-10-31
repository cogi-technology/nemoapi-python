# coding: utf-8

from nemo_api.client.api_client import ApiClient
from nemo_api.status import STATUS as status

class NftApi(object):

    def __init__(self, api_client: ApiClient=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    async def mint(self, recipient: str, metadata: dict, callback: str):
        auth_settings = ['apiv2']
        body_params = {
            'recipient': recipient,
            'data': metadata,
            'callback': callback
        }
        res = await self.api_client.call_api(
            resource_path='/nft/mint',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='str',
        )
        return res

    async def request_mint(self, recipient: str, metadata: dict, callback: str):
        auth_settings = ['apiv2']
        body_params = {
            'recipient': recipient,
            'data': metadata,
            'callback': callback
        }
        res = await self.api_client.call_api(
            resource_path='/nft/request_mint',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='str',
        )
        return res
    
    
    async def mints(self, payload: list[dict]):
        auth_settings = ['apiv2']
        res = await self.api_client.call_api(
            resource_path='/nft/mints',
            method='POST',
            body=payload,
            auth_settings=auth_settings,
            response_type='list[object]',
        )
        return res