# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.13.3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes.client
from kubernetes.client.api.rbac_authorization_api import RbacAuthorizationApi  # noqa: E501
from kubernetes.client.rest import ApiException


class TestRbacAuthorizationApi(unittest.TestCase):
    """RbacAuthorizationApi unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.rbac_authorization_api.RbacAuthorizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_group(self):
        """Test case for get_api_group

        """
        pass


if __name__ == '__main__':
    unittest.main()
