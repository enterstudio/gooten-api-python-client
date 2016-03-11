# coding: utf-8

"""
PreconfiguredproductsApi.py
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
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class PreconfiguredproductsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_preconfiguredproducts(self, preconfigured_product_insert, version, source, **kwargs):
        """
        Insert a preconfigured product
        Insert a preconfigured product into your recipe.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_preconfiguredproducts(preconfigured_product_insert, version, source, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PreconfiguredProductInsert preconfigured_product_insert: The product to be inserted (required)
        :param int version: Version of the api being used (required)
        :param str source: Description of the source-- ios, android, api (required)
        :return: PreconfiguredProductsInsertResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['preconfigured_product_insert', 'version', 'source']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_preconfiguredproducts" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'preconfigured_product_insert' is set
        if ('preconfigured_product_insert' not in params) or (params['preconfigured_product_insert'] is None):
            raise ValueError("Missing the required parameter `preconfigured_product_insert` when calling `create_preconfiguredproducts`")
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `create_preconfiguredproducts`")
        # verify the required parameter 'source' is set
        if ('source' not in params) or (params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `create_preconfiguredproducts`")

        resource_path = '/preconfiguredproducts/v/{version}/source/{source}/'.replace('{format}', 'json')
        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']
        if 'source' in params:
            path_params['source'] = params['source']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'preconfigured_product_insert' in params:
            body_params = params['preconfigured_product_insert']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PreconfiguredProductsInsertResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_preconfiguredproducts(self, version, source, **kwargs):
        """
        Delete a preconfigured product
        Delete a preconfigured product from your recipe.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_preconfiguredproducts(version, source, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int version: Version of the api being used (required)
        :param str source: Description of the source-- ios, android, api (required)
        :param str sku: The preconfigured product's sku.
        :return: PreconfiguredProductsInsertResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version', 'source', 'sku']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_preconfiguredproducts" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `delete_preconfiguredproducts`")
        # verify the required parameter 'source' is set
        if ('source' not in params) or (params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `delete_preconfiguredproducts`")

        resource_path = '/preconfiguredproducts/v/{version}/source/{source}/'.replace('{format}', 'json')
        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']
        if 'source' in params:
            path_params['source'] = params['source']

        query_params = {}
        if 'sku' in params:
            query_params['sku'] = params['sku']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PreconfiguredProductsInsertResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_preconfiguredproducts(self, country_code, version, source, **kwargs):
        """
        Get a list of your preconfigured products
        Get a list of your preconfigured products. The products returned are entirely specific to your recipe.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_preconfiguredproducts(country_code, version, source, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str country_code: The country code where it would be shipped to. For example, 'US' or 'CA' (required)
        :param int version: Version of the api being used (required)
        :param str source: Description of the source-- ios, android, api (required)
        :param str language_code: Two-character language code, defaults to \"en\" (english)
        :param str currency_code: Three character currency code, defaults to \"USD\" (united states dollar)
        :return: PreconfiguredProductsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_code', 'version', 'source', 'language_code', 'currency_code']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_preconfiguredproducts" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'country_code' is set
        if ('country_code' not in params) or (params['country_code'] is None):
            raise ValueError("Missing the required parameter `country_code` when calling `get_preconfiguredproducts`")
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `get_preconfiguredproducts`")
        # verify the required parameter 'source' is set
        if ('source' not in params) or (params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `get_preconfiguredproducts`")

        resource_path = '/preconfiguredproducts/v/{version}/source/{source}/'.replace('{format}', 'json')
        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']
        if 'source' in params:
            path_params['source'] = params['source']

        query_params = {}
        if 'country_code' in params:
            query_params['countryCode'] = params['country_code']
        if 'language_code' in params:
            query_params['languageCode'] = params['language_code']
        if 'currency_code' in params:
            query_params['currencyCode'] = params['currency_code']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PreconfiguredProductsResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_preconfiguredproducts(self, preconfigured_product_insert, version, source, **kwargs):
        """
        Update a preconfigured product
        Update a preconfigured product into your recipe.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_preconfiguredproducts(preconfigured_product_insert, version, source, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PreconfiguredProductInsert preconfigured_product_insert: The product to be inserted (required)
        :param int version: Version of the api being used (required)
        :param str source: Description of the source-- ios, android, api (required)
        :return: PreconfiguredProductsInsertResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['preconfigured_product_insert', 'version', 'source']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_preconfiguredproducts" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'preconfigured_product_insert' is set
        if ('preconfigured_product_insert' not in params) or (params['preconfigured_product_insert'] is None):
            raise ValueError("Missing the required parameter `preconfigured_product_insert` when calling `update_preconfiguredproducts`")
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `update_preconfiguredproducts`")
        # verify the required parameter 'source' is set
        if ('source' not in params) or (params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `update_preconfiguredproducts`")

        resource_path = '/preconfiguredproducts/v/{version}/source/{source}/'.replace('{format}', 'json')
        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']
        if 'source' in params:
            path_params['source'] = params['source']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'preconfigured_product_insert' in params:
            body_params = params['preconfigured_product_insert']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PreconfiguredProductsInsertResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
