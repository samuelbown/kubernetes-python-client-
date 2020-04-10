# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: release-1.15
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes.client
from kubernetes.client.api.authorization_v1_api import AuthorizationV1Api  # noqa: E501
from kubernetes.client.rest import ApiException


class TestAuthorizationV1Api(unittest.TestCase):
    """AuthorizationV1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.authorization_v1_api.AuthorizationV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_namespaced_local_subject_access_review(self):
        """Test case for create_namespaced_local_subject_access_review

        """
        pass

    def test_create_self_subject_access_review(self):
        """Test case for create_self_subject_access_review

        """
        pass

    def test_create_self_subject_rules_review(self):
        """Test case for create_self_subject_rules_review

        """
        pass

    def test_create_subject_access_review(self):
        """Test case for create_subject_access_review

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass


if __name__ == '__main__':
    unittest.main()
