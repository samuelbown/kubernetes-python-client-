"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.18
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from kubernetes.client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from kubernetes.client.model.v1beta1_custom_resource_column_definition import V1beta1CustomResourceColumnDefinition
    from kubernetes.client.model.v1beta1_custom_resource_conversion import V1beta1CustomResourceConversion
    from kubernetes.client.model.v1beta1_custom_resource_definition_names import V1beta1CustomResourceDefinitionNames
    from kubernetes.client.model.v1beta1_custom_resource_definition_version import V1beta1CustomResourceDefinitionVersion
    from kubernetes.client.model.v1beta1_custom_resource_subresources import V1beta1CustomResourceSubresources
    from kubernetes.client.model.v1beta1_custom_resource_validation import V1beta1CustomResourceValidation
    globals()['V1beta1CustomResourceColumnDefinition'] = V1beta1CustomResourceColumnDefinition
    globals()['V1beta1CustomResourceConversion'] = V1beta1CustomResourceConversion
    globals()['V1beta1CustomResourceDefinitionNames'] = V1beta1CustomResourceDefinitionNames
    globals()['V1beta1CustomResourceDefinitionVersion'] = V1beta1CustomResourceDefinitionVersion
    globals()['V1beta1CustomResourceSubresources'] = V1beta1CustomResourceSubresources
    globals()['V1beta1CustomResourceValidation'] = V1beta1CustomResourceValidation


class V1beta1CustomResourceDefinitionSpec(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'group': (str,),  # noqa: E501
            'names': (V1beta1CustomResourceDefinitionNames,),  # noqa: E501
            'scope': (str,),  # noqa: E501
            'additional_printer_columns': ([V1beta1CustomResourceColumnDefinition],),  # noqa: E501
            'conversion': (V1beta1CustomResourceConversion,),  # noqa: E501
            'preserve_unknown_fields': (bool,),  # noqa: E501
            'subresources': (V1beta1CustomResourceSubresources,),  # noqa: E501
            'validation': (V1beta1CustomResourceValidation,),  # noqa: E501
            'version': (str,),  # noqa: E501
            'versions': ([V1beta1CustomResourceDefinitionVersion],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'group': 'group',  # noqa: E501
        'names': 'names',  # noqa: E501
        'scope': 'scope',  # noqa: E501
        'additional_printer_columns': 'additionalPrinterColumns',  # noqa: E501
        'conversion': 'conversion',  # noqa: E501
        'preserve_unknown_fields': 'preserveUnknownFields',  # noqa: E501
        'subresources': 'subresources',  # noqa: E501
        'validation': 'validation',  # noqa: E501
        'version': 'version',  # noqa: E501
        'versions': 'versions',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, group, names, scope, *args, **kwargs):  # noqa: E501
        """V1beta1CustomResourceDefinitionSpec - a model defined in OpenAPI

        Args:
            group (str): group is the API group of the defined custom resource. The custom resources are served under `/apis/<group>/...`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`).
            names (V1beta1CustomResourceDefinitionNames):
            scope (str): scope indicates whether the defined custom resource is cluster- or namespace-scoped. Allowed values are `Cluster` and `Namespaced`. Default is `Namespaced`.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            additional_printer_columns ([V1beta1CustomResourceColumnDefinition]): additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. If present, this field configures columns for all versions. Top-level and per-version columns are mutually exclusive. If no top-level or per-version columns are specified, a single column displaying the age of the custom resource is used.. [optional]  # noqa: E501
            conversion (V1beta1CustomResourceConversion): [optional]  # noqa: E501
            preserve_unknown_fields (bool): preserveUnknownFields indicates that object fields which are not specified in the OpenAPI schema should be preserved when persisting to storage. apiVersion, kind, metadata and known fields inside metadata are always preserved. If false, schemas must be defined for all versions. Defaults to true in v1beta for backwards compatibility. Deprecated: will be required to be false in v1. Preservation of unknown fields can be specified in the validation schema using the `x-kubernetes-preserve-unknown-fields: true` extension. See https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/#pruning-versus-preserving-unknown-fields for details.. [optional]  # noqa: E501
            subresources (V1beta1CustomResourceSubresources): [optional]  # noqa: E501
            validation (V1beta1CustomResourceValidation): [optional]  # noqa: E501
            version (str): version is the API version of the defined custom resource. The custom resources are served under `/apis/<group>/<version>/...`. Must match the name of the first item in the `versions` list if `version` and `versions` are both specified. Optional if `versions` is specified. Deprecated: use `versions` instead.. [optional]  # noqa: E501
            versions ([V1beta1CustomResourceDefinitionVersion]): versions is the list of all API versions of the defined custom resource. Optional if `version` is specified. The name of the first item in the `versions` list must match the `version` field if `version` and `versions` are both specified. Version names are used to compute the order in which served versions are listed in API discovery. If the version string is \"kube-like\", it will sort above non \"kube-like\" version strings, which are ordered lexicographically. \"Kube-like\" versions start with a \"v\", then are followed by a number (the major version), then optionally the string \"alpha\" or \"beta\" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.group = group
        self.names = names
        self.scope = scope
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
