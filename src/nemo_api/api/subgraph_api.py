# coding: utf-8

from nemo_api.client.api_client import ApiClient

class SubgraphApi(object):

    def __init__(self, api_client: ApiClient=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    async def call(self, params: dict):
        #TODO: variables, query
        auth_settings = ['apiv2']
        res = await self.api_client.call_api(
            resource_path='/subgraph/call',
            method='POST',
            body=params,
            auth_settings=auth_settings,
        )
        return res

    async def getTotalVolume(self, params: dict):
        #TODO: params is variables
        auth_settings = ['apiv2']
        res = await self.api_client.call_api(
            resource_path='/subgraph/getTotalVolume',
            method='POST',
            body=params,
            auth_settings=auth_settings,
            response_type='dict(str, str)'
        )
        return res