# coding: utf-8

from nemo_api.client.api_client import ApiClient
from nemo_api.status import STATUS as status

class NemoIdApi(object):

    def __init__(self, api_client: ApiClient=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    async def login(self, code, code_verifier, redirect_uri):
        auth_settings = ['apiv2']
        body_params = {
            'code': code,
            'code_verifier': code_verifier,
            'redirect_uri': redirect_uri
        }
        res = await self.api_client.call_api(
            resource_path='/nemoid/login',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='NemoIdAccount'
        )
        return res

    async def user_info(self, access_token):
        auth_settings = ['apiv2']
        body_params = {
            'access_token': access_token
        }
        res = await self.api_client.call_api(
            resource_path='/nemoid/user_info',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='NemoIdAccount'
        )
        return res

    async def relogin(self, refresh_token, code_verifier):
        auth_settings = ['apiv2']
        body_params = {
            'refresh_token': refresh_token,
            'code_verifier': code_verifier
        }
        res = await self.api_client.call_api(
            resource_path='/nemoid/relogin',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='NemoIdAccount'
        )
        return res