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


class IstioNetworkingV1alpha3EnvoyFilterFilter(object):
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
        'listener_match': 'IstioNetworkingV1alpha3EnvoyFilterDeprecatedListenerMatch',
        'insert_position': 'IstioNetworkingV1alpha3EnvoyFilterInsertPosition',
        'filter_type': 'str',
        'filter_name': 'str',
        'filter_config': 'object'
    }

    attribute_map = {
        'listener_match': 'listenerMatch',
        'insert_position': 'insertPosition',
        'filter_type': 'filterType',
        'filter_name': 'filterName',
        'filter_config': 'filterConfig'
    }

    def __init__(self, listener_match=None, insert_position=None, filter_type=None, filter_name=None, filter_config=None):  # noqa: E501
        """IstioNetworkingV1alpha3EnvoyFilterFilter - a model defined in OpenAPI"""  # noqa: E501

        self._listener_match = None
        self._insert_position = None
        self._filter_type = None
        self._filter_name = None
        self._filter_config = None
        self.discriminator = None

        if listener_match is not None:
            self.listener_match = listener_match
        if insert_position is not None:
            self.insert_position = insert_position
        if filter_type is not None:
            self.filter_type = filter_type
        if filter_name is not None:
            self.filter_name = filter_name
        if filter_config is not None:
            self.filter_config = filter_config

    @property
    def listener_match(self):
        """Gets the listener_match of this IstioNetworkingV1alpha3EnvoyFilterFilter.  # noqa: E501


        :return: The listener_match of this IstioNetworkingV1alpha3EnvoyFilterFilter.  # noqa: E501
        :rtype: IstioNetworkingV1alpha3EnvoyFilterDeprecatedListenerMatch
        """
        return self._listener_match

    @listener_match.setter
    def listener_match(self, listener_match):
        """Sets the listener_match of this IstioNetworkingV1alpha3EnvoyFilterFilter.


        :param listener_match: The listener_match of this IstioNetworkingV1alpha3EnvoyFilterFilter.  # noqa: E501
        :type: IstioNetworkingV1alpha3EnvoyFilterDeprecatedListenerMatch
        """

        self._listener_match = listener_match

    @property
    def insert_position(self):
        """Gets the insert_position of this IstioNetworkingV1alpha3EnvoyFilterFilter.  # noqa: E501


        :return: The insert_position of this IstioNetworkingV1alpha3EnvoyFilterFilter.  # noqa: E501
        :rtype: IstioNetworkingV1alpha3EnvoyFilterInsertPosition
        """
        return self._insert_position

    @insert_position.setter
    def insert_position(self, insert_position):
        """Sets the insert_position of this IstioNetworkingV1alpha3EnvoyFilterFilter.


        :param insert_position: The insert_position of this IstioNetworkingV1alpha3EnvoyFilterFilter.  # noqa: E501
        :type: IstioNetworkingV1alpha3EnvoyFilterInsertPosition
        """

        self._insert_position = insert_position

    @property
    def filter_type(self):
        """Gets the filter_type of this IstioNetworkingV1alpha3EnvoyFilterFilter.  # noqa: E501


        :return: The filter_type of this IstioNetworkingV1alpha3EnvoyFilterFilter.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this IstioNetworkingV1alpha3EnvoyFilterFilter.


        :param filter_type: The filter_type of this IstioNetworkingV1alpha3EnvoyFilterFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["INVALID", "HTTP", "NETWORK"]  # noqa: E501
        if filter_type not in allowed_values:
            raise ValueError(
                "Invalid value for `filter_type` ({0}), must be one of {1}"  # noqa: E501
                .format(filter_type, allowed_values)
            )

        self._filter_type = filter_type

    @property
    def filter_name(self):
        """Gets the filter_name of this IstioNetworkingV1alpha3EnvoyFilterFilter.  # noqa: E501

        The name of the filter to instantiate. The name must match a supported filter _compiled into_ Envoy.  # noqa: E501

        :return: The filter_name of this IstioNetworkingV1alpha3EnvoyFilterFilter.  # noqa: E501
        :rtype: str
        """
        return self._filter_name

    @filter_name.setter
    def filter_name(self, filter_name):
        """Sets the filter_name of this IstioNetworkingV1alpha3EnvoyFilterFilter.

        The name of the filter to instantiate. The name must match a supported filter _compiled into_ Envoy.  # noqa: E501

        :param filter_name: The filter_name of this IstioNetworkingV1alpha3EnvoyFilterFilter.  # noqa: E501
        :type: str
        """

        self._filter_name = filter_name

    @property
    def filter_config(self):
        """Gets the filter_config of this IstioNetworkingV1alpha3EnvoyFilterFilter.  # noqa: E501

        Filter specific configuration which depends on the filter being instantiated.  # noqa: E501

        :return: The filter_config of this IstioNetworkingV1alpha3EnvoyFilterFilter.  # noqa: E501
        :rtype: object
        """
        return self._filter_config

    @filter_config.setter
    def filter_config(self, filter_config):
        """Sets the filter_config of this IstioNetworkingV1alpha3EnvoyFilterFilter.

        Filter specific configuration which depends on the filter being instantiated.  # noqa: E501

        :param filter_config: The filter_config of this IstioNetworkingV1alpha3EnvoyFilterFilter.  # noqa: E501
        :type: object
        """

        self._filter_config = filter_config

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
        if not isinstance(other, IstioNetworkingV1alpha3EnvoyFilterFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
