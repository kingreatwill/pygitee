# coding: utf-8


import pprint
import re  # noqa: F401

import six


class SSHKey(object):
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
        'id': 'str',
        'key': 'str',
        'url': 'str',
        'title': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'key': 'key',
        'url': 'url',
        'title': 'title',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, key=None, url=None, title=None, created_at=None):  # noqa: E501
        """SSHKey - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._key = None
        self._url = None
        self._title = None
        self._created_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if url is not None:
            self.url = url
        if title is not None:
            self.title = title
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this SSHKey.  # noqa: E501


        :return: The id of this SSHKey.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SSHKey.


        :param id: The id of this SSHKey.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this SSHKey.  # noqa: E501


        :return: The key of this SSHKey.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SSHKey.


        :param key: The key of this SSHKey.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def url(self):
        """Gets the url of this SSHKey.  # noqa: E501


        :return: The url of this SSHKey.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SSHKey.


        :param url: The url of this SSHKey.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def title(self):
        """Gets the title of this SSHKey.  # noqa: E501


        :return: The title of this SSHKey.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SSHKey.


        :param title: The title of this SSHKey.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def created_at(self):
        """Gets the created_at of this SSHKey.  # noqa: E501


        :return: The created_at of this SSHKey.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SSHKey.


        :param created_at: The created_at of this SSHKey.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

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
        if issubclass(SSHKey, dict):
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
        if not isinstance(other, SSHKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other