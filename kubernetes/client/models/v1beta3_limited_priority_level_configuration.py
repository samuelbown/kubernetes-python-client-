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


class V1beta3LimitedPriorityLevelConfiguration(object):
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
        'borrowing_limit_percent': 'int',
        'lendable_percent': 'int',
        'limit_response': 'V1beta3LimitResponse',
        'nominal_concurrency_shares': 'int'
    }

    attribute_map = {
        'borrowing_limit_percent': 'borrowingLimitPercent',
        'lendable_percent': 'lendablePercent',
        'limit_response': 'limitResponse',
        'nominal_concurrency_shares': 'nominalConcurrencyShares'
    }

    def __init__(self, borrowing_limit_percent=None, lendable_percent=None, limit_response=None, nominal_concurrency_shares=None, local_vars_configuration=None):  # noqa: E501
        """V1beta3LimitedPriorityLevelConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._borrowing_limit_percent = None
        self._lendable_percent = None
        self._limit_response = None
        self._nominal_concurrency_shares = None
        self.discriminator = None

        if borrowing_limit_percent is not None:
            self.borrowing_limit_percent = borrowing_limit_percent
        if lendable_percent is not None:
            self.lendable_percent = lendable_percent
        if limit_response is not None:
            self.limit_response = limit_response
        if nominal_concurrency_shares is not None:
            self.nominal_concurrency_shares = nominal_concurrency_shares

    @property
    def borrowing_limit_percent(self):
        """Gets the borrowing_limit_percent of this V1beta3LimitedPriorityLevelConfiguration.  # noqa: E501

        `borrowingLimitPercent`, if present, configures a limit on how many seats this priority level can borrow from other priority levels. The limit is known as this level's BorrowingConcurrencyLimit (BorrowingCL) and is a limit on the total number of seats that this level may borrow at any one time. This field holds the ratio of that limit to the level's nominal concurrency limit. When this field is non-nil, it must hold a non-negative integer and the limit is calculated as follows.  BorrowingCL(i) = round( NominalCL(i) * borrowingLimitPercent(i)/100.0 )  The value of this field can be more than 100, implying that this priority level can borrow a number of seats that is greater than its own nominal concurrency limit (NominalCL). When this field is left `nil`, the limit is effectively infinite.  # noqa: E501

        :return: The borrowing_limit_percent of this V1beta3LimitedPriorityLevelConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._borrowing_limit_percent

    @borrowing_limit_percent.setter
    def borrowing_limit_percent(self, borrowing_limit_percent):
        """Sets the borrowing_limit_percent of this V1beta3LimitedPriorityLevelConfiguration.

        `borrowingLimitPercent`, if present, configures a limit on how many seats this priority level can borrow from other priority levels. The limit is known as this level's BorrowingConcurrencyLimit (BorrowingCL) and is a limit on the total number of seats that this level may borrow at any one time. This field holds the ratio of that limit to the level's nominal concurrency limit. When this field is non-nil, it must hold a non-negative integer and the limit is calculated as follows.  BorrowingCL(i) = round( NominalCL(i) * borrowingLimitPercent(i)/100.0 )  The value of this field can be more than 100, implying that this priority level can borrow a number of seats that is greater than its own nominal concurrency limit (NominalCL). When this field is left `nil`, the limit is effectively infinite.  # noqa: E501

        :param borrowing_limit_percent: The borrowing_limit_percent of this V1beta3LimitedPriorityLevelConfiguration.  # noqa: E501
        :type: int
        """

        self._borrowing_limit_percent = borrowing_limit_percent

    @property
    def lendable_percent(self):
        """Gets the lendable_percent of this V1beta3LimitedPriorityLevelConfiguration.  # noqa: E501

        `lendablePercent` prescribes the fraction of the level's NominalCL that can be borrowed by other priority levels. The value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level's LendableConcurrencyLimit (LendableCL), is defined as follows.  LendableCL(i) = round( NominalCL(i) * lendablePercent(i)/100.0 )  # noqa: E501

        :return: The lendable_percent of this V1beta3LimitedPriorityLevelConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._lendable_percent

    @lendable_percent.setter
    def lendable_percent(self, lendable_percent):
        """Sets the lendable_percent of this V1beta3LimitedPriorityLevelConfiguration.

        `lendablePercent` prescribes the fraction of the level's NominalCL that can be borrowed by other priority levels. The value of this field must be between 0 and 100, inclusive, and it defaults to 0. The number of seats that other levels can borrow from this level, known as this level's LendableConcurrencyLimit (LendableCL), is defined as follows.  LendableCL(i) = round( NominalCL(i) * lendablePercent(i)/100.0 )  # noqa: E501

        :param lendable_percent: The lendable_percent of this V1beta3LimitedPriorityLevelConfiguration.  # noqa: E501
        :type: int
        """

        self._lendable_percent = lendable_percent

    @property
    def limit_response(self):
        """Gets the limit_response of this V1beta3LimitedPriorityLevelConfiguration.  # noqa: E501


        :return: The limit_response of this V1beta3LimitedPriorityLevelConfiguration.  # noqa: E501
        :rtype: V1beta3LimitResponse
        """
        return self._limit_response

    @limit_response.setter
    def limit_response(self, limit_response):
        """Sets the limit_response of this V1beta3LimitedPriorityLevelConfiguration.


        :param limit_response: The limit_response of this V1beta3LimitedPriorityLevelConfiguration.  # noqa: E501
        :type: V1beta3LimitResponse
        """

        self._limit_response = limit_response

    @property
    def nominal_concurrency_shares(self):
        """Gets the nominal_concurrency_shares of this V1beta3LimitedPriorityLevelConfiguration.  # noqa: E501

        `nominalConcurrencyShares` (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats available at this priority level. This is used both for requests dispatched from this priority level as well as requests dispatched from other priority levels borrowing seats from this level. The server's concurrency limit (ServerCL) is divided among the Limited priority levels in proportion to their NCS values:  NominalCL(i)  = ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k] NCS(k)  Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level. This field has a default value of 30.  # noqa: E501

        :return: The nominal_concurrency_shares of this V1beta3LimitedPriorityLevelConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._nominal_concurrency_shares

    @nominal_concurrency_shares.setter
    def nominal_concurrency_shares(self, nominal_concurrency_shares):
        """Sets the nominal_concurrency_shares of this V1beta3LimitedPriorityLevelConfiguration.

        `nominalConcurrencyShares` (NCS) contributes to the computation of the NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats available at this priority level. This is used both for requests dispatched from this priority level as well as requests dispatched from other priority levels borrowing seats from this level. The server's concurrency limit (ServerCL) is divided among the Limited priority levels in proportion to their NCS values:  NominalCL(i)  = ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k] NCS(k)  Bigger numbers mean a larger nominal concurrency limit, at the expense of every other priority level. This field has a default value of 30.  # noqa: E501

        :param nominal_concurrency_shares: The nominal_concurrency_shares of this V1beta3LimitedPriorityLevelConfiguration.  # noqa: E501
        :type: int
        """

        self._nominal_concurrency_shares = nominal_concurrency_shares

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
        if not isinstance(other, V1beta3LimitedPriorityLevelConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta3LimitedPriorityLevelConfiguration):
            return True

        return self.to_dict() != other.to_dict()
