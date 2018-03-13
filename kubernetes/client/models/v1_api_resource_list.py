# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1APIResourceList(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'api_version': 'str',
        'group_version': 'str',
        'kind': 'str',
        'resources': 'list[V1APIResource]'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'group_version': 'groupVersion',
        'kind': 'kind',
        'resources': 'resources'
    }

    def __init__(self, api_version=None, group_version=None, kind=None, resources=None):
        """
        V1APIResourceList - a model defined in Swagger
        """

        self._api_version = None
        self._group_version = None
        self._kind = None
        self._resources = None
        self.discriminator = None

        if api_version is not None:
          self.api_version = api_version
        self.group_version = group_version
        if kind is not None:
          self.kind = kind
        self.resources = resources

    @property
    def api_version(self):
        """
        Gets the api_version of this V1APIResourceList.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :return: The api_version of this V1APIResourceList.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1APIResourceList.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1APIResourceList.
        :type: str
        """

        self._api_version = api_version

    @property
    def group_version(self):
        """
        Gets the group_version of this V1APIResourceList.
        groupVersion is the group and version this APIResourceList is for.

        :return: The group_version of this V1APIResourceList.
        :rtype: str
        """
        return self._group_version

    @group_version.setter
    def group_version(self, group_version):
        """
        Sets the group_version of this V1APIResourceList.
        groupVersion is the group and version this APIResourceList is for.

        :param group_version: The group_version of this V1APIResourceList.
        :type: str
        """
        if group_version is None:
            raise ValueError("Invalid value for `group_version`, must not be `None`")

        self._group_version = group_version

    @property
    def kind(self):
        """
        Gets the kind of this V1APIResourceList.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :return: The kind of this V1APIResourceList.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1APIResourceList.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1APIResourceList.
        :type: str
        """

        self._kind = kind

    @property
    def resources(self):
        """
        Gets the resources of this V1APIResourceList.
        resources contains the name of the resources and if they are namespaced.

        :return: The resources of this V1APIResourceList.
        :rtype: list[V1APIResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this V1APIResourceList.
        resources contains the name of the resources and if they are namespaced.

        :param resources: The resources of this V1APIResourceList.
        :type: list[V1APIResource]
        """
        if resources is None:
            raise ValueError("Invalid value for `resources`, must not be `None`")

        self._resources = resources

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1APIResourceList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
