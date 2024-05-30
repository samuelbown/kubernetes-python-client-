# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.30
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


from kubernetes.client.configuration import Configuration


class V1VolumeAttachmentSpec(object):
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
        'attacher': 'str',
        'node_name': 'str',
        'source': 'V1VolumeAttachmentSource'
    }

    attribute_map = {
        'attacher': 'attacher',
        'node_name': 'nodeName',
        'source': 'source'
    }

    def __init__(self, attacher=None, node_name=None, source=None, local_vars_configuration=None):  # noqa: E501
        """V1VolumeAttachmentSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attacher = None
        self._node_name = None
        self._source = None
        self.discriminator = None

        self.attacher = attacher
        self.node_name = node_name
        self.source = source

    @property
    def attacher(self):
        """Gets the attacher of this V1VolumeAttachmentSpec.  # noqa: E501

        attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().  # noqa: E501

        :return: The attacher of this V1VolumeAttachmentSpec.  # noqa: E501
        :rtype: str
        """
        return self._attacher

    @attacher.setter
    def attacher(self, attacher):
        """Sets the attacher of this V1VolumeAttachmentSpec.

        attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().  # noqa: E501

        :param attacher: The attacher of this V1VolumeAttachmentSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and attacher is None:  # noqa: E501
            raise ValueError("Invalid value for `attacher`, must not be `None`")  # noqa: E501

        self._attacher = attacher

    @property
    def node_name(self):
        """Gets the node_name of this V1VolumeAttachmentSpec.  # noqa: E501

        nodeName represents the node that the volume should be attached to.  # noqa: E501

        :return: The node_name of this V1VolumeAttachmentSpec.  # noqa: E501
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this V1VolumeAttachmentSpec.

        nodeName represents the node that the volume should be attached to.  # noqa: E501

        :param node_name: The node_name of this V1VolumeAttachmentSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and node_name is None:  # noqa: E501
            raise ValueError("Invalid value for `node_name`, must not be `None`")  # noqa: E501

        self._node_name = node_name

    @property
    def source(self):
        """Gets the source of this V1VolumeAttachmentSpec.  # noqa: E501


        :return: The source of this V1VolumeAttachmentSpec.  # noqa: E501
        :rtype: V1VolumeAttachmentSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this V1VolumeAttachmentSpec.


        :param source: The source of this V1VolumeAttachmentSpec.  # noqa: E501
        :type: V1VolumeAttachmentSource
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.openapi_types.items():
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
        if not isinstance(other, V1VolumeAttachmentSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1VolumeAttachmentSpec):
            return True

        return self.to_dict() != other.to_dict()
