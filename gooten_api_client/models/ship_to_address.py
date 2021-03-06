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


class ShipToAddress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ShipToAddress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'first_name': 'str',
            'last_name': 'str',
            'line1': 'str',
            'line2': 'str',
            'city': 'str',
            'state': 'str',
            'country_code': 'str',
            'postal_code': 'str',
            'is_business_address': 'bool',
            'phone': 'str',
            'email': 'str'
        }

        self.attribute_map = {
            'first_name': 'FirstName',
            'last_name': 'LastName',
            'line1': 'Line1',
            'line2': 'Line2',
            'city': 'City',
            'state': 'State',
            'country_code': 'CountryCode',
            'postal_code': 'PostalCode',
            'is_business_address': 'IsBusinessAddress',
            'phone': 'Phone',
            'email': 'Email'
        }

        self._first_name = None
        self._last_name = None
        self._line1 = None
        self._line2 = None
        self._city = None
        self._state = None
        self._country_code = None
        self._postal_code = None
        self._is_business_address = None
        self._phone = None
        self._email = None

    @property
    def first_name(self):
        """
        Gets the first_name of this ShipToAddress.


        :return: The first_name of this ShipToAddress.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this ShipToAddress.


        :param first_name: The first_name of this ShipToAddress.
        :type: str
        """
        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this ShipToAddress.


        :return: The last_name of this ShipToAddress.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this ShipToAddress.


        :param last_name: The last_name of this ShipToAddress.
        :type: str
        """
        self._last_name = last_name

    @property
    def line1(self):
        """
        Gets the line1 of this ShipToAddress.


        :return: The line1 of this ShipToAddress.
        :rtype: str
        """
        return self._line1

    @line1.setter
    def line1(self, line1):
        """
        Sets the line1 of this ShipToAddress.


        :param line1: The line1 of this ShipToAddress.
        :type: str
        """
        self._line1 = line1

    @property
    def line2(self):
        """
        Gets the line2 of this ShipToAddress.


        :return: The line2 of this ShipToAddress.
        :rtype: str
        """
        return self._line2

    @line2.setter
    def line2(self, line2):
        """
        Sets the line2 of this ShipToAddress.


        :param line2: The line2 of this ShipToAddress.
        :type: str
        """
        self._line2 = line2

    @property
    def city(self):
        """
        Gets the city of this ShipToAddress.


        :return: The city of this ShipToAddress.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this ShipToAddress.


        :param city: The city of this ShipToAddress.
        :type: str
        """
        self._city = city

    @property
    def state(self):
        """
        Gets the state of this ShipToAddress.


        :return: The state of this ShipToAddress.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this ShipToAddress.


        :param state: The state of this ShipToAddress.
        :type: str
        """
        self._state = state

    @property
    def country_code(self):
        """
        Gets the country_code of this ShipToAddress.


        :return: The country_code of this ShipToAddress.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this ShipToAddress.


        :param country_code: The country_code of this ShipToAddress.
        :type: str
        """
        self._country_code = country_code

    @property
    def postal_code(self):
        """
        Gets the postal_code of this ShipToAddress.


        :return: The postal_code of this ShipToAddress.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this ShipToAddress.


        :param postal_code: The postal_code of this ShipToAddress.
        :type: str
        """
        self._postal_code = postal_code

    @property
    def is_business_address(self):
        """
        Gets the is_business_address of this ShipToAddress.


        :return: The is_business_address of this ShipToAddress.
        :rtype: bool
        """
        return self._is_business_address

    @is_business_address.setter
    def is_business_address(self, is_business_address):
        """
        Sets the is_business_address of this ShipToAddress.


        :param is_business_address: The is_business_address of this ShipToAddress.
        :type: bool
        """
        self._is_business_address = is_business_address

    @property
    def phone(self):
        """
        Gets the phone of this ShipToAddress.


        :return: The phone of this ShipToAddress.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this ShipToAddress.


        :param phone: The phone of this ShipToAddress.
        :type: str
        """
        self._phone = phone

    @property
    def email(self):
        """
        Gets the email of this ShipToAddress.


        :return: The email of this ShipToAddress.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this ShipToAddress.


        :param email: The email of this ShipToAddress.
        :type: str
        """
        self._email = email

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

