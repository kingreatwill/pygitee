# coding: utf-8


import pprint
import re  # noqa: F401

import six


class Body21(object):
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
        'refs': 'str',
        'tag_name': 'str',
        'tag_message': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'refs': 'refs',
        'tag_name': 'tag_name',
        'tag_message': 'tag_message'
    }

    def __init__(self, access_token=None, refs='master', tag_name=None, tag_message=None):  # noqa: E501
        """Body21 - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._refs = None
        self._tag_name = None
        self._tag_message = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        self.refs = refs
        self.tag_name = tag_name
        if tag_message is not None:
            self.tag_message = tag_message

    @property
    def access_token(self):
        """Gets the access_token of this Body21.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this Body21.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this Body21.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this Body21.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def refs(self):
        """Gets the refs of this Body21.  # noqa: E501

        起点名称, 默认：master  # noqa: E501

        :return: The refs of this Body21.  # noqa: E501
        :rtype: str
        """
        return self._refs

    @refs.setter
    def refs(self, refs):
        """Sets the refs of this Body21.

        起点名称, 默认：master  # noqa: E501

        :param refs: The refs of this Body21.  # noqa: E501
        :type: str
        """
        if refs is None:
            raise ValueError("Invalid value for `refs`, must not be `None`")  # noqa: E501

        self._refs = refs

    @property
    def tag_name(self):
        """Gets the tag_name of this Body21.  # noqa: E501

        新创建的标签名称  # noqa: E501

        :return: The tag_name of this Body21.  # noqa: E501
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this Body21.

        新创建的标签名称  # noqa: E501

        :param tag_name: The tag_name of this Body21.  # noqa: E501
        :type: str
        """
        if tag_name is None:
            raise ValueError("Invalid value for `tag_name`, must not be `None`")  # noqa: E501

        self._tag_name = tag_name

    @property
    def tag_message(self):
        """Gets the tag_message of this Body21.  # noqa: E501

        Tag 描述, 默认为空  # noqa: E501

        :return: The tag_message of this Body21.  # noqa: E501
        :rtype: str
        """
        return self._tag_message

    @tag_message.setter
    def tag_message(self, tag_message):
        """Sets the tag_message of this Body21.

        Tag 描述, 默认为空  # noqa: E501

        :param tag_message: The tag_message of this Body21.  # noqa: E501
        :type: str
        """

        self._tag_message = tag_message

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
        if issubclass(Body21, dict):
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
        if not isinstance(other, Body21):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
