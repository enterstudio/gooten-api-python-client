# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Result(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Result - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'is_valid': 'bool',
            'reason': 'str',
            'score': 'int',
            'proposed_address': 'Address'
        }

        self.attribute_map = {
            'is_valid': 'IsValid',
            'reason': 'Reason',
            'score': 'Score',
            'proposed_address': 'ProposedAddress'
        }

        self._is_valid = None
        self._reason = None
        self._score = None
        self._proposed_address = None

    @property
    def is_valid(self):
        """
        Gets the is_valid of this Result.


        :return: The is_valid of this Result.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """
        Sets the is_valid of this Result.


        :param is_valid: The is_valid of this Result.
        :type: bool
        """
        self._is_valid = is_valid

    @property
    def reason(self):
        """
        Gets the reason of this Result.


        :return: The reason of this Result.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this Result.


        :param reason: The reason of this Result.
        :type: str
        """
        self._reason = reason

    @property
    def score(self):
        """
        Gets the score of this Result.


        :return: The score of this Result.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this Result.


        :param score: The score of this Result.
        :type: int
        """
        self._score = score

    @property
    def proposed_address(self):
        """
        Gets the proposed_address of this Result.


        :return: The proposed_address of this Result.
        :rtype: Address
        """
        return self._proposed_address

    @proposed_address.setter
    def proposed_address(self, proposed_address):
        """
        Sets the proposed_address of this Result.


        :param proposed_address: The proposed_address of this Result.
        :type: Address
        """
        self._proposed_address = proposed_address

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

