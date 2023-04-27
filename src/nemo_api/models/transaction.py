import pprint
from decimal import Decimal
from nemo_api.configuration import BaseConfiguration
from eth_utils import is_address
from nemo_api.function import parse_decimal
from nemo_api.status import STATUS as status


class InternalTransaction(object):
    """
    Attributes:
      api_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    api_types = {
        'account': 'str',
        'tx_hash': 'str',
        'amount': 'str',
        'kind': 'int'
    }
    attribute_map = {
        'account': 'account',
        'tx_hash': 'tx_hash',
        'amount': 'amount',
        'kind': 'kind'
    }

    def __init__(
        self,
        account=None,
        tx_hash=None,
        amount=None,
        kind=None,
        local_vars_configuration=None
    ):  # noqa: E501
        # type: (str, str, Decimal, int, BaseConfiguration) -> None
        if local_vars_configuration is None:
            local_vars_configuration = BaseConfiguration()
        self.local_vars_configuration = local_vars_configuration

        self._account = None
        self._tx_hash = None
        self._amount = None
        self._kind = None

        if account is not None:
            self.account = account
        if tx_hash is not None:
            self.tx_hash = tx_hash
        if amount is not None:
            self.amount = amount
        if kind is not None:
            self.kind = kind

    @property
    def account(self):
        """Gets the account of this InternalTransaction.  # noqa: E501

        Account is an Ethereum address  # noqa: E501

        :return: The Ethereum address of this InternalTransaction.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this InternalTransaction.

        Account is an Ethereum address  # noqa: E501

        :param account: The Ethereum address of this InternalTransaction.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and not is_address(account):
            raise ValueError("Not an Ethereum address: {0}".format(account))
        self._account = account

    @property
    def tx_hash(self):
        """Gets the tx_hash of this InternalTransaction.  # noqa: E501

        Transaction hash  # noqa: E501

        :return: The tx_hash of this InternalTransaction.  # noqa: E501
        :rtype: str
        """
        return self._tx_hash

    @tx_hash.setter
    def tx_hash(self, tx_hash):
        """Sets the tx_hash of this InternalTransaction.

        Transaction hash  # noqa: E501

        :param tx_hash: The tx_hash of this InternalTransaction.  # noqa: E501
        :type: str
        """
        self._tx_hash = tx_hash

    @property
    def amount(self):
        """Gets the amount balance of this InternalTransaction.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this InternalTransaction.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InternalTransaction.

        Amount  # noqa: E501

        :param amount: The amount of this InternalTransaction.  # noqa: E501
        :type: str
        """
        self._amount = parse_decimal(amount) if self.local_vars_configuration.client_side_validation else amount

    @property
    def kind(self):
        """Gets the kind of this InternalTransaction.  # noqa: E501

        kind  # noqa: E501

        :return: The kind of this InternalTransaction.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this InternalTransaction.

        Kind  # noqa: E501

        :param kind: The kind of this InternalTransaction.  # noqa: E501
        :type: int
        """
        self._kind = status(int(kind)) if self.local_vars_configuration.client_side_validation else kind

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
        if not isinstance(other, InternalTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InternalTransaction):
            return True

        return self.to_dict() != other.to_dict()