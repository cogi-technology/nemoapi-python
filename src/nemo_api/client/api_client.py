from __future__ import absolute_import

import datetime
import os
import re
import time
import mimetypes

# python 2 and python 3 compatibility library
import six
# from six.moves.urllib.parse import quote
from urllib.parse import quote, unquote_plus, urlencode, urlparse

from nemo_api.configuration import ApiConfiguration
from nemo_api.client.base import HTTPClientObject
from nemo_api.dsa import Base64Encoder, verify as dsa_verify, EDDSA
from nemo_api.function import json_encode, parse_decimal
from nemo_api.status import STATUS as status
from nemo_api.constants import __ANONYMOUS__
import nemo_api.models

from nemo_api.exceptions import ApiValueError, ApiException, ApiReponseError
from decimal import Decimal
from dateutil.parser import parse



class ApiClient(object):
    """
    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    :param user_agent: Identify the client
    :param timeout: limit the amount of time that make http request
    :param max_failed: the maximum number of retries allowed has been exceeded
    :param retried: the number of retries for the HTTP request has failed
    :param poll_latency: delay between HTTP retries
    """

    PRIMITIVE_TYPES = tuple([int, float, bool, bytes, six.text_type, six.integer_types, Decimal])
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,  # noqa: F821
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
        'decimal': Decimal,
    }
    _pool = None

    def __init__(
        self,
        configuration: ApiConfiguration=None,
        header_name=None,
        header_value=None,
        cookie=None,
        user_agent=None,
        timeout=300,
        max_failed=0,
        retried=0,
        poll_latency=3
    ):
        if configuration is None:
            configuration = ApiConfiguration.get_default_copy()
        if user_agent is None:
            user_agent = __ANONYMOUS__
        self.configuration = configuration
        self.timeout = timeout
        self.max_failed = max_failed
        self.retried = retried
        self.poll_latency = poll_latency

        self.client = HTTPClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = "NemoverseAPI/2.0.0/python/{0}".format(user_agent)
        self.client_side_validation = configuration.client_side_validation

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        pass

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    async def call_api(
        self,
        resource_path,
        method,
        path_params=None,
        query_params=None,
        header_params=None,
        verify_ssl=None,
        body=None,
        post_params=None,
        files=None,
        response_type=None,
        auth_settings=None,
        _return_http_data_only=True,
        collection_formats=None,
        timeout=None,
        max_failed=None,
        retried=None,
        poll_latency=None,
        _host=None,
        valid_status=None
    ):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param verify_ssl: Whether SSL verification is enabled.
        :param body: Request body.
        :param list post_params: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param dict files: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param response_type: Response data type.
        :param list auth_settings: Auth Settings names for the request.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param timeout: limit the amount of time that make http request
        :param max_failed: the maximum number of retries allowed has been exceeded
        :param retried: the number of retries for the HTTP request has failed
        :param poll_latency: delay between HTTP retries
        :param _host: server/host defined in path or operation instead
        :param valid_status: the HTTP request response has a valid status
        :return: return the response directly.
        """

        config = self.configuration
        resource_path = resource_path[:-1] if resource_path[-1] == "/" else resource_path

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(self.parameters_to_tuples(header_params, collection_formats))

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace('{%s}' % k, quote(str(v), safe=config.safe_chars_for_path_param))

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = self.parameters_to_tuples(query_params, collection_formats)

        # post parameters
        if post_params or files:
            post_params = post_params if post_params else []
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params, collection_formats)
            post_params.extend(self.files_parameters(files))

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # request url
        if _host is None:
            url = self.configuration.host + resource_path
        else:
            # use server/host defined in path or operation instead
            url = _host + resource_path

        # auth setting
        self.update_params_for_auth(method, url, header_params, query_params, body, auth_settings)

        # perform request and return response
        response_data = await self.request(
            url=url,
            method=method,
            query_params=query_params,
            post_params=post_params,
            body=body,
            verify_ssl=verify_ssl,
            headers=header_params,
            timeout=timeout,
            max_failed=max_failed,
            retried=retried,
            poll_latency=poll_latency,
            valid_status=valid_status
        )

        if not _return_http_data_only:
            return response_data
        
        if response_data is None or not isinstance(response_data, dict):
            raise ApiReponseError("invalid reponse {0}".format(response_data))
        if int(response_data.get('status')) < 0 \
            or (response_data.get('params') is None and response_data.get('uuid') is None) \
            or response_data.get('params', {}).get('error'):
            raise ApiReponseError(response_data)
        
        return_data = response_data

        # deserialize response data
        if response_type:
            return_data = self.deserialize(response_data, response_type)

        return return_data
    
    def deserialize(self, response, response_type):
        """Deserializes response into an object.

        :param response: response object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        """
        # # handle file downloading
        # # save response body into a tmp file and return the instance
        # if response_type == "file":
        #     return self.__deserialize_file(response)

        # fetch data from response object
        try:
            if 'uuid' in response:
                data = response['uuid']
            else:
                data = response['params']
        except Exception as e:
            data = response

        return self.__deserialize(data, response_type)
    
    def __deserialize(self, data, klass):
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if type(klass) == str:
            if klass.startswith('list['):
                sub_kls = re.match(r'list\[(.*)\]', klass).group(1)
                return [self.__deserialize(sub_data, sub_kls) for sub_data in data]
            
            if klass.startswith('tuple('):
                klass = 'tuple(InternalTransaction,AccountBalance)'
                sub_kls = re.match(r'tuple\((.*)\)', klass).group(1)
                sub_kls_list = sub_kls.split(',')
                if isinstance(data, list):
                    if len(data) != len(sub_kls_list):
                        raise TypeError('Data type is not match klass')
                    return [self.__deserialize(sub_data, sub_kls_list[index].strip()) for index, sub_data in enumerate(data)]
                else:
                    return [self.__deserialize(data, kls.strip()) for kls in sub_kls_list]

            if klass.startswith('dict('):
                sub_kls = re.match(r'dict\(([^,]*), (.*)\)', klass).group(2)
                return {k: self.__deserialize(v, sub_kls) for k, v in six.iteritems(data)}

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(nemo_api.models, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datetime(data)
        else:
            return self.__deserialize_model(data, klass)
        
    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise ApiException(status=0, reason="Failed to parse `{0}` as date object".format(string))

    def __deserialize_datetime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise ApiException(status=0, reason=("Failed to parse `{0}` as datetime object".format(string)))
        
    def __deserialize_object(self, value):
        """Return an original value.

        :return: object.
        """
        return value
    
    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool, Decimal.
        """
        try:
            if klass == Decimal:
                return parse_decimal(data)
            return klass(data)
        except UnicodeEncodeError:
            return six.text_type(data)
        except TypeError:
            return data
        
    def __deserialize_model(self, data, klass):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """
        has_discriminator = False
        if hasattr(klass, 'get_real_child_model') and klass.discriminator_value_class_map:
            has_discriminator = True

        if not klass.api_types and has_discriminator is False:
            return data

        kwargs = {}
        if data is not None and klass.api_types is not None and isinstance(data, (list, dict)):
            for attr, attr_type in six.iteritems(klass.api_types):
                if klass.attribute_map[attr] in data:
                    value = data[klass.attribute_map[attr]]
                    kwargs[attr] = self.__deserialize(value, attr_type)

        instance = klass(**kwargs)

        if has_discriminator:
            klass_name = instance.get_real_child_model(data)
            if klass_name:
                instance = self.__deserialize(data, klass_name)
        return instance

    def sanitize_for_serialization(self, obj):
        """Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj) for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj) for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return str(obj)

        if isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `api_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            obj_dict = {
                obj.attribute_map[attr]: getattr(obj, attr)
                for attr, _ in six.iteritems(obj.api_types)
                if getattr(obj, attr) is not None
            }

        return {key: self.sanitize_for_serialization(val) for key, val in six.iteritems(obj_dict)}
    
    def request(
        self,
        url,
        method,
        query_params=None,
        post_params=None,
        body=None,
        verify_ssl=True,
        headers=None,
        timeout=None,
        max_failed=None,
        retried=None,
        poll_latency=None,
        valid_status=None
    ):
        """Makes the HTTP request using HTTPClient."""
        timeout = timeout or self.timeout
        max_failed = max_failed or self.max_failed
        retried = retried or self.retried
        poll_latency = poll_latency or self.poll_latency

        if method == "GET":
            return self.client.GET(
                url=url,
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
        elif method == "POST":
            return self.client.POST(
                url=url,
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
        else:
            raise ApiValueError("http method must be `GET`, `HEAD`, `OPTIONS`," " `POST`, `PATCH`, `PUT` or `DELETE`.")

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in six.iteritems(params) if isinstance(params, dict) else params:  # noqa: E501
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append((k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def files_parameters(self, files=None):
        """Builds form parameters.

        :param files: File parameters.
        :return: Form parameters with files.
        """
        params = []

        if files:
            for k, v in six.iteritems(files):
                if not v:
                    continue
                file_names = v if type(v) is list else [v]
                for n in file_names:
                    with open(n, 'rb') as f:
                        filename = os.path.basename(f.name)
                        filedata = f.read()
                        mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
                        params.append(tuple([k, tuple([filename, filedata, mimetype])]))

        return params

    def select_header_accept(self, accepts):
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'
        else:
            return ', '.join(accepts)

    def select_header_content_type(self, content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return 'application/json'

        content_types = [x.lower() for x in content_types]

        if 'application/json' in content_types or '*/*' in content_types:
            return 'application/json'
        else:
            return content_types[0]

    def update_params_for_auth(self, method, url, headers, querys, body, auth_settings):
        """Updates header and query params based on authentication setting.

        :param method: Request method
        :param url: Request path, host included
        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters tuple list to be updated.
        :param body: Request body
        :param auth_settings: Authentication setting identifiers list.
        """
        if not auth_settings:
            return

        for auth in auth_settings:
            auth_setting = self.configuration.auth_settings().get(auth)
            if auth_setting:
                if auth_setting['type'] == 'apiv2':
                    auth_headers = self.gen_sign(url, body)
                    headers.update(auth_headers)
                    continue
                if auth_setting['in'] == 'cookie':
                    headers['Cookie'] = auth_setting['value']
                elif auth_setting['in'] == 'header':
                    headers[auth_setting['key']] = auth_setting['value']
                elif auth_setting['in'] == 'query':
                    querys.append((auth_setting['key'], auth_setting['value']))
                else:
                    raise ApiValueError('Authentication token must be in `query` or `header`')

    def gen_sign(self, url, body=None, access_time=None):
        """generate authentication headers

        :param url: http resource path
        :param body: request body
        :param access_time: UNIX timestamp in milliseconds
        :return: signature headers
        """
        access_time = access_time or str(time.time_ns())
        body = body or {}
        private_key = Base64Encoder.decode(self.configuration.private_key)
        public_key = Base64Encoder.decode(self.configuration.public_key)
        access_key_id = self.configuration.key_id
        access_id = urlparse(url).path
        message_hash = ("%s:%s:%s" % (access_id, access_time, json_encode(body))).encode()
        access_signature = EDDSA.from_prv(private_key).sign(message_hash, Base64Encoder)

        assert dsa_verify(public_key, message_hash, Base64Encoder.decode(access_signature))

        return {
            'Access-Time': access_time,
            'Access-Signature': access_signature.decode(),
            'Access-Key-Id': access_key_id
        }