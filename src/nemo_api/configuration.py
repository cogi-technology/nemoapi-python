# coding: utf-8


from __future__ import absolute_import

import copy
import logging
import multiprocessing
import sys
import urllib3
from urllib3.util.request import make_headers

import six
# from six.moves import http_client as httplib

from nemo_api.constants import __SYSTEM__

class BaseConfiguration(object):
    """
        :param host: Base url
        :param username: Username for HTTP basic authentication
        :param password: Password for HTTP basic authentication
    """

    _default = None

    def __init__(
        self,
        host=None,
        username=None,
        password=None,
        discard_unknown_keys=False,
    ):
        """Constructor"""
        self.host = host if host is None else (host[:-1] if host[-1] == "/" else host)
        
        self.temp_folder_path = None
        """Temp file folder for downloading files
        """
        # Authentication Settings
        self.username = username
        """Username for HTTP basic authentication
        """
        self.password = password
        """Password for HTTP basic authentication
        """
        self.discard_unknown_keys = discard_unknown_keys
        self.logger = {}
        """Logging Settings
        """
        self.logger["package_logger"] = logging.getLogger("nemoverse_api")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        """Log format
        """
        self.logger_stream_handler = None
        """Log stream handler
        """
        self.logger_file_handler = None
        """Log file handler
        """
        self.logger_file = None
        """Debug file location
        """
        self.debug = False
        """Debug switch
        """

        self.verify_ssl = __SYSTEM__ != 'Darwin'
        """SSL/TLS verification
           Set this to false to skip verifying SSL certificate when calling API
           from https server.
        """
        self.ssl_ca_cert = None
        """Set this to customize the certificate file to verify the peer.
        """
        self.cert_file = None
        """client certificate file
        """
        self.key_file = None
        """client key file
        """
        self.assert_hostname = None
        """Set this to True/False to enable/disable SSL hostname verification.
        """

        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5
        """urllib3 connection pool's maximum number of connections saved
           per pool. urllib3 uses 1 connection as default value, but this is
           not the best value when you are making a lot of possibly parallel
           requests to the same host, which is often the case here.
           cpu_count * 5 is used as default value to increase performance.
        """

        self.proxy = None
        """Proxy URL
        """
        self.proxy_headers = None
        """Proxy headers
        """
        self.safe_chars_for_path_param = ''
        """Safe chars for path_param
        """
        self.retries = None
        """Adding retries to override urllib3 default value 3
        """
        # Disable client side validation
        self.client_side_validation = True

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ('logger', 'logger_file_handler'):
                setattr(result, k, copy.deepcopy(v, memo))
        # shallow copy of loggers
        result.logger = copy.copy(self.logger)
        # use setters to configure loggers
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    @classmethod
    def set_default(cls, default):
        """Set default instance of configuration.

        It stores default configuration, which can be
        returned by get_default_copy method.

        :param default: object of Configuration
        """
        cls._default = copy.deepcopy(default)

    @classmethod
    def get_default_copy(cls):
        """Return new instance of configuration.

        This method returns newly created, based on default constructor,
        object of Configuration class or returns a copy of default
        configuration passed by the set_default method.

        :return: The configuration object.
        """
        if cls._default is not None:
            return copy.deepcopy(cls._default)
        return BaseConfiguration()

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :return: The logger_file path.
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :return: The debug status, True or False.
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            # httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            # httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :return: The format string.
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        username = ""
        if self.username is not None:
            username = self.username
        password = ""
        if self.password is not None:
            password = self.password
        return urllib3.util.make_headers(basic_auth=username + ':' + password).get('authorization')

    def auth_settings(self):
        pass

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return (
            "Python SDK Debug Report:\n"
            "OS: {env}\n"
            "Python Version: {pyversion}\n"
            "Version of the API: 2.0.0\n"
            "SDK Package Version: 2.0.0".format(env=sys.platform, pyversion=sys.version)
        )

    def get_host_settings(self):
        pass

    def get_host_from_settings(self, index, variables=None):
        pass


class ApiConfiguration(BaseConfiguration):
    """
        :param key_id: Key id of public key
        :param private_key: The DSA private key is used to generate digital signatures
        :param public_key: The DSA public key is used to verify digital signatures
    """

    def __init__(
        self,
        key_id,
        private_key,
        public_key,
        host="https://api.nemoverse.io/nemo-wallet-testnet/v2",
        username=None,
        password=None,
        discard_unknown_keys=False,
    ):
        super().__init__(
            host=host,
            username=username,
            password=password,
            discard_unknown_keys=discard_unknown_keys
        )

        self.key_id = key_id
        self.private_key = private_key
        self.public_key = public_key

    @classmethod
    def get_default_copy(cls):
        """Return new instance of configuration.

        This method returns newly created, based on default constructor,
        object of Configuration class or returns a copy of default
        configuration passed by the set_default method.

        :return: The configuration object.
        """
        if cls._default is not None:
            return copy.deepcopy(cls._default)
        return ApiConfiguration()

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        auth = {}
        if self.public_key is not None and self.private_key is not None:
            auth['apiv2'] = {
                'type': 'apiv2',
                'in': 'header',
                'key': 'SIGN',
            }
        return auth
    
    def get_host_settings(self):
        """Gets an array of host settings

        :return: An array of host settings
        """
        return [
            {
                'url': "https://api.nemoverse.io/nemo-wallet/v2",
                'description': "MainNet",
            },
            {
                'url': "https://api.nemoverse.io/nemo-wallet-testnet/v2",
                'description': "TestNet",
            },
        ]

    def get_host_from_settings(self, index, variables=None):
        """Gets host URL based on the index and variables
        :param index: array index of the host settings
        :param variables: hash of variable and the corresponding value
        :return: URL based on host settings
        """
        variables = {} if variables is None else variables
        servers = self.get_host_settings()

        try:
            server = servers[index]
        except IndexError:
            raise ValueError(
                "Invalid index {0} when selecting the host settings. "
                "Must be less than {1}".format(index, len(servers))
            )

        url = server['url']

        # go through variables and replace placeholders
        if server.get('variables') is not None:
            for variable_name, variable in server['variables'].items():
                used_value = variables.get(variable_name, variable['default_value'])

                if 'enum_values' in variable and used_value not in variable['enum_values']:
                    raise ValueError(
                        "The variable `{0}` in the host URL has invalid value "
                        "{1}. Must be {2}.".format(variable_name, variables[variable_name], variable['enum_values'])
                    )

                url = url.replace("{" + variable_name + "}", used_value)

        return url