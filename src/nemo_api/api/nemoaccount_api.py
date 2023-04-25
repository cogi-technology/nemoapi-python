# coding: utf-8

from nemo_api.client.api_client import ApiClient

class NemoAccountApi(object):

    def __init__(self, api_client: ApiClient=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    async def get_link(self, main_account: str):
        auth_settings = ['apiv2']
        body_params = {
            'main_account': main_account
        }
        res = await self.api_client.call_api(
            resource_path='/account/get_link',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='list[str]',
        )
        return res

    async def get_nemo_wallet(self, sub_account: str):
        auth_settings = ['apiv2']
        body_params = {
            'sub_account': sub_account
        }
        res = await self.api_client.call_api(
            resource_path='/account/get_nemo_wallet',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='dict(str, str)',
        )
        return res