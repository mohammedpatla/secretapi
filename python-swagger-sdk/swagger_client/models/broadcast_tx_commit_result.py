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


class BroadcastTxCommitResult(object):
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
        'check_tx': 'CheckTxResult',
        'deliver_tx': 'DeliverTxResult',
        'hash': 'Hash',
        'height': 'int'
    }

    attribute_map = {
        'check_tx': 'check_tx',
        'deliver_tx': 'deliver_tx',
        'hash': 'hash',
        'height': 'height'
    }

    def __init__(self, check_tx=None, deliver_tx=None, hash=None, height=None):  # noqa: E501
        """BroadcastTxCommitResult - a model defined in Swagger"""  # noqa: E501

        self._check_tx = None
        self._deliver_tx = None
        self._hash = None
        self._height = None
        self.discriminator = None

        if check_tx is not None:
            self.check_tx = check_tx
        if deliver_tx is not None:
            self.deliver_tx = deliver_tx
        if hash is not None:
            self.hash = hash
        if height is not None:
            self.height = height

    @property
    def check_tx(self):
        """Gets the check_tx of this BroadcastTxCommitResult.  # noqa: E501


        :return: The check_tx of this BroadcastTxCommitResult.  # noqa: E501
        :rtype: CheckTxResult
        """
        return self._check_tx

    @check_tx.setter
    def check_tx(self, check_tx):
        """Sets the check_tx of this BroadcastTxCommitResult.


        :param check_tx: The check_tx of this BroadcastTxCommitResult.  # noqa: E501
        :type: CheckTxResult
        """

        self._check_tx = check_tx

    @property
    def deliver_tx(self):
        """Gets the deliver_tx of this BroadcastTxCommitResult.  # noqa: E501


        :return: The deliver_tx of this BroadcastTxCommitResult.  # noqa: E501
        :rtype: DeliverTxResult
        """
        return self._deliver_tx

    @deliver_tx.setter
    def deliver_tx(self, deliver_tx):
        """Sets the deliver_tx of this BroadcastTxCommitResult.


        :param deliver_tx: The deliver_tx of this BroadcastTxCommitResult.  # noqa: E501
        :type: DeliverTxResult
        """

        self._deliver_tx = deliver_tx

    @property
    def hash(self):
        """Gets the hash of this BroadcastTxCommitResult.  # noqa: E501


        :return: The hash of this BroadcastTxCommitResult.  # noqa: E501
        :rtype: Hash
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this BroadcastTxCommitResult.


        :param hash: The hash of this BroadcastTxCommitResult.  # noqa: E501
        :type: Hash
        """

        self._hash = hash

    @property
    def height(self):
        """Gets the height of this BroadcastTxCommitResult.  # noqa: E501


        :return: The height of this BroadcastTxCommitResult.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this BroadcastTxCommitResult.


        :param height: The height of this BroadcastTxCommitResult.  # noqa: E501
        :type: int
        """

        self._height = height

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
        if issubclass(BroadcastTxCommitResult, dict):
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
        if not isinstance(other, BroadcastTxCommitResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other