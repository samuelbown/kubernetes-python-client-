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


class V1DeleteOptions(object):
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
        'api_version': 'str',
        'dry_run': 'list[str]',
        'grace_period_seconds': 'int',
        'kind': 'str',
        'orphan_dependents': 'bool',
        'preconditions': 'V1Preconditions',
        'propagation_policy': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'dry_run': 'dryRun',
        'grace_period_seconds': 'gracePeriodSeconds',
        'kind': 'kind',
        'orphan_dependents': 'orphanDependents',
        'preconditions': 'preconditions',
        'propagation_policy': 'propagationPolicy'
    }

    def __init__(self, api_version=None, dry_run=None, grace_period_seconds=None, kind=None, orphan_dependents=None, preconditions=None, propagation_policy=None, local_vars_configuration=None):  # noqa: E501
        """V1DeleteOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._dry_run = None
        self._grace_period_seconds = None
        self._kind = None
        self._orphan_dependents = None
        self._preconditions = None
        self._propagation_policy = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if dry_run is not None:
            self.dry_run = dry_run
        if grace_period_seconds is not None:
            self.grace_period_seconds = grace_period_seconds
        if kind is not None:
            self.kind = kind
        if orphan_dependents is not None:
            self.orphan_dependents = orphan_dependents
        if preconditions is not None:
            self.preconditions = preconditions
        if propagation_policy is not None:
            self.propagation_policy = propagation_policy

    @property
    def api_version(self):
        """Gets the api_version of this V1DeleteOptions.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1DeleteOptions.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1DeleteOptions.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1DeleteOptions.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def dry_run(self):
        """Gets the dry_run of this V1DeleteOptions.  # noqa: E501

        When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed  # noqa: E501

        :return: The dry_run of this V1DeleteOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this V1DeleteOptions.

        When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed  # noqa: E501

        :param dry_run: The dry_run of this V1DeleteOptions.  # noqa: E501
        :type: list[str]
        """

        self._dry_run = dry_run

    @property
    def grace_period_seconds(self):
        """Gets the grace_period_seconds of this V1DeleteOptions.  # noqa: E501

        The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.  # noqa: E501

        :return: The grace_period_seconds of this V1DeleteOptions.  # noqa: E501
        :rtype: int
        """
        return self._grace_period_seconds

    @grace_period_seconds.setter
    def grace_period_seconds(self, grace_period_seconds):
        """Sets the grace_period_seconds of this V1DeleteOptions.

        The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.  # noqa: E501

        :param grace_period_seconds: The grace_period_seconds of this V1DeleteOptions.  # noqa: E501
        :type: int
        """

        self._grace_period_seconds = grace_period_seconds

    @property
    def kind(self):
        """Gets the kind of this V1DeleteOptions.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1DeleteOptions.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1DeleteOptions.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1DeleteOptions.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def orphan_dependents(self):
        """Gets the orphan_dependents of this V1DeleteOptions.  # noqa: E501

        Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both.  # noqa: E501

        :return: The orphan_dependents of this V1DeleteOptions.  # noqa: E501
        :rtype: bool
        """
        return self._orphan_dependents

    @orphan_dependents.setter
    def orphan_dependents(self, orphan_dependents):
        """Sets the orphan_dependents of this V1DeleteOptions.

        Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both.  # noqa: E501

        :param orphan_dependents: The orphan_dependents of this V1DeleteOptions.  # noqa: E501
        :type: bool
        """

        self._orphan_dependents = orphan_dependents

    @property
    def preconditions(self):
        """Gets the preconditions of this V1DeleteOptions.  # noqa: E501


        :return: The preconditions of this V1DeleteOptions.  # noqa: E501
        :rtype: V1Preconditions
        """
        return self._preconditions

    @preconditions.setter
    def preconditions(self, preconditions):
        """Sets the preconditions of this V1DeleteOptions.


        :param preconditions: The preconditions of this V1DeleteOptions.  # noqa: E501
        :type: V1Preconditions
        """

        self._preconditions = preconditions

    @property
    def propagation_policy(self):
        """Gets the propagation_policy of this V1DeleteOptions.  # noqa: E501

        Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground.  # noqa: E501

        :return: The propagation_policy of this V1DeleteOptions.  # noqa: E501
        :rtype: str
        """
        return self._propagation_policy

    @propagation_policy.setter
    def propagation_policy(self, propagation_policy):
        """Sets the propagation_policy of this V1DeleteOptions.

        Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground.  # noqa: E501

        :param propagation_policy: The propagation_policy of this V1DeleteOptions.  # noqa: E501
        :type: str
        """

        self._propagation_policy = propagation_policy

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
        if not isinstance(other, V1DeleteOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DeleteOptions):
            return True

        return self.to_dict() != other.to_dict()
