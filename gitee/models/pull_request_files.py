# coding: utf-8


import pprint
import re  # noqa: F401

import six


class PullRequestFiles(object):
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
        'filename': 'str',
        'status': 'str',
        'additions': 'str',
        'deletions': 'str',
        'blob_url': 'str',
        'raw_url': 'str',
        'patch': 'str'
    }

    attribute_map = {
        'sha': 'sha',
        'filename': 'filename',
        'status': 'status',
        'additions': 'additions',
        'deletions': 'deletions',
        'blob_url': 'blob_url',
        'raw_url': 'raw_url',
        'patch': 'patch'
    }

    def __init__(self, sha=None, filename=None, status=None, additions=None, deletions=None, blob_url=None,
                 raw_url=None, patch=None):  # noqa: E501
        """PullRequestFiles - a model defined in Swagger"""  # noqa: E501
        self._sha = None
        self._filename = None
        self._status = None
        self._additions = None
        self._deletions = None
        self._blob_url = None
        self._raw_url = None
        self._patch = None
        self.discriminator = None
        if sha is not None:
            self.sha = sha
        if filename is not None:
            self.filename = filename
        if status is not None:
            self.status = status
        if additions is not None:
            self.additions = additions
        if deletions is not None:
            self.deletions = deletions
        if blob_url is not None:
            self.blob_url = blob_url
        if raw_url is not None:
            self.raw_url = raw_url
        if patch is not None:
            self.patch = patch

    @property
    def sha(self):
        """Gets the sha of this PullRequestFiles.  # noqa: E501


        :return: The sha of this PullRequestFiles.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this PullRequestFiles.


        :param sha: The sha of this PullRequestFiles.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def filename(self):
        """Gets the filename of this PullRequestFiles.  # noqa: E501


        :return: The filename of this PullRequestFiles.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this PullRequestFiles.


        :param filename: The filename of this PullRequestFiles.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def status(self):
        """Gets the status of this PullRequestFiles.  # noqa: E501


        :return: The status of this PullRequestFiles.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PullRequestFiles.


        :param status: The status of this PullRequestFiles.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def additions(self):
        """Gets the additions of this PullRequestFiles.  # noqa: E501


        :return: The additions of this PullRequestFiles.  # noqa: E501
        :rtype: str
        """
        return self._additions

    @additions.setter
    def additions(self, additions):
        """Sets the additions of this PullRequestFiles.


        :param additions: The additions of this PullRequestFiles.  # noqa: E501
        :type: str
        """

        self._additions = additions

    @property
    def deletions(self):
        """Gets the deletions of this PullRequestFiles.  # noqa: E501


        :return: The deletions of this PullRequestFiles.  # noqa: E501
        :rtype: str
        """
        return self._deletions

    @deletions.setter
    def deletions(self, deletions):
        """Sets the deletions of this PullRequestFiles.


        :param deletions: The deletions of this PullRequestFiles.  # noqa: E501
        :type: str
        """

        self._deletions = deletions

    @property
    def blob_url(self):
        """Gets the blob_url of this PullRequestFiles.  # noqa: E501


        :return: The blob_url of this PullRequestFiles.  # noqa: E501
        :rtype: str
        """
        return self._blob_url

    @blob_url.setter
    def blob_url(self, blob_url):
        """Sets the blob_url of this PullRequestFiles.


        :param blob_url: The blob_url of this PullRequestFiles.  # noqa: E501
        :type: str
        """

        self._blob_url = blob_url

    @property
    def raw_url(self):
        """Gets the raw_url of this PullRequestFiles.  # noqa: E501


        :return: The raw_url of this PullRequestFiles.  # noqa: E501
        :rtype: str
        """
        return self._raw_url

    @raw_url.setter
    def raw_url(self, raw_url):
        """Sets the raw_url of this PullRequestFiles.


        :param raw_url: The raw_url of this PullRequestFiles.  # noqa: E501
        :type: str
        """

        self._raw_url = raw_url

    @property
    def patch(self):
        """Gets the patch of this PullRequestFiles.  # noqa: E501


        :return: The patch of this PullRequestFiles.  # noqa: E501
        :rtype: str
        """
        return self._patch

    @patch.setter
    def patch(self, patch):
        """Sets the patch of this PullRequestFiles.


        :param patch: The patch of this PullRequestFiles.  # noqa: E501
        :type: str
        """

        self._patch = patch

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
        if issubclass(PullRequestFiles, dict):
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
        if not isinstance(other, PullRequestFiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other