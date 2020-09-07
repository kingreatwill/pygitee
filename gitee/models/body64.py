# coding: utf-8


import pprint
import re  # noqa: F401

import six


class Body64(object):
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
        'year': 'int',
        'content': 'str',
        'week_index': 'int',
        'username': 'str',
        '_date': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'year': 'year',
        'content': 'content',
        'week_index': 'week_index',
        'username': 'username',
        '_date': 'date'
    }

    def __init__(self, access_token=None, year=None, content=None, week_index=None, username=None,
                 _date=None):  # noqa: E501
        """Body64 - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._year = None
        self._content = None
        self._week_index = None
        self._username = None
        self.__date = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        self.year = year
        self.content = content
        self.week_index = week_index
        self.username = username
        if _date is not None:
            self._date = _date

    @property
    def access_token(self):
        """Gets the access_token of this Body64.  # noqa: E501

        用户授权码  # noqa: E501

        :return: The access_token of this Body64.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this Body64.

        用户授权码  # noqa: E501

        :param access_token: The access_token of this Body64.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def year(self):
        """Gets the year of this Body64.  # noqa: E501

        周报所属年  # noqa: E501

        :return: The year of this Body64.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this Body64.

        周报所属年  # noqa: E501

        :param year: The year of this Body64.  # noqa: E501
        :type: int
        """
        if year is None:
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

    @property
    def content(self):
        """Gets the content of this Body64.  # noqa: E501

        周报内容  # noqa: E501

        :return: The content of this Body64.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Body64.

        周报内容  # noqa: E501

        :param content: The content of this Body64.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def week_index(self):
        """Gets the week_index of this Body64.  # noqa: E501

        周报所属周  # noqa: E501

        :return: The week_index of this Body64.  # noqa: E501
        :rtype: int
        """
        return self._week_index

    @week_index.setter
    def week_index(self, week_index):
        """Sets the week_index of this Body64.

        周报所属周  # noqa: E501

        :param week_index: The week_index of this Body64.  # noqa: E501
        :type: int
        """
        if week_index is None:
            raise ValueError("Invalid value for `week_index`, must not be `None`")  # noqa: E501

        self._week_index = week_index

    @property
    def username(self):
        """Gets the username of this Body64.  # noqa: E501

        用户名(username/login)  # noqa: E501

        :return: The username of this Body64.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Body64.

        用户名(username/login)  # noqa: E501

        :param username: The username of this Body64.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def _date(self):
        """Gets the _date of this Body64.  # noqa: E501

        周报日期(格式：2019-03-25)  # noqa: E501

        :return: The _date of this Body64.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Body64.

        周报日期(格式：2019-03-25)  # noqa: E501

        :param _date: The _date of this Body64.  # noqa: E501
        :type: str
        """

        self.__date = _date

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
        if issubclass(Body64, dict):
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
        if not isinstance(other, Body64):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
