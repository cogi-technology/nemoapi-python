import logging
import random

from config import RunConfig, __ACCOUNT__, __METADATA__, __CALLBACK__

from nemo_api.client.api_client import ApiClient
from nemo_api.configuration import ApiConfiguration
from nemo_api.api.hotwallet_api import HotwalletApi

logger = logging.getLogger(__name__)

async def balance_demo(run_config: RunConfig):
    config = ApiConfiguration(
        key_id=run_config.key_id,
        private_key=run_config.prv,
        public_key=run_config.pub,
        host=run_config.host
    )
    client = ApiClient(configuration=config, user_agent="nemoapi-python-demo")
    hotwallet = HotwalletApi(client)
    return await hotwallet.balance(__ACCOUNT__)