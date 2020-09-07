# coding: utf-8


import pprint
import re  # noqa: F401

import six


class Contributor(object):
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
        'email': 'str',
        'name': 'str',
        'contributions': 'str'
    }

    attribute_map = {
        'email': 'email',
        'name': 'name',
        'contributions': 'contributions'
    }

    def __init__(self, email=None, name=None, contributions=None):  # noqa: E501
        """Contributor - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._name = None
        self._contributions = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if name is not None:
            self.name = name
        if contributions is not None:
            self.contributions = contributions

    @property
    def email(self):
        """Gets the email of this Contributor.  # noqa: E501


        :return: The email of this Contributor.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Contributor.


        :param email: The email of this Contributor.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def name(self):
        """Gets the name of this Contributor.  # noqa: E501


        :return: The name of this Contributor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Contributor.


        :param name: The name of this Contributor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def contributions(self):
        """Gets the contributions of this Contributor.  # noqa: E501


        :return: The contributions of this Contributor.  # noqa: E501
        :rtype: str
        """
        return self._contributions

    @contributions.setter
    def contributions(self, contributions):
        """Sets the contributions of this Contributor.


        :param contributions: The contributions of this Contributor.  # noqa: E501
        :type: str
        """

        self._contributions = contributions

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
        if issubclass(Contributor, dict):
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
        if not isinstance(other, Contributor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
