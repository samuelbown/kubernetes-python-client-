# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.25
    Generated by: https://openapi-generator.tech
"""

from kubernetes.client.paths.apis_node_k8s_io_v1_runtimeclasses.post import CreateRuntimeClass
from kubernetes.client.paths.apis_node_k8s_io_v1_runtimeclasses.delete import DeleteCollectionRuntimeClass
from kubernetes.client.paths.apis_node_k8s_io_v1_runtimeclasses_name.delete import DeleteRuntimeClass
from kubernetes.client.paths.apis_node_k8s_io_v1_.get import GetApiResources
from kubernetes.client.paths.apis_node_k8s_io_v1_runtimeclasses.get import ListRuntimeClass
from kubernetes.client.paths.apis_node_k8s_io_v1_runtimeclasses_name.patch import PatchRuntimeClass
from kubernetes.client.paths.apis_node_k8s_io_v1_runtimeclasses_name.get import ReadRuntimeClass
from kubernetes.client.paths.apis_node_k8s_io_v1_runtimeclasses_name.put import ReplaceRuntimeClass


class NodeV1Api(
    CreateRuntimeClass,
    DeleteCollectionRuntimeClass,
    DeleteRuntimeClass,
    GetApiResources,
    ListRuntimeClass,
    PatchRuntimeClass,
    ReadRuntimeClass,
    ReplaceRuntimeClass,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
