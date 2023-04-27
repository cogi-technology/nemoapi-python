# !/usr/bin/env python
# coding: utf-8
import logging
from argparse import ArgumentParser
import asyncio

from config import RunConfig
from hotwallet_balance import balance_demo
from mint_nft import mint_demo

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)


async def main():
    parser = ArgumentParser(description="Run NEMO APIv2 demo application")
    parser.add_argument("-P", "--prv", required=True, help="NEMO APIv2 private key")
    parser.add_argument("-p", "--pub", required=True, help="NEMO APIv2 public key")
    parser.add_argument("-k", "--keyid", required=True, help="NEMO APIv2 key id")
    parser.add_argument("-u", "--url", required=False, help="API base URL used to test")
    parser.add_argument("tests", nargs='+', help="tests to run")
    options = parser.parse_args()

    host_used = options.url
    if not host_used:
        host_used = "http://127.0.0.1:5555/api/v2"

    run_config = RunConfig(
        host=host_used,
        prv=options.prv,
        pub=options.pub,
        keyid=options.keyid
    )
    for t in options.tests:
        logger.info("run %s API demo", t)
        if t == 'mint':
            await mint_demo(run_config)
        elif t == 'balance':
            await balance_demo(run_config)
        else:
            logger.warning("ignore unknown test %s", t)

asyncio.run(main())