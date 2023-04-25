# coding: utf-8

from nemo_api.client.api_client import ApiClient
from nemo_api.status import STATUS as status

class OnchainApi(object):

    def __init__(self, api_client: ApiClient=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    async def scan_tx(self, chain_id: int, hashes: list[str]):
        auth_settings = ['apiv2']
        body_params = {
            'chain_id': chain_id,
            'hashes': hashes
        }
        res = await self.api_client.call_api(
            resource_path='/onchain/scan_tx',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
        )
        try:
            return status(res.get('status'))
        except:
            return res