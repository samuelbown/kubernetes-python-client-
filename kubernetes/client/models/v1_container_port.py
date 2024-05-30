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


class V1ContainerPort(object):
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
        'container_port': 'int',
        'host_ip': 'str',
        'host_port': 'int',
        'name': 'str',
        'protocol': 'str'
    }

    attribute_map = {
        'container_port': 'containerPort',
        'host_ip': 'hostIP',
        'host_port': 'hostPort',
        'name': 'name',
        'protocol': 'protocol'
    }

    def __init__(self, container_port=None, host_ip=None, host_port=None, name=None, protocol=None, local_vars_configuration=None):  # noqa: E501
        """V1ContainerPort - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._container_port = None
        self._host_ip = None
        self._host_port = None
        self._name = None
        self._protocol = None
        self.discriminator = None

        self.container_port = container_port
        if host_ip is not None:
            self.host_ip = host_ip
        if host_port is not None:
            self.host_port = host_port
        if name is not None:
            self.name = name
        if protocol is not None:
            self.protocol = protocol

    @property
    def container_port(self):
        """Gets the container_port of this V1ContainerPort.  # noqa: E501

        Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536.  # noqa: E501

        :return: The container_port of this V1ContainerPort.  # noqa: E501
        :rtype: int
        """
        return self._container_port

    @container_port.setter
    def container_port(self, container_port):
        """Sets the container_port of this V1ContainerPort.

        Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536.  # noqa: E501

        :param container_port: The container_port of this V1ContainerPort.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and container_port is None:  # noqa: E501
            raise ValueError("Invalid value for `container_port`, must not be `None`")  # noqa: E501

        self._container_port = container_port

    @property
    def host_ip(self):
        """Gets the host_ip of this V1ContainerPort.  # noqa: E501

        What host IP to bind the external port to.  # noqa: E501

        :return: The host_ip of this V1ContainerPort.  # noqa: E501
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this V1ContainerPort.

        What host IP to bind the external port to.  # noqa: E501

        :param host_ip: The host_ip of this V1ContainerPort.  # noqa: E501
        :type: str
        """

        self._host_ip = host_ip

    @property
    def host_port(self):
        """Gets the host_port of this V1ContainerPort.  # noqa: E501

        Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.  # noqa: E501

        :return: The host_port of this V1ContainerPort.  # noqa: E501
        :rtype: int
        """
        return self._host_port

    @host_port.setter
    def host_port(self, host_port):
        """Sets the host_port of this V1ContainerPort.

        Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.  # noqa: E501

        :param host_port: The host_port of this V1ContainerPort.  # noqa: E501
        :type: int
        """

        self._host_port = host_port

    @property
    def name(self):
        """Gets the name of this V1ContainerPort.  # noqa: E501

        If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.  # noqa: E501

        :return: The name of this V1ContainerPort.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1ContainerPort.

        If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.  # noqa: E501

        :param name: The name of this V1ContainerPort.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def protocol(self):
        """Gets the protocol of this V1ContainerPort.  # noqa: E501

        Protocol for port. Must be UDP, TCP, or SCTP. Defaults to \"TCP\".  # noqa: E501

        :return: The protocol of this V1ContainerPort.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this V1ContainerPort.

        Protocol for port. Must be UDP, TCP, or SCTP. Defaults to \"TCP\".  # noqa: E501

        :param protocol: The protocol of this V1ContainerPort.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

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
        if not isinstance(other, V1ContainerPort):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ContainerPort):
            return True

        return self.to_dict() != other.to_dict()
