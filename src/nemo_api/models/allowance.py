import pprint
from decimal import Decimal
from nemo_api.configuration import BaseConfiguration
from eth_utils import is_address
from nemo_api.function import parse_decimal
from nemo_api.status import STATUS as status


class HotwalletAllowance(object):
    """
    Attributes:
      api_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    api_types = {
        'account': 'str',
        'spender': 'str',
        'amount': 'str'
    }
    attribute_map = {
        'account': 'account',
        'spender': 'spender',
        'amount': 'amount'
    }

    def __init__(
        self,
        account=None,
        spender=None,
        amount=None,
        local_vars_configuration=None
    ):  # noqa: E501
        # type: (str, str, str, BaseConfiguration) -> None
        if local_vars_configuration is None:
            local_vars_configuration = BaseConfiguration()
        self.local_vars_configuration = local_vars_configuration

        self._account = None
        self._spender = None
        self._amount = None

        if account is not None:
            self.account = account
        if spender is not None:
            self.spender = spender
        if amount is not None:
            self.amount = amount

    @property
    def account(self):
        """Gets the account of this HotwalletAllowance.  # noqa: E501

        Account is an Ethereum address  # noqa: E501

        :return: The Ethereum address of this HotwalletAllowance.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this HotwalletAllowance.

        Account is an Ethereum address  # noqa: E501

        :param account: The Ethereum address of this HotwalletAllowance.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and not is_address(account):
            raise ValueError("Not an Ethereum address: {0}".format(account))
        self._account = account

    @property
    def spender(self):
        """Gets the spender of this HotwalletAllowance.  # noqa: E501

        Spender  # noqa: E501

        :return: The spender of this HotwalletAllowance.  # noqa: E501
        :rtype: str
        """
        return self._spender

    @spender.setter
    def spender(self, spender):
        """Sets the spender of this HotwalletAllowance.

        Spender  # noqa: E501

        :param spender: The spender of this HotwalletAllowance.  # noqa: E501
        :type: str
        """
        self._spender = spender

    @property
    def amount(self):
        """Gets the amount balance of this HotwalletAllowance.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this HotwalletAllowance.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this HotwalletAllowance.

        Amount  # noqa: E501

        :param amount: The amount of this HotwalletAllowance.  # noqa: E501
        :type: str
        """
        self._amount = amount


    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.api_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HotwalletAllowance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HotwalletAllowance):
            return True

        return self.to_dict() != other.to_dict()