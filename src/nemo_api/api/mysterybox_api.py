# coding: utf-8

from nemo_api.client.api_client import ApiClient
from nemo_api.status import STATUS as status
from nemo_api.function import py2json

class MysteryboxApi(object):

    def __init__(self, api_client: ApiClient=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    async def mint(
        self,
        box_id: str,
        recipient: str,
        metadata: dict,
        callback: str,
        json_fomater = py2json
    ):
        auth_settings = ['apiv2']
        body_params = {
            'recipient': recipient,
            'data': json_fomater(metadata),
            'callback': callback,
            'boxid': box_id
        }
        res = await self.api_client.call_api(
            resource_path='/mysterybox/mint',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='str',
        )
        return res
    
    def build_batch_mint_data(
        self,
        box_ids: list[str],
        recipients: list[str],
        metadatas: list[dict],
        callbacks: list[str],
        json_fomater = py2json
    ):
        ret = []
        for index, boxid in enumerate(box_ids):
            ret.append({
                'recipient': recipients[index],
                'data': json_fomater(metadatas[index]),
                'callback': callbacks[index],
                'boxid': boxid
            })
        return ret

    async def mints(
        self,
        boxs: list[dict],
        json_fomater = py2json
    ):
        auth_settings = ['apiv2']
        body_params = {
            'boxs': json_fomater(boxs)
        }
        res = await self.api_client.call_api(
            resource_path='/mysterybox/mints',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='list[object]',
        )
        return res