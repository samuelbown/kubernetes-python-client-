# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.11.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1alpha1Initializer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'name': 'str',
        'rules': 'list[V1alpha1Rule]'
    }

    attribute_map = {
        'name': 'name',
        'rules': 'rules'
    }

    def __init__(self, name=None, rules=None):
        """
        V1alpha1Initializer - a model defined in Swagger
        """

        self._name = None
        self._rules = None
        self.discriminator = None

        self.name = name
        if rules is not None:
          self.rules = rules

    @property
    def name(self):
        """
        Gets the name of this V1alpha1Initializer.
        Name is the identifier of the initializer. It will be added to the object that needs to be initialized. Name should be fully qualified, e.g., alwayspullimages.kubernetes.io, where \"alwayspullimages\" is the name of the webhook, and kubernetes.io is the name of the organization. Required

        :return: The name of this V1alpha1Initializer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1alpha1Initializer.
        Name is the identifier of the initializer. It will be added to the object that needs to be initialized. Name should be fully qualified, e.g., alwayspullimages.kubernetes.io, where \"alwayspullimages\" is the name of the webhook, and kubernetes.io is the name of the organization. Required

        :param name: The name of this V1alpha1Initializer.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def rules(self):
        """
        Gets the rules of this V1alpha1Initializer.
        Rules describes what resources/subresources the initializer cares about. The initializer cares about an operation if it matches _any_ Rule. Rule.Resources must not include subresources.

        :return: The rules of this V1alpha1Initializer.
        :rtype: list[V1alpha1Rule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this V1alpha1Initializer.
        Rules describes what resources/subresources the initializer cares about. The initializer cares about an operation if it matches _any_ Rule. Rule.Resources must not include subresources.

        :param rules: The rules of this V1alpha1Initializer.
        :type: list[V1alpha1Rule]
        """

        self._rules = rules

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
        if not isinstance(other, V1alpha1Initializer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
