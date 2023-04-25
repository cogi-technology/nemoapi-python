# coding: utf-8

from nemo_api.client.api_client import ApiClient
from nemo_api.status import STATUS as status
from typing import Union
from nemo_api.models import AccountBalance

class HotwalletApi(object):

    def __init__(self, api_client: ApiClient=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    async def balance(self, account: Union[str, AccountBalance]):
        account = account.account if isinstance(account, AccountBalance) else account
        auth_settings = ['apiv2']
        body_params = {
            'account': account
        }
        res: AccountBalance = await self.api_client.call_api(
            resource_path='/hotwallet/balance',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='AccountBalance',  # noqa: E501
        )
        if res is not None:
            res.account = account
        return res
    
    async def charge(self, account: Union[str, AccountBalance], amount):
        account = account.account if isinstance(account, AccountBalance) else account
        auth_settings = ['apiv2']
        body_params = {
            'account': account,
            'amount': str(amount)
        }
        (transaction, account_balance) = await self.api_client.call_api(
            resource_path='/hotwallet/charge',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='tuple(InternalTransaction,AccountBalance)'
        )

        if transaction:
            transaction.account = account
            transaction.kind = status.TRANSACTION_WITHDRAW
        if account_balance:
            account_balance.account = account
        return (transaction, account_balance)
    
    async def award(self, account: Union[str, AccountBalance], amount):
        account = account.account if isinstance(account, AccountBalance) else account
        auth_settings = ['apiv2']
        body_params = {
            'account': account,
            'amount': str(amount)
        }
        (transaction, account_balance) = await self.api_client.call_api(
            resource_path='/hotwallet/award',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='tuple(InternalTransaction,AccountBalance)'
        )

        if transaction:
            transaction.account = account
            transaction.kind = status.TRANSACTION_DEPOSIT
        if account_balance:
            account_balance.account = account
        return (transaction, account_balance)
    
    async def get_allowance(self, account: Union[str, AccountBalance]):
        account = account.account if isinstance(account, AccountBalance) else account
        auth_settings = ['apiv2']
        body_params = {
            'account': account
        }
        allowance = await self.api_client.call_api(
            resource_path='/hotwallet/get_allowance',
            method='POST',
            body=body_params,
            auth_settings=auth_settings,
            response_type='HotwalletAllowance'
        )

        if allowance:
            allowance.account = account
        return allowance