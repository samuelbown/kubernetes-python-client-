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


class V1PodResourceClaimStatus(object):
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
        'resource_claim_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'resource_claim_name': 'resourceClaimName'
    }

    def __init__(self, name=None, resource_claim_name=None, local_vars_configuration=None):  # noqa: E501
        """V1PodResourceClaimStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._resource_claim_name = None
        self.discriminator = None

        self.name = name
        if resource_claim_name is not None:
            self.resource_claim_name = resource_claim_name

    @property
    def name(self):
        """Gets the name of this V1PodResourceClaimStatus.  # noqa: E501

        Name uniquely identifies this resource claim inside the pod. This must match the name of an entry in pod.spec.resourceClaims, which implies that the string must be a DNS_LABEL.  # noqa: E501

        :return: The name of this V1PodResourceClaimStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1PodResourceClaimStatus.

        Name uniquely identifies this resource claim inside the pod. This must match the name of an entry in pod.spec.resourceClaims, which implies that the string must be a DNS_LABEL.  # noqa: E501

        :param name: The name of this V1PodResourceClaimStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def resource_claim_name(self):
        """Gets the resource_claim_name of this V1PodResourceClaimStatus.  # noqa: E501

        ResourceClaimName is the name of the ResourceClaim that was generated for the Pod in the namespace of the Pod. It this is unset, then generating a ResourceClaim was not necessary. The pod.spec.resourceClaims entry can be ignored in this case.  # noqa: E501

        :return: The resource_claim_name of this V1PodResourceClaimStatus.  # noqa: E501
        :rtype: str
        """
        return self._resource_claim_name

    @resource_claim_name.setter
    def resource_claim_name(self, resource_claim_name):
        """Sets the resource_claim_name of this V1PodResourceClaimStatus.

        ResourceClaimName is the name of the ResourceClaim that was generated for the Pod in the namespace of the Pod. It this is unset, then generating a ResourceClaim was not necessary. The pod.spec.resourceClaims entry can be ignored in this case.  # noqa: E501

        :param resource_claim_name: The resource_claim_name of this V1PodResourceClaimStatus.  # noqa: E501
        :type: str
        """

        self._resource_claim_name = resource_claim_name

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
        if not isinstance(other, V1PodResourceClaimStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PodResourceClaimStatus):
            return True

        return self.to_dict() != other.to_dict()
