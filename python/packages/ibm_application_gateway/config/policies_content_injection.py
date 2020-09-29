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

class PoliciesContentInjection(object):
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
        'name': 'str',
        'paths': 'list[str]',
        'full_line_match': 'bool',
        'location': 'str',
        'replace_match': 'bool',
        'content': 'str'
    }

    attribute_map = {
        'name': 'name',
        'paths': 'paths',
        'full_line_match': 'full_line_match',
        'location': 'location',
        'replace_match': 'replace_match',
        'content': 'content'
    }

    def __init__(self, name=None, paths=None, full_line_match=True, location=None, replace_match=False, content=None):  # noqa: E501
        """PoliciesContentInjection - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._paths = None
        self._full_line_match = None
        self._location = None
        self._replace_match = None
        self._content = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if paths is not None:
            self.paths = paths
        if full_line_match is not None:
            self.full_line_match = full_line_match
        if location is not None:
            self.location = location
        if replace_match is not None:
            self.replace_match = replace_match
        if content is not None:
            self.content = content

    @property
    def name(self):
        """Gets the name of this PoliciesContentInjection.  # noqa: E501

        A name to be associated with this content injection rule.   # noqa: E501

        :return: The name of this PoliciesContentInjection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PoliciesContentInjection.

        A name to be associated with this content injection rule.   # noqa: E501

        :param name: The name of this PoliciesContentInjection.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def paths(self):
        """Gets the paths of this PoliciesContentInjection.  # noqa: E501

        The path for which content injection will take place. This entry  is an array and can be used to specify multiple paths.   # noqa: E501

        :return: The paths of this PoliciesContentInjection.  # noqa: E501
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this PoliciesContentInjection.

        The path for which content injection will take place. This entry  is an array and can be used to specify multiple paths.   # noqa: E501

        :param paths: The paths of this PoliciesContentInjection.  # noqa: E501
        :type: list[str]
        """

        self._paths = paths

    @property
    def full_line_match(self):
        """Gets the full_line_match of this PoliciesContentInjection.  # noqa: E501

        Should the location match a full line, or should it match  any string in the response?  When a full line match is configured the content will be inserted prior to the matching line.  When a partial line match is configured the content will be inserted  immediately prior to the matching string.   # noqa: E501

        :return: The full_line_match of this PoliciesContentInjection.  # noqa: E501
        :rtype: bool
        """
        return self._full_line_match

    @full_line_match.setter
    def full_line_match(self, full_line_match):
        """Sets the full_line_match of this PoliciesContentInjection.

        Should the location match a full line, or should it match  any string in the response?  When a full line match is configured the content will be inserted prior to the matching line.  When a partial line match is configured the content will be inserted  immediately prior to the matching string.   # noqa: E501

        :param full_line_match: The full_line_match of this PoliciesContentInjection.  # noqa: E501
        :type: bool
        """

        self._full_line_match = full_line_match

    @property
    def location(self):
        """Gets the location of this PoliciesContentInjection.  # noqa: E501

        The location where the content should be injected. If a full line match is being used the location is pattern matched against  a line in the response using the '*.' wildcard characters.  The  maximum length of a line which can be matched is 8192 bytes.   # noqa: E501

        :return: The location of this PoliciesContentInjection.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this PoliciesContentInjection.

        The location where the content should be injected. If a full line match is being used the location is pattern matched against  a line in the response using the '*.' wildcard characters.  The  maximum length of a line which can be matched is 8192 bytes.   # noqa: E501

        :param location: The location of this PoliciesContentInjection.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def replace_match(self):
        """Gets the replace_match of this PoliciesContentInjection.  # noqa: E501

        If a partial line match is being used this configuration entry will control whether the matching string is replaced with the supplied content, or whether the supplied content is inserted prior to the matching string.  This configuration entry will be ignored if full line matches are being used.   # noqa: E501

        :return: The replace_match of this PoliciesContentInjection.  # noqa: E501
        :rtype: bool
        """
        return self._replace_match

    @replace_match.setter
    def replace_match(self, replace_match):
        """Sets the replace_match of this PoliciesContentInjection.

        If a partial line match is being used this configuration entry will control whether the matching string is replaced with the supplied content, or whether the supplied content is inserted prior to the matching string.  This configuration entry will be ignored if full line matches are being used.   # noqa: E501

        :param replace_match: The replace_match of this PoliciesContentInjection.  # noqa: E501
        :type: bool
        """

        self._replace_match = replace_match

    @property
    def content(self):
        """Gets the content of this PoliciesContentInjection.  # noqa: E501

        The data which is to be injected.   # noqa: E501

        :return: The content of this PoliciesContentInjection.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this PoliciesContentInjection.

        The data which is to be injected.   # noqa: E501

        :param content: The content of this PoliciesContentInjection.  # noqa: E501
        :type: str
        """

        self._content = content

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
        if not isinstance(other, PoliciesContentInjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PoliciesContentInjection):
            return True

        return self.to_dict() != other.to_dict()
