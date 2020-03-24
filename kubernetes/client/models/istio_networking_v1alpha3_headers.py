# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.15.6
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class IstioNetworkingV1alpha3Headers(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'response': 'IstioNetworkingV1alpha3HeadersHeaderOperations',
        'request': 'IstioNetworkingV1alpha3HeadersHeaderOperations'
    }

    attribute_map = {
        'response': 'response',
        'request': 'request'
    }

    def __init__(self, response=None, request=None):  # noqa: E501
        """IstioNetworkingV1alpha3Headers - a model defined in OpenAPI"""  # noqa: E501

        self._response = None
        self._request = None
        self.discriminator = None

        if response is not None:
            self.response = response
        if request is not None:
            self.request = request

    @property
    def response(self):
        """Gets the response of this IstioNetworkingV1alpha3Headers.  # noqa: E501


        :return: The response of this IstioNetworkingV1alpha3Headers.  # noqa: E501
        :rtype: IstioNetworkingV1alpha3HeadersHeaderOperations
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this IstioNetworkingV1alpha3Headers.


        :param response: The response of this IstioNetworkingV1alpha3Headers.  # noqa: E501
        :type: IstioNetworkingV1alpha3HeadersHeaderOperations
        """

        self._response = response

    @property
    def request(self):
        """Gets the request of this IstioNetworkingV1alpha3Headers.  # noqa: E501


        :return: The request of this IstioNetworkingV1alpha3Headers.  # noqa: E501
        :rtype: IstioNetworkingV1alpha3HeadersHeaderOperations
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this IstioNetworkingV1alpha3Headers.


        :param request: The request of this IstioNetworkingV1alpha3Headers.  # noqa: E501
        :type: IstioNetworkingV1alpha3HeadersHeaderOperations
        """

        self._request = request

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IstioNetworkingV1alpha3Headers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
