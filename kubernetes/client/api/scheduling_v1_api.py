# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.25
    Generated by: https://openapi-generator.tech
"""

from kubernetes.client.paths.apis_scheduling_k8s_io_v1_priorityclasses.post import CreatePriorityClass
from kubernetes.client.paths.apis_scheduling_k8s_io_v1_priorityclasses.delete import DeleteCollectionPriorityClass
from kubernetes.client.paths.apis_scheduling_k8s_io_v1_priorityclasses_name.delete import DeletePriorityClass
from kubernetes.client.paths.apis_scheduling_k8s_io_v1_.get import GetApiResources
from kubernetes.client.paths.apis_scheduling_k8s_io_v1_priorityclasses.get import ListPriorityClass
from kubernetes.client.paths.apis_scheduling_k8s_io_v1_priorityclasses_name.patch import PatchPriorityClass
from kubernetes.client.paths.apis_scheduling_k8s_io_v1_priorityclasses_name.get import ReadPriorityClass
from kubernetes.client.paths.apis_scheduling_k8s_io_v1_priorityclasses_name.put import ReplacePriorityClass


class SchedulingV1Api(
    CreatePriorityClass,
    DeleteCollectionPriorityClass,
    DeletePriorityClass,
    GetApiResources,
    ListPriorityClass,
    PatchPriorityClass,
    ReadPriorityClass,
    ReplacePriorityClass,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
