# coding: utf-8


import pprint
import re  # noqa: F401

import six


class Body71(object):
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
        'username': 'str',
        'content': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'username': 'username',
        'content': 'content'
    }

    def __init__(self, access_token=None, username=None, content=None):  # noqa: E501
        """Body71 - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._username = None
        self._content = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        self.username = username
        self.content = content

    @property
    def access_token(self):
        """Gets the access_token of this Body71.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this Body71.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this Body71.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this Body71.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def username(self):
        """Gets the username of this Body71.  # noqa: E501

        用户名(username/login)  # noqa: E501

        :return: The username of this Body71.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Body71.

        用户名(username/login)  # noqa: E501

        :param username: The username of this Body71.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def content(self):
        """Gets the content of this Body71.  # noqa: E501

        私信内容  # noqa: E501

        :return: The content of this Body71.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Body71.

        私信内容  # noqa: E501

        :param content: The content of this Body71.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

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
        if issubclass(Body71, dict):
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
        if not isinstance(other, Body71):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
