#!/usr/bin/env python

from pinterest import json, PinterestError


class Comment(object):
    """ A class representing a pin Comment structure used by the pinterest API

    The pin Comment structure exposes the following properties:
      comment.id
      comment.text
      comment.type
      comment.created_at
    """

    def __init__(self, **kwargs):
        """ Comment initializer
        :param kwargs: Keyword arguments
        """
        param_defaults = {
            'id': None,
            'text': None,
            'type': 'comment',
            'created_at': None}

        # Override defaults
        for (param, default) in param_defaults.iteritems():
            setattr(self, param, kwargs.get(param, default))

    @property
    def id(self):
        """ Gets the unique ID of the pin Comment
        :return: The unique ID of the pin Comment
        """
        return self._id

    @id.setter
    def id(self, value):
        """ Sets the unique ID of the pin Comment
        :param value: The unique ID of the pin Comment
        """
        self._id = value

    @property
    def text(self):
        """ Gets the pin Comment's text
        :return: The pin Comment's text
        """
        return self._text

    @text.setter
    def text(self, value):
        """ Sets the pin Comment's text
        :param value: The pin Comment's text
        """
        self._text = value

    @property
    def type(self):
        """ Gets the pin Comment's type (only known type: comment)
        :return: The pin Comment's type
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Sets the pin Comment's type (only known type: comment)
        :param value: The pin Comment's type
        """
        self._type = value

    @property
    def created_at(self):
        """ Gets the date and time the pin Comment was created
        :return: The date and time the pin Comment was created
        """
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """ Sets the date and time the pin Comment was created
        :param value: The date and time the pin Comment was created
        """
        self._created_at = value

    def __ne__(self, other):
        """ Checks if a pin Comment is not equal to another pin Comment
        :param other: Other pin Comment to compare to
        :return: True if pin Comments are not equal, False otherwise
        """
        return not self.__eq__(other)

    def __eq__(self, other):
        """ Checks if a pin comment is equal to another pin Comment
        :param other: Other pin Comment to compare to
        :return: True if pin Comments are equal, False otherwise
        """
        try:
            return other and \
                   self.id == other.id

        except AttributeError:
            return False

    def __str__(self):
        """ A string representation of this pinterest.Comment instance
        The return value is the same as the JSON string representation
        :return: A string representation of this pinterest.Comment instance
        """
        return self.asJsonString()

    def asJsonString(self):
        """ A JSON string representation of this pinterest.Comment instance
        :return: A JSON string representation of this pinterest.Comment instance
        """
        return json.dumps(self.asDict(), sort_keys=True)

    def asDict(self):
        """ A dict representation of this pinterest.Comment instance
        The return value uses the same key names as the JSON representation
        :return: A dict representing this pinterest.Comment instance
        """
        data = {}
        if self.id:
            data['id'] = self.id
        if self.text:
            data['text'] = self.text
        if self.type:
            data['type'] = self.type
        if self.created_at:
            data['created_at'] = self.created_at
        return data

    @staticmethod
    def newFromJsonDict(data):
        """ Create a new instance based on a JSON dict
        :param data:  A JSON dict, as converted from the JSON in the pinterest API
        :return: A pinterest.Comment instance
        """
        return Comment(id=data.get('id', None),
                       text=data.get('text', None),
                       type=data.get('type', 'comment'),
                       created_at=data.get('created_at', None))