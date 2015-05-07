#!/usr/bin/env python

import json


class Board(object):
    """ A class representing a Board structure used by the pinterest API

    The Board structure exposes the following properties:
      Board.id
      Board.name
      Board.url
      Board.layout
      Board.category
      Board.type
      Board.image_thumbnail_url
      Board.is_collaborative
      Board.collaborated_by_me
      Board.followed_by_me
      Board.created_at
    """

    def __init__(self, **kwargs):
        """ Board initializer
        :param kwargs: Keyword arguments
        """
        param_defaults = {
            'id': None,
            'name': None,
            'url': None,
            'layout': None,
            'category': None,
            'type': 'board',
            'image_thumbnail_url': None,
            'is_collaborative': False,
            'collaborated_by_me': False,
            'followed_by_me': False,
            'created_at': None}

        # Override defaults
        for (param, default) in param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    @property
    def id(self):
        """ Gets the unique ID of the Board
        :return: The unique ID of the Board
        """
        return self._id

    @id.setter
    def id(self, value):
        """ Sets the unique ID of the Board
        :param value: The unique ID of the Board
        """
        self._id = value

    @property
    def name(self):
        """ Gets the Board's name
        :return: The Board's name
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Sets the Board's name
        :param value: The Board's name
        """
        self._name = value

    @property
    def url(self):
        """ Gets the Board's URL
        :return: The Board's URL
        """
        return self._url

    @url.setter
    def url(self, value):
        """ Sets the Board's URL
        :param value: The Board's URL
        """
        self._url = value

    @property
    def layout(self):
        """ Gets the Board's layout
        :return: The Board's layout
        """
        return self._layout

    @layout.setter
    def layout(self, value):
        """ Sets the Board's layout
        :param value: The Board's layout
        """
        self._layout = value

    @property
    def category(self):
        """ Gets the Board's category
        :return: The Board's category
        """
        return self._category

    @category.setter
    def category(self, value):
        """ Sets the Board's category
        :param value: The Board's category
        """
        self._category = value

    @property
    def type(self):
        """ Gets the Board's type
        :return: The Board's type
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Sets the Board's type
        :param value: The Board's type
        """
        self._type = value

    @property
    def image_thumbnail_url(self):
        """ Gets the Board's image thumbnail URL
        :return: The Board's image thumbnail URL
        """
        return self._image_thumbnail_url

    @image_thumbnail_url.setter
    def image_thumbnail_url(self, value):
        """ Sets the Board's image thumbnail URL
        :param value: The Board's image thumbnail URL
        """
        self._image_thumbnail_url = value

    @property
    def is_collaborative(self):
        """ Returns whether the Board is collaborative
        :return: True if the Board is collaborative, False otherwise
        """
        return self._is_collaborative

    @is_collaborative.setter
    def is_collaborative(self, value):
        """ Sets whether the Board is collaborative
        :param value: True if the Board is collaborative, False otherwise
        """
        self._is_collaborative = value

    @property
    def collaborated_by_me(self):
        """ Returns whether the Board is collaborated on by me
        :return: True if the Board is collaborated on by me, False otherwise
        """
        return self._collaborated_by_me

    @collaborated_by_me.setter
    def collaborated_by_me(self, value):
        """ Sets whether the Board is collaborated on by me
        :param value: True if the Board is collaborated on by me, False otherwise
        """
        self._collaborated_by_me = value

    @property
    def followed_by_me(self):
        """ Returns whether the Board is followed by me
        :return: True if the Board is followed by me, False otherwise
        """
        return self._followed_by_me

    @followed_by_me.setter
    def followed_by_me(self, value):
        """ Sets whether the Board is followed by me
        :param value: True if the Board is followed by me, False otherwise
        """
        self._followed_by_me = value

    @property
    def created_at(self):
        """ Gets the date and time the Board was created
        :return: The date and time the Board was created
        """
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """ Sets the date and time the Board was created
        :param value: The date and time the Board was created
        """
        self._created_at = value

    def __ne__(self, other):
        """ Checks if a Board is not equal to another Board
        :param other: Other Board to compare to
        :return: True if Boards are not equal, False otherwise
        """
        return not self.__eq__(other)

    def __eq__(self, other):
        """ Checks if a Board is equal to another Board
        :param other: Other Board to compare to
        :return: True if Boards are equal, False otherwise
        """
        try:
            return other and \
                   self.id == other.id

        except AttributeError:
            return False

    def __str__(self):
        """ A string representation of this pinterest.Board instance
        The return value is the same as the JSON string representation
        :return: A string representation of this pinterest.Board instance
        """
        return self.asJsonString()

    def asJsonString(self):
        """ A JSON string representation of this pinterest.Board instance
        :return: A JSON string representation of this pinterest.Board instance
        """
        return json.dumps(self.asDict(), sort_keys=True)

    def asDict(self):
        """ A dict representation of this pinterest.Board instance
        The return value uses the same key names as the JSON representation
        :return: A dict representing this pinterest.Board instance
        """
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'layout': self.layout,
            'category': self.category,
            'type': self.type,
            'image_thumbnail_url': self.image_thumbnail_url,
            'is_collaborative': self.is_collaborative,
            'collaborated_by_me': self.collaborated_by_me,
            'followed_by_me': self.followed_by_me,
            'created_at': self.created_at
        }

    @staticmethod
    def newFromJsonDict(data):
        """ Create a new instance based on a JSON dict
        :param data:  A JSON dict, as converted from the JSON in the pinterest API
        :return: A pinterest.Board instance
        """
        return Board(id=data.get('id', None),
                     name=data.get('name', None),
                     url=data.get('url', None),
                     layout=data.get('layout', None),
                     category=data.get('category', None),
                     type=data.get('type', 'board'),
                     image_thumbnail_url=data.get('image_thumbnail_url', None),
                     is_collaborative=data.get('is_collaborative', False),
                     collaborated_by_me=data.get('collaborated_by_me', False),
                     followed_by_me=data.get('followed_by_me', False),
                     created_at=data.get('created_at', None))