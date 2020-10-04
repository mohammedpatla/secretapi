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


class UnbondingEntries(object):
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
        'initial_balance': 'str',
        'balance': 'str',
        'creation_height': 'str',
        'min_time': 'str'
    }

    attribute_map = {
        'initial_balance': 'initial_balance',
        'balance': 'balance',
        'creation_height': 'creation_height',
        'min_time': 'min_time'
    }

    def __init__(self, initial_balance=None, balance=None, creation_height=None, min_time=None):  # noqa: E501
        """UnbondingEntries - a model defined in Swagger"""  # noqa: E501

        self._initial_balance = None
        self._balance = None
        self._creation_height = None
        self._min_time = None
        self.discriminator = None

        if initial_balance is not None:
            self.initial_balance = initial_balance
        if balance is not None:
            self.balance = balance
        if creation_height is not None:
            self.creation_height = creation_height
        if min_time is not None:
            self.min_time = min_time

    @property
    def initial_balance(self):
        """Gets the initial_balance of this UnbondingEntries.  # noqa: E501


        :return: The initial_balance of this UnbondingEntries.  # noqa: E501
        :rtype: str
        """
        return self._initial_balance

    @initial_balance.setter
    def initial_balance(self, initial_balance):
        """Sets the initial_balance of this UnbondingEntries.


        :param initial_balance: The initial_balance of this UnbondingEntries.  # noqa: E501
        :type: str
        """

        self._initial_balance = initial_balance

    @property
    def balance(self):
        """Gets the balance of this UnbondingEntries.  # noqa: E501


        :return: The balance of this UnbondingEntries.  # noqa: E501
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this UnbondingEntries.


        :param balance: The balance of this UnbondingEntries.  # noqa: E501
        :type: str
        """

        self._balance = balance

    @property
    def creation_height(self):
        """Gets the creation_height of this UnbondingEntries.  # noqa: E501


        :return: The creation_height of this UnbondingEntries.  # noqa: E501
        :rtype: str
        """
        return self._creation_height

    @creation_height.setter
    def creation_height(self, creation_height):
        """Sets the creation_height of this UnbondingEntries.


        :param creation_height: The creation_height of this UnbondingEntries.  # noqa: E501
        :type: str
        """

        self._creation_height = creation_height

    @property
    def min_time(self):
        """Gets the min_time of this UnbondingEntries.  # noqa: E501


        :return: The min_time of this UnbondingEntries.  # noqa: E501
        :rtype: str
        """
        return self._min_time

    @min_time.setter
    def min_time(self, min_time):
        """Sets the min_time of this UnbondingEntries.


        :param min_time: The min_time of this UnbondingEntries.  # noqa: E501
        :type: str
        """

        self._min_time = min_time

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
        if issubclass(UnbondingEntries, dict):
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
        if not isinstance(other, UnbondingEntries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other