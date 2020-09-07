# coding: utf-8


import pprint
import re  # noqa: F401

import six


class UserNotificationSubject(object):
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
        'title': 'str',
        'url': 'str',
        'latest_comment_url': 'str',
        'type': 'str'
    }

    attribute_map = {
        'title': 'title',
        'url': 'url',
        'latest_comment_url': 'latest_comment_url',
        'type': 'type'
    }

    def __init__(self, title=None, url=None, latest_comment_url=None, type=None):  # noqa: E501
        """UserNotificationSubject - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._url = None
        self._latest_comment_url = None
        self._type = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if url is not None:
            self.url = url
        if latest_comment_url is not None:
            self.latest_comment_url = latest_comment_url
        if type is not None:
            self.type = type

    @property
    def title(self):
        """Gets the title of this UserNotificationSubject.  # noqa: E501


        :return: The title of this UserNotificationSubject.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UserNotificationSubject.


        :param title: The title of this UserNotificationSubject.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def url(self):
        """Gets the url of this UserNotificationSubject.  # noqa: E501


        :return: The url of this UserNotificationSubject.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UserNotificationSubject.


        :param url: The url of this UserNotificationSubject.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def latest_comment_url(self):
        """Gets the latest_comment_url of this UserNotificationSubject.  # noqa: E501


        :return: The latest_comment_url of this UserNotificationSubject.  # noqa: E501
        :rtype: str
        """
        return self._latest_comment_url

    @latest_comment_url.setter
    def latest_comment_url(self, latest_comment_url):
        """Sets the latest_comment_url of this UserNotificationSubject.


        :param latest_comment_url: The latest_comment_url of this UserNotificationSubject.  # noqa: E501
        :type: str
        """

        self._latest_comment_url = latest_comment_url

    @property
    def type(self):
        """Gets the type of this UserNotificationSubject.  # noqa: E501


        :return: The type of this UserNotificationSubject.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserNotificationSubject.


        :param type: The type of this UserNotificationSubject.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(UserNotificationSubject, dict):
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
        if not isinstance(other, UserNotificationSubject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
