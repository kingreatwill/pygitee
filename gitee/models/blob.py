# coding: utf-8


import pprint
import re  # noqa: F401

import six


class Blob(object):
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
        'sha': 'str',
        'size': 'str',
        'url': 'str',
        'content': 'str',
        'encoding': 'str'
    }

    attribute_map = {
        'sha': 'sha',
        'size': 'size',
        'url': 'url',
        'content': 'content',
        'encoding': 'encoding'
    }

    def __init__(self, sha=None, size=None, url=None, content=None, encoding=None):  # noqa: E501
        """Blob - a model defined in Swagger"""  # noqa: E501
        self._sha = None
        self._size = None
        self._url = None
        self._content = None
        self._encoding = None
        self.discriminator = None
        if sha is not None:
            self.sha = sha
        if size is not None:
            self.size = size
        if url is not None:
            self.url = url
        if content is not None:
            self.content = content
        if encoding is not None:
            self.encoding = encoding

    @property
    def sha(self):
        """Gets the sha of this Blob.  # noqa: E501


        :return: The sha of this Blob.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this Blob.


        :param sha: The sha of this Blob.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def size(self):
        """Gets the size of this Blob.  # noqa: E501


        :return: The size of this Blob.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Blob.


        :param size: The size of this Blob.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def url(self):
        """Gets the url of this Blob.  # noqa: E501


        :return: The url of this Blob.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Blob.


        :param url: The url of this Blob.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def content(self):
        """Gets the content of this Blob.  # noqa: E501


        :return: The content of this Blob.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Blob.


        :param content: The content of this Blob.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def encoding(self):
        """Gets the encoding of this Blob.  # noqa: E501


        :return: The encoding of this Blob.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this Blob.


        :param encoding: The encoding of this Blob.  # noqa: E501
        :type: str
        """

        self._encoding = encoding

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
        if issubclass(Blob, dict):
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
        if not isinstance(other, Blob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other