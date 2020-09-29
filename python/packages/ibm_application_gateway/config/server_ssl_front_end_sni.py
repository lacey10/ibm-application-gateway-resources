# coding: utf-8

"""
    IBM Application Gateway Configuration Specification (OpenAPI)

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 20.09
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ServerSslFrontEndSni(object):
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
        'certificate': 'list[str]',
        'hostname': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'hostname': 'hostname'
    }

    def __init__(self, certificate=None, hostname=None):  # noqa: E501
        """ServerSslFrontEndSni - a model defined in OpenAPI"""  # noqa: E501

        self._certificate = None
        self._hostname = None
        self.discriminator = None

        if certificate is not None:
            self.certificate = certificate
        if hostname is not None:
            self.hostname = hostname

    @property
    def certificate(self):
        """Gets the certificate of this ServerSslFrontEndSni.  # noqa: E501

        PEM based personal certificate files which will be used  when communicating with clients which indicate this host. These certificate files should include the private key,  a certificate signed with the private key, and the  signer certificate or signer certificate chain  (if required).   # noqa: E501

        :return: The certificate of this ServerSslFrontEndSni.  # noqa: E501
        :rtype: list[str]
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this ServerSslFrontEndSni.

        PEM based personal certificate files which will be used  when communicating with clients which indicate this host. These certificate files should include the private key,  a certificate signed with the private key, and the  signer certificate or signer certificate chain  (if required).   # noqa: E501

        :param certificate: The certificate of this ServerSslFrontEndSni.  # noqa: E501
        :type: list[str]
        """

        self._certificate = certificate

    @property
    def hostname(self):
        """Gets the hostname of this ServerSslFrontEndSni.  # noqa: E501

        The name of the host for this SNI entry.   # noqa: E501

        :return: The hostname of this ServerSslFrontEndSni.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ServerSslFrontEndSni.

        The name of the host for this SNI entry.   # noqa: E501

        :param hostname: The hostname of this ServerSslFrontEndSni.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

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
        if not isinstance(other, ServerSslFrontEndSni):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServerSslFrontEndSni):
            return True

        return self.to_dict() != other.to_dict()
