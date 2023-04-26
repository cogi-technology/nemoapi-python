# coding: utf-8

from nemo_api.client.api_client import ApiClient
from nemo_api.status import STATUS as status
from nemo_api.function import py2json

class LandApi(object):

    def __init__(self, api_client: ApiClient=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    async def mint(
        self,
        recipient: str,
        land_id: str,
        level: str,
        land_x: str,
        land_y: str,
        metadata: dict,
        callback: str,
        json_fomater = py2json
    ):
        auth_settings = ['apiv2']
        body_params = {
            'recipient': recipient,
            'data': json_fomater(metadata),
            'callback': callback,
            'landid': land_id,
            'level': level,
            'land_x': land_x,
            'land_y': land_y
        }
        res = await self.api_client.call_api(
            resource_path='/land/mint',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='str',
        )
        return res

    async def request_mint(
        self,
        recipient: str,
        land_id: str,
        level: str,
        land_x: str,
        land_y: str,
        metadata: dict,
        callback: str,
        json_fomater = py2json
    ):
        auth_settings = ['apiv2']
        body_params = {
            'recipient': recipient,
            'data': json_fomater(metadata),
            'callback': callback,
            'landid': land_id,
            'level': level,
            'land_x': land_x,
            'land_y': land_y
        }
        res = await self.api_client.call_api(
            resource_path='/land/request_mint',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='str',
        )
        return res
    
    def build_batch_mint_data(
        self,
        recipients: list[str],
        land_ids: list[str],
        levels: list[str],
        land_xs: list[str],
        land_ys: list[str],
        metadatas: list[dict],
        callbacks: list[str],
        json_fomater = py2json
    ):
        ret = []
        for index, recipient in enumerate(recipients):
            ret.append({
                'recipient': recipient,
                'data': json_fomater(metadatas[index]),
                'callback': callbacks[index],
                'landid': land_ids[index],
                'level': levels[index],
                'land_x': land_xs[index],
                'land_y': land_ys[index]
            })
        
        return ret

    def build_batch_cancelbuys_data(self, accounts: list[str], cids: list[str]):
        ret = []
        for index, account in enumerate(accounts):
            ret.append({
                "account": account,
                "cid": cids[index]
            })
        return ret
    
    async def mints(self, lands: list[dict], json_fomater = py2json):
        auth_settings = ['apiv2']
        body_params = { 'lands': json_fomater(lands) }
        res = await self.api_client.call_api(
            resource_path='/land/mints',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='list[object]',
        )
        return res
    
    async def request_mints(self, lands: list[dict], json_fomater = py2json):
        auth_settings = ['apiv2']
        body_params = { 'lands': json_fomater(lands) }
        res = await self.api_client.call_api(
            resource_path='/land/request_mints',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='list[object]',
        )
        return res
    
    async def request_cancelbuys(self, lands: list[dict]):
        #TODO lands: list[{account, cid}]
        auth_settings = ['apiv2']
        body_params = { 'lands': lands }
        res = await self.api_client.call_api(
            resource_path='/land/request_cancelbuys',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='list[object]',
        )
        return res