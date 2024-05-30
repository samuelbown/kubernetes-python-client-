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


class V1beta3ResourcePolicyRule(object):
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
        'api_groups': 'list[str]',
        'cluster_scope': 'bool',
        'namespaces': 'list[str]',
        'resources': 'list[str]',
        'verbs': 'list[str]'
    }

    attribute_map = {
        'api_groups': 'apiGroups',
        'cluster_scope': 'clusterScope',
        'namespaces': 'namespaces',
        'resources': 'resources',
        'verbs': 'verbs'
    }

    def __init__(self, api_groups=None, cluster_scope=None, namespaces=None, resources=None, verbs=None, local_vars_configuration=None):  # noqa: E501
        """V1beta3ResourcePolicyRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_groups = None
        self._cluster_scope = None
        self._namespaces = None
        self._resources = None
        self._verbs = None
        self.discriminator = None

        self.api_groups = api_groups
        if cluster_scope is not None:
            self.cluster_scope = cluster_scope
        if namespaces is not None:
            self.namespaces = namespaces
        self.resources = resources
        self.verbs = verbs

    @property
    def api_groups(self):
        """Gets the api_groups of this V1beta3ResourcePolicyRule.  # noqa: E501

        `apiGroups` is a list of matching API groups and may not be empty. \"*\" matches all API groups and, if present, must be the only entry. Required.  # noqa: E501

        :return: The api_groups of this V1beta3ResourcePolicyRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._api_groups

    @api_groups.setter
    def api_groups(self, api_groups):
        """Sets the api_groups of this V1beta3ResourcePolicyRule.

        `apiGroups` is a list of matching API groups and may not be empty. \"*\" matches all API groups and, if present, must be the only entry. Required.  # noqa: E501

        :param api_groups: The api_groups of this V1beta3ResourcePolicyRule.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and api_groups is None:  # noqa: E501
            raise ValueError("Invalid value for `api_groups`, must not be `None`")  # noqa: E501

        self._api_groups = api_groups

    @property
    def cluster_scope(self):
        """Gets the cluster_scope of this V1beta3ResourcePolicyRule.  # noqa: E501

        `clusterScope` indicates whether to match requests that do not specify a namespace (which happens either because the resource is not namespaced or the request targets all namespaces). If this field is omitted or false then the `namespaces` field must contain a non-empty list.  # noqa: E501

        :return: The cluster_scope of this V1beta3ResourcePolicyRule.  # noqa: E501
        :rtype: bool
        """
        return self._cluster_scope

    @cluster_scope.setter
    def cluster_scope(self, cluster_scope):
        """Sets the cluster_scope of this V1beta3ResourcePolicyRule.

        `clusterScope` indicates whether to match requests that do not specify a namespace (which happens either because the resource is not namespaced or the request targets all namespaces). If this field is omitted or false then the `namespaces` field must contain a non-empty list.  # noqa: E501

        :param cluster_scope: The cluster_scope of this V1beta3ResourcePolicyRule.  # noqa: E501
        :type: bool
        """

        self._cluster_scope = cluster_scope

    @property
    def namespaces(self):
        """Gets the namespaces of this V1beta3ResourcePolicyRule.  # noqa: E501

        `namespaces` is a list of target namespaces that restricts matches.  A request that specifies a target namespace matches only if either (a) this list contains that target namespace or (b) this list contains \"*\".  Note that \"*\" matches any specified namespace but does not match a request that _does not specify_ a namespace (see the `clusterScope` field for that). This list may be empty, but only if `clusterScope` is true.  # noqa: E501

        :return: The namespaces of this V1beta3ResourcePolicyRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this V1beta3ResourcePolicyRule.

        `namespaces` is a list of target namespaces that restricts matches.  A request that specifies a target namespace matches only if either (a) this list contains that target namespace or (b) this list contains \"*\".  Note that \"*\" matches any specified namespace but does not match a request that _does not specify_ a namespace (see the `clusterScope` field for that). This list may be empty, but only if `clusterScope` is true.  # noqa: E501

        :param namespaces: The namespaces of this V1beta3ResourcePolicyRule.  # noqa: E501
        :type: list[str]
        """

        self._namespaces = namespaces

    @property
    def resources(self):
        """Gets the resources of this V1beta3ResourcePolicyRule.  # noqa: E501

        `resources` is a list of matching resources (i.e., lowercase and plural) with, if desired, subresource.  For example, [ \"services\", \"nodes/status\" ].  This list may not be empty. \"*\" matches all resources and, if present, must be the only entry. Required.  # noqa: E501

        :return: The resources of this V1beta3ResourcePolicyRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this V1beta3ResourcePolicyRule.

        `resources` is a list of matching resources (i.e., lowercase and plural) with, if desired, subresource.  For example, [ \"services\", \"nodes/status\" ].  This list may not be empty. \"*\" matches all resources and, if present, must be the only entry. Required.  # noqa: E501

        :param resources: The resources of this V1beta3ResourcePolicyRule.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and resources is None:  # noqa: E501
            raise ValueError("Invalid value for `resources`, must not be `None`")  # noqa: E501

        self._resources = resources

    @property
    def verbs(self):
        """Gets the verbs of this V1beta3ResourcePolicyRule.  # noqa: E501

        `verbs` is a list of matching verbs and may not be empty. \"*\" matches all verbs and, if present, must be the only entry. Required.  # noqa: E501

        :return: The verbs of this V1beta3ResourcePolicyRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._verbs

    @verbs.setter
    def verbs(self, verbs):
        """Sets the verbs of this V1beta3ResourcePolicyRule.

        `verbs` is a list of matching verbs and may not be empty. \"*\" matches all verbs and, if present, must be the only entry. Required.  # noqa: E501

        :param verbs: The verbs of this V1beta3ResourcePolicyRule.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and verbs is None:  # noqa: E501
            raise ValueError("Invalid value for `verbs`, must not be `None`")  # noqa: E501

        self._verbs = verbs

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
        if not isinstance(other, V1beta3ResourcePolicyRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta3ResourcePolicyRule):
            return True

        return self.to_dict() != other.to_dict()
