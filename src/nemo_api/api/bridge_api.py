# coding: utf-8

from nemo_api.client.api_client import ApiClient
from nemo_api.exceptions import ApiValueError

class BridgeApi(object):

    def __init__(self, api_client: ApiClient=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    async def pause(self, networks: list[str]=None, chain_ids: list[int]=None):
        auth_settings = ['apiv2']
        body_params = {}
    
        if networks is not None:
            body_params['networks'] = networks
        if chain_ids is not None:
            body_params['chainIds'] = chain_ids
        
        res = await self.api_client.call_api(
            resource_path='/bridge/pause',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='list[object]'
        )
        return res

    async def unpause(self, networks: list[str]=None, chain_ids: list[int]=None):
        auth_settings = ['apiv2']
        body_params = {}
    
        if networks is not None:
            body_params['networks'] = networks
        if chain_ids is not None:
            body_params['chainIds'] = chain_ids
        
        res = await self.api_client.call_api(
            resource_path='/bridge/unpause',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='list[object]'
        )
        return res

    async def block_token(self, token: str, network: str=None, chain_id: int=None):
        auth_settings = ['apiv2']
        body_params = {'token':token}
        if network is not None:
            body_params['network'] = network
        elif chain_id is not None:
            body_params['chainId'] = chain_id
        else:
            raise ApiValueError("Network or chain id is requested.")
        
        res = await self.api_client.call_api(
            resource_path='/bridge/block_token',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='list[object]'
        )
        return res

    async def unblock_token(self, token: str, network: str=None, chain_id: int=None):
        auth_settings = ['apiv2']
        body_params = {'token':token}
        if network is not None:
            body_params['network'] = network
        elif chain_id is not None:
            body_params['chainId'] = chain_id
        else:
            raise ApiValueError("Network or chain id is requested.")
        
        res = await self.api_client.call_api(
            resource_path='/bridge/unblock_token',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='list[object]'
        )
        return res