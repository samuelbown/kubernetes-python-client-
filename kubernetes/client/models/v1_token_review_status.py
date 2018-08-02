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


class V1TokenReviewStatus(object):
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
        'authenticated': 'bool',
        'error': 'str',
        'user': 'V1UserInfo'
    }

    attribute_map = {
        'authenticated': 'authenticated',
        'error': 'error',
        'user': 'user'
    }

    def __init__(self, authenticated=None, error=None, user=None):
        """
        V1TokenReviewStatus - a model defined in Swagger
        """

        self._authenticated = None
        self._error = None
        self._user = None
        self.discriminator = None

        if authenticated is not None:
          self.authenticated = authenticated
        if error is not None:
          self.error = error
        if user is not None:
          self.user = user

    @property
    def authenticated(self):
        """
        Gets the authenticated of this V1TokenReviewStatus.
        Authenticated indicates that the token was associated with a known user.

        :return: The authenticated of this V1TokenReviewStatus.
        :rtype: bool
        """
        return self._authenticated

    @authenticated.setter
    def authenticated(self, authenticated):
        """
        Sets the authenticated of this V1TokenReviewStatus.
        Authenticated indicates that the token was associated with a known user.

        :param authenticated: The authenticated of this V1TokenReviewStatus.
        :type: bool
        """

        self._authenticated = authenticated

    @property
    def error(self):
        """
        Gets the error of this V1TokenReviewStatus.
        Error indicates that the token couldn't be checked

        :return: The error of this V1TokenReviewStatus.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this V1TokenReviewStatus.
        Error indicates that the token couldn't be checked

        :param error: The error of this V1TokenReviewStatus.
        :type: str
        """

        self._error = error

    @property
    def user(self):
        """
        Gets the user of this V1TokenReviewStatus.
        User is the UserInfo associated with the provided token.

        :return: The user of this V1TokenReviewStatus.
        :rtype: V1UserInfo
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this V1TokenReviewStatus.
        User is the UserInfo associated with the provided token.

        :param user: The user of this V1TokenReviewStatus.
        :type: V1UserInfo
        """

        self._user = user

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
        if not isinstance(other, V1TokenReviewStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
