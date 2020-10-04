# coding: utf-8

"""
    API for Secret Network by ChainofSecrets.org

    A REST interface for state queries, transaction generation and broadcasting.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Coin(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'denom': 'str',
        'amount': 'str'
    }

    attribute_map = {
        'denom': 'denom',
        'amount': 'amount'
    }

    def __init__(self, denom=None, amount=None):  # noqa: E501
        """Coin - a model defined in Swagger"""  # noqa: E501

        self._denom = None
        self._amount = None
        self.discriminator = None

        if denom is not None:
            self.denom = denom
        if amount is not None:
            self.amount = amount

    @property
    def denom(self):
        """Gets the denom of this Coin.  # noqa: E501


        :return: The denom of this Coin.  # noqa: E501
        :rtype: str
        """
        return self._denom

    @denom.setter
    def denom(self, denom):
        """Sets the denom of this Coin.


        :param denom: The denom of this Coin.  # noqa: E501
        :type: str
        """

        self._denom = denom

    @property
    def amount(self):
        """Gets the amount of this Coin.  # noqa: E501


        :return: The amount of this Coin.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Coin.


        :param amount: The amount of this Coin.  # noqa: E501
        :type: str
        """

        self._amount = amount

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Coin, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Coin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other