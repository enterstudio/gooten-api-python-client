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


class OrderItemImage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        OrderItemImage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'url': 'str',
            'index': 'int',
            'thumbnail_url': 'str',
            'manip_command': 'str',
            'space_id': 'str'
        }

        self.attribute_map = {
            'url': 'Url',
            'index': 'Index',
            'thumbnail_url': 'ThumbnailUrl',
            'manip_command': 'ManipCommand',
            'space_id': 'SpaceId'
        }

        self._url = None
        self._index = None
        self._thumbnail_url = None
        self._manip_command = None
        self._space_id = None

    @property
    def url(self):
        """
        Gets the url of this OrderItemImage.


        :return: The url of this OrderItemImage.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this OrderItemImage.


        :param url: The url of this OrderItemImage.
        :type: str
        """
        self._url = url

    @property
    def index(self):
        """
        Gets the index of this OrderItemImage.


        :return: The index of this OrderItemImage.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Sets the index of this OrderItemImage.


        :param index: The index of this OrderItemImage.
        :type: int
        """
        self._index = index

    @property
    def thumbnail_url(self):
        """
        Gets the thumbnail_url of this OrderItemImage.


        :return: The thumbnail_url of this OrderItemImage.
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """
        Sets the thumbnail_url of this OrderItemImage.


        :param thumbnail_url: The thumbnail_url of this OrderItemImage.
        :type: str
        """
        self._thumbnail_url = thumbnail_url

    @property
    def manip_command(self):
        """
        Gets the manip_command of this OrderItemImage.


        :return: The manip_command of this OrderItemImage.
        :rtype: str
        """
        return self._manip_command

    @manip_command.setter
    def manip_command(self, manip_command):
        """
        Sets the manip_command of this OrderItemImage.


        :param manip_command: The manip_command of this OrderItemImage.
        :type: str
        """
        self._manip_command = manip_command

    @property
    def space_id(self):
        """
        Gets the space_id of this OrderItemImage.


        :return: The space_id of this OrderItemImage.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """
        Sets the space_id of this OrderItemImage.


        :param space_id: The space_id of this OrderItemImage.
        :type: str
        """
        self._space_id = space_id

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

