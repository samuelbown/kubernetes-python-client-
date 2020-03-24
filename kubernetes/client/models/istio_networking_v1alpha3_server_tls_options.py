# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.15.6
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class IstioNetworkingV1alpha3ServerTLSOptions(object):
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
        'mode': 'str',
        'private_key': 'str',
        'ca_certificates': 'str',
        'subject_alt_names': 'list[str]',
        'https_redirect': 'bool',
        'server_certificate': 'str',
        'credential_name': 'str',
        'verify_certificate_spki': 'list[str]',
        'verify_certificate_hash': 'list[str]',
        'min_protocol_version': 'str',
        'max_protocol_version': 'str',
        'cipher_suites': 'list[str]'
    }

    attribute_map = {
        'mode': 'mode',
        'private_key': 'privateKey',
        'ca_certificates': 'caCertificates',
        'subject_alt_names': 'subjectAltNames',
        'https_redirect': 'httpsRedirect',
        'server_certificate': 'serverCertificate',
        'credential_name': 'credentialName',
        'verify_certificate_spki': 'verifyCertificateSpki',
        'verify_certificate_hash': 'verifyCertificateHash',
        'min_protocol_version': 'minProtocolVersion',
        'max_protocol_version': 'maxProtocolVersion',
        'cipher_suites': 'cipherSuites'
    }

    def __init__(self, mode=None, private_key=None, ca_certificates=None, subject_alt_names=None, https_redirect=None, server_certificate=None, credential_name=None, verify_certificate_spki=None, verify_certificate_hash=None, min_protocol_version=None, max_protocol_version=None, cipher_suites=None):  # noqa: E501
        """IstioNetworkingV1alpha3ServerTLSOptions - a model defined in OpenAPI"""  # noqa: E501

        self._mode = None
        self._private_key = None
        self._ca_certificates = None
        self._subject_alt_names = None
        self._https_redirect = None
        self._server_certificate = None
        self._credential_name = None
        self._verify_certificate_spki = None
        self._verify_certificate_hash = None
        self._min_protocol_version = None
        self._max_protocol_version = None
        self._cipher_suites = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if private_key is not None:
            self.private_key = private_key
        if ca_certificates is not None:
            self.ca_certificates = ca_certificates
        if subject_alt_names is not None:
            self.subject_alt_names = subject_alt_names
        if https_redirect is not None:
            self.https_redirect = https_redirect
        if server_certificate is not None:
            self.server_certificate = server_certificate
        if credential_name is not None:
            self.credential_name = credential_name
        if verify_certificate_spki is not None:
            self.verify_certificate_spki = verify_certificate_spki
        if verify_certificate_hash is not None:
            self.verify_certificate_hash = verify_certificate_hash
        if min_protocol_version is not None:
            self.min_protocol_version = min_protocol_version
        if max_protocol_version is not None:
            self.max_protocol_version = max_protocol_version
        if cipher_suites is not None:
            self.cipher_suites = cipher_suites

    @property
    def mode(self):
        """Gets the mode of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501

        TLS modes enforced by the proxy  # noqa: E501

        :return: The mode of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this IstioNetworkingV1alpha3ServerTLSOptions.

        TLS modes enforced by the proxy  # noqa: E501

        :param mode: The mode of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["PASSTHROUGH", "SIMPLE", "MUTUAL", "AUTO_PASSTHROUGH", "ISTIO_MUTUAL"]  # noqa: E501
        if mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"  # noqa: E501
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def private_key(self):
        """Gets the private_key of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501

        REQUIRED if mode is `SIMPLE` or `MUTUAL`. The path to the file holding the server's private key.  # noqa: E501

        :return: The private_key of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this IstioNetworkingV1alpha3ServerTLSOptions.

        REQUIRED if mode is `SIMPLE` or `MUTUAL`. The path to the file holding the server's private key.  # noqa: E501

        :param private_key: The private_key of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :type: str
        """

        self._private_key = private_key

    @property
    def ca_certificates(self):
        """Gets the ca_certificates of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501

        REQUIRED if mode is `MUTUAL`. The path to a file containing certificate authority certificates to use in verifying a presented client side certificate.  # noqa: E501

        :return: The ca_certificates of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :rtype: str
        """
        return self._ca_certificates

    @ca_certificates.setter
    def ca_certificates(self, ca_certificates):
        """Sets the ca_certificates of this IstioNetworkingV1alpha3ServerTLSOptions.

        REQUIRED if mode is `MUTUAL`. The path to a file containing certificate authority certificates to use in verifying a presented client side certificate.  # noqa: E501

        :param ca_certificates: The ca_certificates of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :type: str
        """

        self._ca_certificates = ca_certificates

    @property
    def subject_alt_names(self):
        """Gets the subject_alt_names of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501

        A list of alternate names to verify the subject identity in the certificate presented by the client.  # noqa: E501

        :return: The subject_alt_names of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._subject_alt_names

    @subject_alt_names.setter
    def subject_alt_names(self, subject_alt_names):
        """Sets the subject_alt_names of this IstioNetworkingV1alpha3ServerTLSOptions.

        A list of alternate names to verify the subject identity in the certificate presented by the client.  # noqa: E501

        :param subject_alt_names: The subject_alt_names of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :type: list[str]
        """

        self._subject_alt_names = subject_alt_names

    @property
    def https_redirect(self):
        """Gets the https_redirect of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501

        If set to true, the load balancer will send a 301 redirect for all http connections, asking the clients to use HTTPS.  # noqa: E501

        :return: The https_redirect of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :rtype: bool
        """
        return self._https_redirect

    @https_redirect.setter
    def https_redirect(self, https_redirect):
        """Sets the https_redirect of this IstioNetworkingV1alpha3ServerTLSOptions.

        If set to true, the load balancer will send a 301 redirect for all http connections, asking the clients to use HTTPS.  # noqa: E501

        :param https_redirect: The https_redirect of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :type: bool
        """

        self._https_redirect = https_redirect

    @property
    def server_certificate(self):
        """Gets the server_certificate of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501

        REQUIRED if mode is `SIMPLE` or `MUTUAL`. The path to the file holding the server-side TLS certificate to use.  # noqa: E501

        :return: The server_certificate of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :rtype: str
        """
        return self._server_certificate

    @server_certificate.setter
    def server_certificate(self, server_certificate):
        """Sets the server_certificate of this IstioNetworkingV1alpha3ServerTLSOptions.

        REQUIRED if mode is `SIMPLE` or `MUTUAL`. The path to the file holding the server-side TLS certificate to use.  # noqa: E501

        :param server_certificate: The server_certificate of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :type: str
        """

        self._server_certificate = server_certificate

    @property
    def credential_name(self):
        """Gets the credential_name of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501

        The credentialName stands for a unique identifier that can be used to identify the serverCertificate and the privateKey. The credentialName appended with suffix \"-cacert\" is used to identify the CaCertificates associated with this server. Gateway workloads capable of fetching credentials from a remote credential store such as Kubernetes secrets, will be configured to retrieve the serverCertificate and the privateKey using credentialName, instead of using the file system paths specified above. If using mutual TLS, gateway workload instances will retrieve the CaCertificates using credentialName-cacert. The semantics of the name are platform dependent. In Kubernetes, the default Istio supplied credential server expects the credentialName to match the name of the Kubernetes secret that holds the server certificate, the private key, and the CA certificate (if using mutual TLS). Set the `ISTIO_META_USER_SDS` metadata variable in the gateway's proxy to enable the dynamic credential fetching feature.  # noqa: E501

        :return: The credential_name of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :rtype: str
        """
        return self._credential_name

    @credential_name.setter
    def credential_name(self, credential_name):
        """Sets the credential_name of this IstioNetworkingV1alpha3ServerTLSOptions.

        The credentialName stands for a unique identifier that can be used to identify the serverCertificate and the privateKey. The credentialName appended with suffix \"-cacert\" is used to identify the CaCertificates associated with this server. Gateway workloads capable of fetching credentials from a remote credential store such as Kubernetes secrets, will be configured to retrieve the serverCertificate and the privateKey using credentialName, instead of using the file system paths specified above. If using mutual TLS, gateway workload instances will retrieve the CaCertificates using credentialName-cacert. The semantics of the name are platform dependent. In Kubernetes, the default Istio supplied credential server expects the credentialName to match the name of the Kubernetes secret that holds the server certificate, the private key, and the CA certificate (if using mutual TLS). Set the `ISTIO_META_USER_SDS` metadata variable in the gateway's proxy to enable the dynamic credential fetching feature.  # noqa: E501

        :param credential_name: The credential_name of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :type: str
        """

        self._credential_name = credential_name

    @property
    def verify_certificate_spki(self):
        """Gets the verify_certificate_spki of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501

        An optional list of base64-encoded SHA-256 hashes of the SKPIs of authorized client certificates. Note: When both verify_certificate_hash and verify_certificate_spki are specified, a hash matching either value will result in the certificate being accepted.  # noqa: E501

        :return: The verify_certificate_spki of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._verify_certificate_spki

    @verify_certificate_spki.setter
    def verify_certificate_spki(self, verify_certificate_spki):
        """Sets the verify_certificate_spki of this IstioNetworkingV1alpha3ServerTLSOptions.

        An optional list of base64-encoded SHA-256 hashes of the SKPIs of authorized client certificates. Note: When both verify_certificate_hash and verify_certificate_spki are specified, a hash matching either value will result in the certificate being accepted.  # noqa: E501

        :param verify_certificate_spki: The verify_certificate_spki of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :type: list[str]
        """

        self._verify_certificate_spki = verify_certificate_spki

    @property
    def verify_certificate_hash(self):
        """Gets the verify_certificate_hash of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501

        An optional list of hex-encoded SHA-256 hashes of the authorized client certificates. Both simple and colon separated formats are acceptable. Note: When both verify_certificate_hash and verify_certificate_spki are specified, a hash matching either value will result in the certificate being accepted.  # noqa: E501

        :return: The verify_certificate_hash of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._verify_certificate_hash

    @verify_certificate_hash.setter
    def verify_certificate_hash(self, verify_certificate_hash):
        """Sets the verify_certificate_hash of this IstioNetworkingV1alpha3ServerTLSOptions.

        An optional list of hex-encoded SHA-256 hashes of the authorized client certificates. Both simple and colon separated formats are acceptable. Note: When both verify_certificate_hash and verify_certificate_spki are specified, a hash matching either value will result in the certificate being accepted.  # noqa: E501

        :param verify_certificate_hash: The verify_certificate_hash of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :type: list[str]
        """

        self._verify_certificate_hash = verify_certificate_hash

    @property
    def min_protocol_version(self):
        """Gets the min_protocol_version of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501

        TLS protocol versions.  # noqa: E501

        :return: The min_protocol_version of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :rtype: str
        """
        return self._min_protocol_version

    @min_protocol_version.setter
    def min_protocol_version(self, min_protocol_version):
        """Sets the min_protocol_version of this IstioNetworkingV1alpha3ServerTLSOptions.

        TLS protocol versions.  # noqa: E501

        :param min_protocol_version: The min_protocol_version of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["TLS_AUTO", "TLSV1_0", "TLSV1_1", "TLSV1_2", "TLSV1_3"]  # noqa: E501
        if min_protocol_version not in allowed_values:
            raise ValueError(
                "Invalid value for `min_protocol_version` ({0}), must be one of {1}"  # noqa: E501
                .format(min_protocol_version, allowed_values)
            )

        self._min_protocol_version = min_protocol_version

    @property
    def max_protocol_version(self):
        """Gets the max_protocol_version of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501

        TLS protocol versions.  # noqa: E501

        :return: The max_protocol_version of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :rtype: str
        """
        return self._max_protocol_version

    @max_protocol_version.setter
    def max_protocol_version(self, max_protocol_version):
        """Sets the max_protocol_version of this IstioNetworkingV1alpha3ServerTLSOptions.

        TLS protocol versions.  # noqa: E501

        :param max_protocol_version: The max_protocol_version of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["TLS_AUTO", "TLSV1_0", "TLSV1_1", "TLSV1_2", "TLSV1_3"]  # noqa: E501
        if max_protocol_version not in allowed_values:
            raise ValueError(
                "Invalid value for `max_protocol_version` ({0}), must be one of {1}"  # noqa: E501
                .format(max_protocol_version, allowed_values)
            )

        self._max_protocol_version = max_protocol_version

    @property
    def cipher_suites(self):
        """Gets the cipher_suites of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501

        Optional: If specified, only support the specified cipher list. Otherwise default to the default cipher list supported by Envoy.  # noqa: E501

        :return: The cipher_suites of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._cipher_suites

    @cipher_suites.setter
    def cipher_suites(self, cipher_suites):
        """Sets the cipher_suites of this IstioNetworkingV1alpha3ServerTLSOptions.

        Optional: If specified, only support the specified cipher list. Otherwise default to the default cipher list supported by Envoy.  # noqa: E501

        :param cipher_suites: The cipher_suites of this IstioNetworkingV1alpha3ServerTLSOptions.  # noqa: E501
        :type: list[str]
        """

        self._cipher_suites = cipher_suites

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
        if not isinstance(other, IstioNetworkingV1alpha3ServerTLSOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
