# coding: utf-8

from nemo_api.exceptions import ApiException, ApiValueError
from nemo_api.configuration import BaseConfiguration
from nemo_api.constants import __SYSTEM__, __VALID_STATUS__

import asyncio
from aiohttp import ClientSession, TCPConnector
import async_timeout

import logging
logger = logging.getLogger(__name__)

__headers__ = {} #TODO

async def do_request(
    url,
    method,
    params=None,
    data=None,
    json=None,
    verify_ssl=True,
    headers: dict={},
    raw=False,
    json_reponse=True,
    timeout=300,
    max_failed=0,
    retried=0,
    poll_latency=3,
    valid_status=None
):    
    ret = None
    valid_status = valid_status or __VALID_STATUS__

    try:
        async with async_timeout.timeout(timeout):
            async with ClientSession(headers={**__headers__, **headers}, connector=TCPConnector(ssl=verify_ssl)) as session:
                if method == 'POST':
                    if headers.get('Content-Type') == 'application/json':
                        async with session.post(url, params=params, json=json) as resp:
                            assert resp.status in valid_status, f"Failed post {url} {resp.status} {await resp.text()}"
                            try:
                                return await resp.json()
                            except:
                                return await resp.text()
                    else: 
                        async with session.post(url, params=params, data=data, chunked=True) as resp:
                            assert resp.status in valid_status, f"Failed post {url} {resp.status} {await resp.text()}"
                            return await resp.text()

                elif method == 'GET':
                    async with session.get(url, params=params) as resp:
                        assert resp.status in valid_status, f"Failed get {url} {resp.status} {await resp.text()}"
                        if json_reponse:
                            return await resp.json()
                        else:
                            if raw:
                                return await resp.read()
                            else:
                                return await resp.text()

                else:
                    raise ApiValueError("{method} unsupported.".format(method=method))
                        
    except Exception as e:
        logger.error("%s %s %s" % (e, url, data))
        if max_failed > retried or max_failed == -1:
            await asyncio.sleep(poll_latency)
            ret = await do_request(
                url=url,
                method=method,
                data=data,
                json=json,
                verify_ssl=verify_ssl,
                headers=headers,
                timeout=timeout,
                max_failed=max_failed,
                retried=retried+1,
                poll_latency=poll_latency,
                valid_status=valid_status
            )
        else:
            ret = None

    return ret
    
class HTTPClientObject(object):

    def __init__(self, configuration: BaseConfiguration) -> None:
        self.configuration = configuration

        
    async def request(
        self,
        url,
        method,
        query_params=None,
        post_params=None,
        body=None,
        verify_ssl=None,
        headers=None,
        timeout=300,
        max_failed=0,
        retried=0,
        poll_latency=3,
        valid_status=None
    ):
        #TODO
        """Perform request.

        :param url: http request url. Default is `configuration.url`.
        :param method: http request method
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param body: request json body, for `application/json`
        :param headers: http request headers
        :param max_failed: max failed.
        :param timeout: timeout setting for this request.
        :param valid_status: valid status.
        """

        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT', 'PATCH', 'OPTIONS']

        if body and post_params:
            raise ApiValueError("body parameter cannot be used with post_params parameter.")

        post_params = post_params or {}
        body = body or {}
        headers = headers or {}
        verify_ssl = verify_ssl or self.configuration.verify_ssl

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        return await do_request(
            url=url,
            method=method,
            params=query_params,
            data=post_params,
            json=body,
            verify_ssl=verify_ssl,
            headers=headers,
            timeout=timeout,
            max_failed=max_failed,
            retried=retried+1,
            poll_latency=poll_latency,
            valid_status=valid_status
        )
    
    async def POST(
        self,
        url,
        query_params=None,
        post_params=None,
        body=None,
        verify_ssl=None,
        headers=None,
        timeout=300,
        max_failed=0,
        retried=0,
        poll_latency=3,
        valid_status=None
    ):
        return await self.request(
            url=url,
            method='POST',
            query_params=query_params,
            post_params=post_params,
            body=body,
            verify_ssl=verify_ssl,
            headers=headers,
            timeout=timeout,
            max_failed=max_failed,
            retried=retried,
            poll_latency=poll_latency,
            valid_status=valid_status
        )
    
    async def GET(
        self,
        url,
        query_params=None,
        post_params=None,
        body=None,
        verify_ssl=None,
        headers=None,
        timeout=300,
        max_failed=0,
        retried=0,
        poll_latency=3,
        valid_status=None
    ):
        return await self.request(
            url=url,
            method='GET',
            query_params=query_params,
            post_params=post_params,
            body=body,
            verify_ssl=verify_ssl,
            headers=headers,
            timeout=timeout,
            max_failed=max_failed,
            retried=retried,
            poll_latency=poll_latency,
            valid_status=valid_status
        )