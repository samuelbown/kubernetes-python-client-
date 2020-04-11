# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: release-1.15
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class V2beta2ResourceMetricSource(object):
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
        'name': 'str',
        'target': 'V2beta2MetricTarget'
    }

    attribute_map = {
        'name': 'name',
        'target': 'target'
    }

    def __init__(self, name=None, target=None):  # noqa: E501
        """V2beta2ResourceMetricSource - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._target = None
        self.discriminator = None

        self.name = name
        self.target = target

    @property
    def name(self):
        """Gets the name of this V2beta2ResourceMetricSource.  # noqa: E501

        name is the name of the resource in question.  # noqa: E501

        :return: The name of this V2beta2ResourceMetricSource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2beta2ResourceMetricSource.

        name is the name of the resource in question.  # noqa: E501

        :param name: The name of this V2beta2ResourceMetricSource.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def target(self):
        """Gets the target of this V2beta2ResourceMetricSource.  # noqa: E501


        :return: The target of this V2beta2ResourceMetricSource.  # noqa: E501
        :rtype: V2beta2MetricTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this V2beta2ResourceMetricSource.


        :param target: The target of this V2beta2ResourceMetricSource.  # noqa: E501
        :type: V2beta2MetricTarget
        """
        if target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

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
        if not isinstance(other, V2beta2ResourceMetricSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
