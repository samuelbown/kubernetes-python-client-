# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.29
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1alpha1ServerStorageVersion(object):
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
        'api_server_id': 'str',
        'decodable_versions': 'list[str]',
        'encoding_version': 'str',
        'served_versions': 'list[str]'
    }

    attribute_map = {
        'api_server_id': 'apiServerID',
        'decodable_versions': 'decodableVersions',
        'encoding_version': 'encodingVersion',
        'served_versions': 'servedVersions'
    }

    def __init__(self, api_server_id=None, decodable_versions=None, encoding_version=None, served_versions=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ServerStorageVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_server_id = None
        self._decodable_versions = None
        self._encoding_version = None
        self._served_versions = None
        self.discriminator = None

        if api_server_id is not None:
            self.api_server_id = api_server_id
        if decodable_versions is not None:
            self.decodable_versions = decodable_versions
        if encoding_version is not None:
            self.encoding_version = encoding_version
        if served_versions is not None:
            self.served_versions = served_versions

    @property
    def api_server_id(self):
        """Gets the api_server_id of this V1alpha1ServerStorageVersion.  # noqa: E501

        The ID of the reporting API server.  # noqa: E501

        :return: The api_server_id of this V1alpha1ServerStorageVersion.  # noqa: E501
        :rtype: str
        """
        return self._api_server_id

    @api_server_id.setter
    def api_server_id(self, api_server_id):
        """Sets the api_server_id of this V1alpha1ServerStorageVersion.

        The ID of the reporting API server.  # noqa: E501

        :param api_server_id: The api_server_id of this V1alpha1ServerStorageVersion.  # noqa: E501
        :type: str
        """

        self._api_server_id = api_server_id

    @property
    def decodable_versions(self):
        """Gets the decodable_versions of this V1alpha1ServerStorageVersion.  # noqa: E501

        The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions.  # noqa: E501

        :return: The decodable_versions of this V1alpha1ServerStorageVersion.  # noqa: E501
        :rtype: list[str]
        """
        return self._decodable_versions

    @decodable_versions.setter
    def decodable_versions(self, decodable_versions):
        """Sets the decodable_versions of this V1alpha1ServerStorageVersion.

        The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions.  # noqa: E501

        :param decodable_versions: The decodable_versions of this V1alpha1ServerStorageVersion.  # noqa: E501
        :type: list[str]
        """

        self._decodable_versions = decodable_versions

    @property
    def encoding_version(self):
        """Gets the encoding_version of this V1alpha1ServerStorageVersion.  # noqa: E501

        The API server encodes the object to this version when persisting it in the backend (e.g., etcd).  # noqa: E501

        :return: The encoding_version of this V1alpha1ServerStorageVersion.  # noqa: E501
        :rtype: str
        """
        return self._encoding_version

    @encoding_version.setter
    def encoding_version(self, encoding_version):
        """Sets the encoding_version of this V1alpha1ServerStorageVersion.

        The API server encodes the object to this version when persisting it in the backend (e.g., etcd).  # noqa: E501

        :param encoding_version: The encoding_version of this V1alpha1ServerStorageVersion.  # noqa: E501
        :type: str
        """

        self._encoding_version = encoding_version

    @property
    def served_versions(self):
        """Gets the served_versions of this V1alpha1ServerStorageVersion.  # noqa: E501

        The API server can serve these versions. DecodableVersions must include all ServedVersions.  # noqa: E501

        :return: The served_versions of this V1alpha1ServerStorageVersion.  # noqa: E501
        :rtype: list[str]
        """
        return self._served_versions

    @served_versions.setter
    def served_versions(self, served_versions):
        """Sets the served_versions of this V1alpha1ServerStorageVersion.

        The API server can serve these versions. DecodableVersions must include all ServedVersions.  # noqa: E501

        :param served_versions: The served_versions of this V1alpha1ServerStorageVersion.  # noqa: E501
        :type: list[str]
        """

        self._served_versions = served_versions

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
        if not isinstance(other, V1alpha1ServerStorageVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ServerStorageVersion):
            return True

        return self.to_dict() != other.to_dict()
