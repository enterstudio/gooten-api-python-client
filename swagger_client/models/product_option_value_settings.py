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


class ProductOptionValueSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProductOptionValueSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'icon_url': 'str',
            'icon_type': 'str',
            'color_rgba': 'str'
        }

        self.attribute_map = {
            'icon_url': 'IconUrl',
            'icon_type': 'IconType',
            'color_rgba': 'ColorRgba'
        }

        self._icon_url = None
        self._icon_type = None
        self._color_rgba = None

    @property
    def icon_url(self):
        """
        Gets the icon_url of this ProductOptionValueSettings.


        :return: The icon_url of this ProductOptionValueSettings.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """
        Sets the icon_url of this ProductOptionValueSettings.


        :param icon_url: The icon_url of this ProductOptionValueSettings.
        :type: str
        """
        self._icon_url = icon_url

    @property
    def icon_type(self):
        """
        Gets the icon_type of this ProductOptionValueSettings.


        :return: The icon_type of this ProductOptionValueSettings.
        :rtype: str
        """
        return self._icon_type

    @icon_type.setter
    def icon_type(self, icon_type):
        """
        Sets the icon_type of this ProductOptionValueSettings.


        :param icon_type: The icon_type of this ProductOptionValueSettings.
        :type: str
        """
        self._icon_type = icon_type

    @property
    def color_rgba(self):
        """
        Gets the color_rgba of this ProductOptionValueSettings.


        :return: The color_rgba of this ProductOptionValueSettings.
        :rtype: str
        """
        return self._color_rgba

    @color_rgba.setter
    def color_rgba(self, color_rgba):
        """
        Sets the color_rgba of this ProductOptionValueSettings.


        :param color_rgba: The color_rgba of this ProductOptionValueSettings.
        :type: str
        """
        self._color_rgba = color_rgba

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

