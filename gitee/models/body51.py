# coding: utf-8


import pprint
import re  # noqa: F401

import six


class Body51(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'access_token': 'str',
        'files': 'object',
        'description': 'str',
        'public': 'bool'
    }

    attribute_map = {
        'access_token': 'access_token',
        'files': 'files',
        'description': 'description',
        'public': 'public'
    }

    def __init__(self, access_token=None, files=None, description=None, public=None):  # noqa: E501
        """Body51 - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._files = None
        self._description = None
        self._public = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        self.files = files
        self.description = description
        if public is not None:
            self.public = public

    @property
    def access_token(self):
        """Gets the access_token of this Body51.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this Body51.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this Body51.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this Body51.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def files(self):
        """Gets the files of this Body51.  # noqa: E501

        Hash形式的代码片段文件名以及文件内容。如: { \"file1.txt\": { \"content\": \"String file contents\" } }  # noqa: E501

        :return: The files of this Body51.  # noqa: E501
        :rtype: object
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Body51.

        Hash形式的代码片段文件名以及文件内容。如: { \"file1.txt\": { \"content\": \"String file contents\" } }  # noqa: E501

        :param files: The files of this Body51.  # noqa: E501
        :type: object
        """
        if files is None:
            raise ValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = files

    @property
    def description(self):
        """Gets the description of this Body51.  # noqa: E501

        代码片段描述，1~30个字符  # noqa: E501

        :return: The description of this Body51.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Body51.

        代码片段描述，1~30个字符  # noqa: E501

        :param description: The description of this Body51.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def public(self):
        """Gets the public of this Body51.  # noqa: E501

        公开/私有，默认: 私有  # noqa: E501

        :return: The public of this Body51.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this Body51.

        公开/私有，默认: 私有  # noqa: E501

        :param public: The public of this Body51.  # noqa: E501
        :type: bool
        """

        self._public = public

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Body51, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Body51):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
