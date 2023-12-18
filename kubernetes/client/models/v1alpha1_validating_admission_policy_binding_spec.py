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


class V1alpha1ValidatingAdmissionPolicyBindingSpec(object):
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
        'match_resources': 'V1alpha1MatchResources',
        'param_ref': 'V1alpha1ParamRef',
        'policy_name': 'str',
        'validation_actions': 'list[str]'
    }

    attribute_map = {
        'match_resources': 'matchResources',
        'param_ref': 'paramRef',
        'policy_name': 'policyName',
        'validation_actions': 'validationActions'
    }

    def __init__(self, match_resources=None, param_ref=None, policy_name=None, validation_actions=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ValidatingAdmissionPolicyBindingSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._match_resources = None
        self._param_ref = None
        self._policy_name = None
        self._validation_actions = None
        self.discriminator = None

        if match_resources is not None:
            self.match_resources = match_resources
        if param_ref is not None:
            self.param_ref = param_ref
        if policy_name is not None:
            self.policy_name = policy_name
        if validation_actions is not None:
            self.validation_actions = validation_actions

    @property
    def match_resources(self):
        """Gets the match_resources of this V1alpha1ValidatingAdmissionPolicyBindingSpec.  # noqa: E501


        :return: The match_resources of this V1alpha1ValidatingAdmissionPolicyBindingSpec.  # noqa: E501
        :rtype: V1alpha1MatchResources
        """
        return self._match_resources

    @match_resources.setter
    def match_resources(self, match_resources):
        """Sets the match_resources of this V1alpha1ValidatingAdmissionPolicyBindingSpec.


        :param match_resources: The match_resources of this V1alpha1ValidatingAdmissionPolicyBindingSpec.  # noqa: E501
        :type: V1alpha1MatchResources
        """

        self._match_resources = match_resources

    @property
    def param_ref(self):
        """Gets the param_ref of this V1alpha1ValidatingAdmissionPolicyBindingSpec.  # noqa: E501


        :return: The param_ref of this V1alpha1ValidatingAdmissionPolicyBindingSpec.  # noqa: E501
        :rtype: V1alpha1ParamRef
        """
        return self._param_ref

    @param_ref.setter
    def param_ref(self, param_ref):
        """Sets the param_ref of this V1alpha1ValidatingAdmissionPolicyBindingSpec.


        :param param_ref: The param_ref of this V1alpha1ValidatingAdmissionPolicyBindingSpec.  # noqa: E501
        :type: V1alpha1ParamRef
        """

        self._param_ref = param_ref

    @property
    def policy_name(self):
        """Gets the policy_name of this V1alpha1ValidatingAdmissionPolicyBindingSpec.  # noqa: E501

        PolicyName references a ValidatingAdmissionPolicy name which the ValidatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding is considered invalid and will be ignored Required.  # noqa: E501

        :return: The policy_name of this V1alpha1ValidatingAdmissionPolicyBindingSpec.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this V1alpha1ValidatingAdmissionPolicyBindingSpec.

        PolicyName references a ValidatingAdmissionPolicy name which the ValidatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding is considered invalid and will be ignored Required.  # noqa: E501

        :param policy_name: The policy_name of this V1alpha1ValidatingAdmissionPolicyBindingSpec.  # noqa: E501
        :type: str
        """

        self._policy_name = policy_name

    @property
    def validation_actions(self):
        """Gets the validation_actions of this V1alpha1ValidatingAdmissionPolicyBindingSpec.  # noqa: E501

        validationActions declares how Validations of the referenced ValidatingAdmissionPolicy are enforced. If a validation evaluates to false it is always enforced according to these actions.  Failures defined by the ValidatingAdmissionPolicy's FailurePolicy are enforced according to these actions only if the FailurePolicy is set to Fail, otherwise the failures are ignored. This includes compilation errors, runtime errors and misconfigurations of the policy.  validationActions is declared as a set of action values. Order does not matter. validationActions may not contain duplicates of the same action.  The supported actions values are:  \"Deny\" specifies that a validation failure results in a denied request.  \"Warn\" specifies that a validation failure is reported to the request client in HTTP Warning headers, with a warning code of 299. Warnings can be sent both for allowed or denied admission responses.  \"Audit\" specifies that a validation failure is included in the published audit event for the request. The audit event will contain a `validation.policy.admission.k8s.io/validation_failure` audit annotation with a value containing the details of the validation failures, formatted as a JSON list of objects, each with the following fields: - message: The validation failure message string - policy: The resource name of the ValidatingAdmissionPolicy - binding: The resource name of the ValidatingAdmissionPolicyBinding - expressionIndex: The index of the failed validations in the ValidatingAdmissionPolicy - validationActions: The enforcement actions enacted for the validation failure Example audit annotation: `\"validation.policy.admission.k8s.io/validation_failure\": \"[{\"message\": \"Invalid value\", {\"policy\": \"policy.example.com\", {\"binding\": \"policybinding.example.com\", {\"expressionIndex\": \"1\", {\"validationActions\": [\"Audit\"]}]\"`  Clients should expect to handle additional values by ignoring any values not recognized.  \"Deny\" and \"Warn\" may not be used together since this combination needlessly duplicates the validation failure both in the API response body and the HTTP warning headers.  Required.  # noqa: E501

        :return: The validation_actions of this V1alpha1ValidatingAdmissionPolicyBindingSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._validation_actions

    @validation_actions.setter
    def validation_actions(self, validation_actions):
        """Sets the validation_actions of this V1alpha1ValidatingAdmissionPolicyBindingSpec.

        validationActions declares how Validations of the referenced ValidatingAdmissionPolicy are enforced. If a validation evaluates to false it is always enforced according to these actions.  Failures defined by the ValidatingAdmissionPolicy's FailurePolicy are enforced according to these actions only if the FailurePolicy is set to Fail, otherwise the failures are ignored. This includes compilation errors, runtime errors and misconfigurations of the policy.  validationActions is declared as a set of action values. Order does not matter. validationActions may not contain duplicates of the same action.  The supported actions values are:  \"Deny\" specifies that a validation failure results in a denied request.  \"Warn\" specifies that a validation failure is reported to the request client in HTTP Warning headers, with a warning code of 299. Warnings can be sent both for allowed or denied admission responses.  \"Audit\" specifies that a validation failure is included in the published audit event for the request. The audit event will contain a `validation.policy.admission.k8s.io/validation_failure` audit annotation with a value containing the details of the validation failures, formatted as a JSON list of objects, each with the following fields: - message: The validation failure message string - policy: The resource name of the ValidatingAdmissionPolicy - binding: The resource name of the ValidatingAdmissionPolicyBinding - expressionIndex: The index of the failed validations in the ValidatingAdmissionPolicy - validationActions: The enforcement actions enacted for the validation failure Example audit annotation: `\"validation.policy.admission.k8s.io/validation_failure\": \"[{\"message\": \"Invalid value\", {\"policy\": \"policy.example.com\", {\"binding\": \"policybinding.example.com\", {\"expressionIndex\": \"1\", {\"validationActions\": [\"Audit\"]}]\"`  Clients should expect to handle additional values by ignoring any values not recognized.  \"Deny\" and \"Warn\" may not be used together since this combination needlessly duplicates the validation failure both in the API response body and the HTTP warning headers.  Required.  # noqa: E501

        :param validation_actions: The validation_actions of this V1alpha1ValidatingAdmissionPolicyBindingSpec.  # noqa: E501
        :type: list[str]
        """

        self._validation_actions = validation_actions

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
        if not isinstance(other, V1alpha1ValidatingAdmissionPolicyBindingSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ValidatingAdmissionPolicyBindingSpec):
            return True

        return self.to_dict() != other.to_dict()
