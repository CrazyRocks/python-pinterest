#!/usr/bin/env python

from pinterest import json, PinterestError


class Domain(object):
    """ A class representing a Domain structure used by the pinterest API

    The Domain structure exposes the following properties:
      domain.id
      domain.name
      domain.type
      domain.favicon
      domain.thumbnails
      domain.access
      domain.client_details
    """

    def __init__(self, **kwargs):
        """ Domain initializer
        :param kwargs: Keyword arguments
        """
        param_defaults = {
            'id': None,
            'name': None,
            'type': 'domain',
            'favicon': None,
            'thumbnails': [],
            'access': [],
            'client_details': {}}

        # Override defaults
        for (param, default) in param_defaults.iteritems():
            setattr(self, param, kwargs.get(param, default))

    @property
    def id(self):
        """ Gets the unique ID of the Domain
        :return: The unique ID of the Domain
        """
        return self._id

    @id.setter
    def id(self, value):
        """ Sets the unique ID of the Domain
        :param value: The unique ID of the Domain
        """
        self._id = value

    @property
    def name(self):
        """ Gets the Domain's name
        :return: The Domain's name
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Sets the Domain's name
        :param value: The Domain's name
        """
        self._name = value

    @property
    def type(self):
        """ Gets the Domain's type (only known type: domain)
        :return: The Domain's type
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Sets the Domain's type (only known type: domain)
        :param value: The Domain's type
        """
        self._type = value

    @property
    def favicon(self):
        """ Gets the Domain's favicon
        :return: The Domain's favicon
        """
        return self._favicon

    @favicon.setter
    def favicon(self, value):
        """ Sets the Domain's favicon
        :param value: The Domain's favicon
        """
        self._favicon = value

    @property
    def thumbnails(self):
        """ Gets the Domain's thumbnails
        :return: The Domain's thumbnails
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, value):
        """ Sets the Domain's thumbnails
        :param value: The Domain's thumbnails
        """
        self._thumbnails = value

    @property
    def access(self):
        """ Gets the Domain's access
        :return: The Domain's access
        """
        return self._access

    @access.setter
    def access(self, value):
        """ Sets the Domain's access
        :param value: The Domain's access
        """
        self._access = value

    @property
    def client_details(self):
        """ Gets the Domain's client details
        :return: The Domain's client details
        """
        return self._client_details

    @client_details.setter
    def client_details(self, value):
        """ Sets the Domain's client details
        :param value: The Domain's client details
        """
        self._client_details = value

    def __ne__(self, other):
        """ Checks if a Domain is not equal to another Domain
        :param other: Other Domain to compare to
        :return: True if Domains are not equal, False otherwise
        """
        return not self.__eq__(other)

    def __eq__(self, other):
        """ Checks if a Domain is equal to another Domain
        :param other: Other Domain to compare to
        :return: True if Domains are equal, False otherwise
        """
        try:
            return other and \
                   self.id == other.id

        except AttributeError:
            return False

    def __str__(self):
        """ A string representation of this pinterest.Domain instance
        The return value is the same as the JSON string representation
        :return: A string representation of this pinterest.Domain instance
        """
        return self.asJsonString()

    def asJsonString(self):
        """ A JSON string representation of this pinterest.Domain instance
        :return: A JSON string representation of this pinterest.Domain instance
        """
        return json.dumps(self.asDict(), sort_keys=True)

    def asDict(self):
        """ A dict representation of this pinterest.Domain instance
        The return value uses the same key names as the JSON representation
        :return: A dict representing this pinterest.Domain instance
        """
        data = {}
        if self.id:
            data['id'] = self.id
        if self.name:
            data['name'] = self.name
        if self.type:
            data['type'] = self.type
        if self.favicon:
            data['favicon'] = self.favicon
        if self.thumbnails:
            data['thumbnails'] = self.thumbnails
        if self.access:
            data['access'] = self.access
        if self.client_details:
            data['client_details'] = self.client_details
        return data

    @staticmethod
    def newFromJsonDict(data):
        """ Create a new instance based on a JSON dict
        :param data:  A JSON dict, as converted from the JSON in the pinterest API
        :return: A pinterest.Domain instance
        """
        return Domain(id=data.get('id', None),
                      name=data.get('name', None),
                      type=data.get('type', 'domain'),
                      favicon=data.get('favicon', None),
                      thumbnails=data.get('thumbnails', []),
                      access=data.get('access', []),
                      client_details=data.get('client_details', {}))