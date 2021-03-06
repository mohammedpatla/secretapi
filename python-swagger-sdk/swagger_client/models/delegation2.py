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


class Delegation2(object):
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
        'base_req': 'BaseReq',
        'delegator_address': 'Address',
        'validator_src_addressess': 'ValidatorAddress',
        'validator_dst_address': 'ValidatorAddress',
        'shares': 'str'
    }

    attribute_map = {
        'base_req': 'base_req',
        'delegator_address': 'delegator_address',
        'validator_src_addressess': 'validator_src_addressess',
        'validator_dst_address': 'validator_dst_address',
        'shares': 'shares'
    }

    def __init__(self, base_req=None, delegator_address=None, validator_src_addressess=None, validator_dst_address=None, shares=None):  # noqa: E501
        """Delegation2 - a model defined in Swagger"""  # noqa: E501

        self._base_req = None
        self._delegator_address = None
        self._validator_src_addressess = None
        self._validator_dst_address = None
        self._shares = None
        self.discriminator = None

        if base_req is not None:
            self.base_req = base_req
        if delegator_address is not None:
            self.delegator_address = delegator_address
        if validator_src_addressess is not None:
            self.validator_src_addressess = validator_src_addressess
        if validator_dst_address is not None:
            self.validator_dst_address = validator_dst_address
        if shares is not None:
            self.shares = shares

    @property
    def base_req(self):
        """Gets the base_req of this Delegation2.  # noqa: E501


        :return: The base_req of this Delegation2.  # noqa: E501
        :rtype: BaseReq
        """
        return self._base_req

    @base_req.setter
    def base_req(self, base_req):
        """Sets the base_req of this Delegation2.


        :param base_req: The base_req of this Delegation2.  # noqa: E501
        :type: BaseReq
        """

        self._base_req = base_req

    @property
    def delegator_address(self):
        """Gets the delegator_address of this Delegation2.  # noqa: E501


        :return: The delegator_address of this Delegation2.  # noqa: E501
        :rtype: Address
        """
        return self._delegator_address

    @delegator_address.setter
    def delegator_address(self, delegator_address):
        """Sets the delegator_address of this Delegation2.


        :param delegator_address: The delegator_address of this Delegation2.  # noqa: E501
        :type: Address
        """

        self._delegator_address = delegator_address

    @property
    def validator_src_addressess(self):
        """Gets the validator_src_addressess of this Delegation2.  # noqa: E501


        :return: The validator_src_addressess of this Delegation2.  # noqa: E501
        :rtype: ValidatorAddress
        """
        return self._validator_src_addressess

    @validator_src_addressess.setter
    def validator_src_addressess(self, validator_src_addressess):
        """Sets the validator_src_addressess of this Delegation2.


        :param validator_src_addressess: The validator_src_addressess of this Delegation2.  # noqa: E501
        :type: ValidatorAddress
        """

        self._validator_src_addressess = validator_src_addressess

    @property
    def validator_dst_address(self):
        """Gets the validator_dst_address of this Delegation2.  # noqa: E501


        :return: The validator_dst_address of this Delegation2.  # noqa: E501
        :rtype: ValidatorAddress
        """
        return self._validator_dst_address

    @validator_dst_address.setter
    def validator_dst_address(self, validator_dst_address):
        """Sets the validator_dst_address of this Delegation2.


        :param validator_dst_address: The validator_dst_address of this Delegation2.  # noqa: E501
        :type: ValidatorAddress
        """

        self._validator_dst_address = validator_dst_address

    @property
    def shares(self):
        """Gets the shares of this Delegation2.  # noqa: E501


        :return: The shares of this Delegation2.  # noqa: E501
        :rtype: str
        """
        return self._shares

    @shares.setter
    def shares(self, shares):
        """Sets the shares of this Delegation2.


        :param shares: The shares of this Delegation2.  # noqa: E501
        :type: str
        """

        self._shares = shares

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
        if issubclass(Delegation2, dict):
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
        if not isinstance(other, Delegation2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
