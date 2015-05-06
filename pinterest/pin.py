#!/usr/bin/env python

from pinterest import json, PinterestError


class Pin(object):
    """ A class representing a Pin structure used by the pinterest API

    The Pin structure exposes the following properties:
      Pin.id
      Pin.cacheable_id
      Pin.title
      Pin.description
      Pin.type
      Pin.domain
      Pin.link
      Pin.like_count
      Pin.comment_count
      Pin.repin_count
      Pin.image_square_url
      Pin.image_square_size_pixels
      Pin.image_square_size_points
      Pin.image_medium_url
      Pin.image_medium_size_pixels
      Pin.image_medium_size_points
      Pin.image_large_url
      Pin.image_large_size_pixels
      Pin.image_large_size_points
      Pin.price_value
      Pin.price_currency
      Pin.attribution
      Pin.tracked_link
      Pin.promoter
      Pin.debug
      Pin.liked_by_me
      Pin.is_repin
      Pin.is_uploaded
      Pin.is_playable
      Pin.is_video
      Pin.created_at
    """

    def __init__(self, **kwargs):
        """ Pin initializer
        :param kwargs: Keyword arguments
        """
        param_defaults = {
            'id': None,
            'cacheable_id': None,
            'title': None,
            'description': None,
            'type': None,
            'domain': None,
            'link': None,
            'like_count': 0,
            'comment_count': 0,
            'repin_count': 0,
            'image_square_url': None,
            'image_square_size_pixels': {},
            'image_square_size_points': {},
            'image_medium_url': None,
            'image_medium_size_pixels': {},
            'image_medium_size_points': {},
            'image_large_url': None,
            'image_large_size_pixels': {},
            'image_large_size_points': {},
            'price_value': 0,
            'price_currency': None,
            'attribution': None,
            'tracked_link': None,
            'promoter': None,
            'debug': None,
            'liked_by_me': False,
            'is_repin': False,
            'is_uploaded': False,
            'is_playable': False,
            'is_video': False,
            'created_at': None}

        # Override defaults
        for (param, default) in param_defaults.iteritems():
            setattr(self, param, kwargs.get(param, default))

    @property
    def id(self):
        """ Gets the unique ID of the Pin
        :return: The unique ID of the Pin
        """
        return self._id

    @id.setter
    def id(self, value):
        """ Sets the unique ID of the Pin
        :param value: The unique ID of the Pin
        """
        self._id = value

    @property
    def cacheable_id(self):
        """ Gets the cacheable ID of the Pin
        :return: The cacheable ID of the Pin
        """
        return self._cacheable_id

    @cacheable_id.setter
    def cacheable_id(self, value):
        """ Sets the cacheable ID of the Pin
        :param value: The cacheable ID of the Pin
        """
        self._cacheable_id = value

    @property
    def title(self):
        """ Gets the Pin's title
        :return: The Pin's title
        """
        return self._title

    @title.setter
    def title(self, value):
        """ Sets the Pin's title
        :param value: The Pin's title
        """
        self._title = value

    @property
    def description(self):
        """ Gets the Pin's description
        :return: The Pin's description
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Sets the Pin's description
        :param value: The Pin's description
        """
        self._description = value

    @property
    def type(self):
        """ Gets the Pin's type
        :return: The Pin's type
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Sets the Pin's type
        :param value: The Pin's type
        """
        self._type = value

    @property
    def domain(self):
        """ Gets the Pin's domain
        :return: The Pin's domain
        """
        return self._domain

    @domain.setter
    def domain(self, value):
        """ Sets the Pin's domain
        :param value: The Pin's domain
        """
        self._domain = value

    @property
    def link(self):
        """ Gets the Pin's link
        :return: The Pin's link
        """
        return self._link

    @link.setter
    def link(self, value):
        """ Sets the Pin's link
        :param value: The Pin's link
        """
        self._link = value

    @property
    def like_count(self):
        """ Gets the Pin's like count
        :return: The Pin's like count
        """
        return self._like_count

    @like_count.setter
    def like_count(self, value):
        """ Sets the Pin's like count
        :param value: The Pin's like count
        """
        self._like_count = value

    @property
    def comment_count(self):
        """ Gets the Pin's comment count
        :return: The Pin's comment count
        """
        return self._comment_count

    @comment_count.setter
    def comment_count(self, value):
        """ Sets the Pin's comment count
        :param value: The Pin's comment count
        """
        self._comment_count = value

    @property
    def repin_count(self):
        """ Gets the Pin's repin count
        :return: The Pin's repin count
        """
        return self._repin_count

    @repin_count.setter
    def repin_count(self, value):
        """ Sets the Pin's repin count
        :param value: The Pin's repin count
        """
        self._repin_count = value

    @property
    def image_square_url(self):
        """ Gets the Pin's square image URL
        :return: The Pin's square image URL
        """
        return self._image_square_url

    @image_square_url.setter
    def image_square_url(self, value):
        """ Sets the Pin's square image URL
        :param value: The Pin's square image URL
        """
        self._image_square_url = value

    @property
    def image_square_size_pixels(self):
        """ Gets the Pin's square image size in pixels
        :return: The Pin's square image size in pixels
        """
        return self._image_square_size_pixels

    @image_square_size_pixels.setter
    def image_square_size_pixels(self, value):
        """ Sets the Pin's square image size in pixels
        :param value: The Pin's square image size in pixels
        """
        self._image_square_size_pixels = value

    @property
    def image_square_size_points(self):
        """ Gets the Pin's square image size in points
        :return: The Pin's square image size in points
        """
        return self._image_square_size_points

    @image_square_size_points.setter
    def image_square_size_points(self, value):
        """ Sets the Pin's square image size in points
        :param value: The Pin's square image size in points
        """
        self._image_square_size_points = value

    @property
    def image_medium_url(self):
        """ Gets the Pin's medium image URL
        :return: The Pin's medium image URL
        """
        return self._image_medium_url

    @image_medium_url.setter
    def image_medium_url(self, value):
        """ Sets the Pin's medium image URL
        :param value: The Pin's medium image URL
        """
        self._image_medium_url = value

    @property
    def image_medium_size_pixels(self):
        """ Gets the Pin's medium image size in pixels
        :return: The Pin's medium image size in pixels
        """
        return self._image_medium_size_pixels

    @image_medium_size_pixels.setter
    def image_medium_size_pixels(self, value):
        """ Sets the Pin's medium image size in pixels
        :param value: The Pin's medium image size in pixels
        """
        self._image_medium_size_pixels = value

    @property
    def image_medium_size_points(self):
        """ Gets the Pin's medium image size in points
        :return: The Pin's medium image size in points
        """
        return self._image_medium_size_points

    @image_medium_size_points.setter
    def image_medium_size_points(self, value):
        """ Sets the Pin's medium image size in points
        :param value: The Pin's medium image size in points
        """
        self._image_medium_size_points = value

    @property
    def image_large_url(self):
        """ Gets the Pin's large image URL
        :return: The Pin's large image URL
        """
        return self._image_large_url

    @image_large_url.setter
    def image_large_url(self, value):
        """ Sets the Pin's large image URL
        :param value: The Pin's large image URL
        """
        self._image_large_url = value

    @property
    def image_large_size_pixels(self):
        """ Gets the Pin's large image size in pixels
        :return: The Pin's large image size in pixels
        """
        return self._image_large_size_pixels

    @image_large_size_pixels.setter
    def image_large_size_pixels(self, value):
        """ Sets the Pin's large image size in pixels
        :param value: The Pin's large image size in pixels
        """
        self._image_large_size_pixels = value

    @property
    def image_large_size_points(self):
        """ Gets the Pin's large image size in points
        :return: The Pin's large image size in points
        """
        return self._image_large_size_points

    @image_large_size_points.setter
    def image_large_size_points(self, value):
        """ Sets the Pin's large image size in points
        :param value: The Pin's large image size in points
        """
        self._image_large_size_points = value

    @property
    def price_value(self):
        """ Gets the Pin's price value
        :return: The Pin's price value
        """
        return self._price_value

    @price_value.setter
    def price_value(self, value):
        """ Sets the Pin's price value
        :param value: The Pin's price value
        """
        self._price_value = value

    @property
    def price_currency(self):
        """ Gets the Pin's price currency
        :return: The Pin's price currency
        """
        return self._price_currency

    @price_currency.setter
    def price_currency(self, value):
        """ Sets the Pin's price currency
        :param value: The Pin's price currency
        """
        self._price_currency = value

    @property
    def price_currency(self):
        """ Gets the Pin's price currency
        :return: The Pin's price currency
        """
        return self._price_currency

    @price_currency.setter
    def price_currency(self, value):
        """ Sets the Pin's price currency
        :param value: The Pin's price currency
        """
        self._price_currency = value

    @property
    def attribution(self):
        """ Gets the Pin's attribution
        :return: The Pin's attribution
        """
        return self._attribution

    @attribution.setter
    def attribution(self, value):
        """ Sets the Pin's attribution
        :param value: The Pin's attribution
        """
        self._attribution = value

    @property
    def tracked_link(self):
        """ Gets the Pin's tracked link
        :return: The Pin's tracked link
        """
        return self._tracked_link

    @tracked_link.setter
    def tracked_link(self, value):
        """ Sets the Pin's tracked link
        :param value: The Pin's tracked link
        """
        self._tracked_link = value

    @property
    def promoter(self):
        """ Gets the Pin's promoter
        :return: The Pin's promoter
        """
        return self._promoter

    @promoter.setter
    def promoter(self, value):
        """ Sets the Pin's promoter
        :param value: The Pin's promoter
        """
        self._promoter = value

    @property
    def debug(self):
        """ Gets the Pin's debug status
        :return: The Pin's debug status
        """
        return self._debug

    @debug.setter
    def debug(self, value):
        """ Sets the Pin's debug status
        :param value: The Pin's debug status
        """
        self._debug = value

    @property
    def liked_by_me(self):
        """ Returns whether the Pin is liked by me
        :return: True if the Pin is liked by me, False otherwise
        """
        return self._liked_by_me

    @liked_by_me.setter
    def liked_by_me(self, value):
        """ Sets whether the Pin is liked by me
        :param value: True if the Pin is liked by me, False otherwise
        """
        self._liked_by_me = value

    @property
    def is_repin(self):
        """ Returns whether the Pin is a repin
        :return: True if the Pin is a repin, False otherwise
        """
        return self._is_repin

    @is_repin.setter
    def is_repin(self, value):
        """ Sets whether the Pin is a repin
        :param value: True if the Pin is a repin, False otherwise
        """
        self._is_repin = value

    @property
    def is_uploaded(self):
        """ Returns whether the Pin is uploaded
        :return: True if the Pin is uploaded, False otherwise
        """
        return self._is_uploaded

    @is_uploaded.setter
    def is_uploaded(self, value):
        """ Sets whether the Pin is uploaded
        :param value: True if the Pin is uploaded, False otherwise
        """
        self._is_uploaded = value

    @property
    def is_playable(self):
        """ Returns whether the Pin is playable
        :return: True if the Pin is playable, False otherwise
        """
        return self._is_playable

    @is_playable.setter
    def is_playable(self, value):
        """ Sets whether the Pin is playable
        :param value: True if the Pin is playable, False otherwise
        """
        self._is_playable = value

    @property
    def is_video(self):
        """ Returns whether the Pin is a video
        :return: True if the Pin is a video, False otherwise
        """
        return self._is_video

    @is_video.setter
    def is_video(self, value):
        """ Sets whether the Pin is a video
        :param value: True if the Pin is a video, False otherwise
        """
        self._is_video = value

    @property
    def created_at(self):
        """ Gets the date and time the Pin was created
        :return: The date and time the Pin was created
        """
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """ Sets the date and time the Pin was created
        :param value: The date and time the Pin was created
        """
        self._created_at = value

    def __ne__(self, other):
        """ Checks if a Pin is not equal to another Pin
        :param other: Other Pin to compare to
        :return: True if Pins are not equal, False otherwise
        """
        return not self.__eq__(other)

    def __eq__(self, other):
        """ Checks if a Pin is equal to another Pin
        :param other: Other Pin to compare to
        :return: True if Pins are equal, False otherwise
        """
        try:
            return other and \
                   self.id == other.id

        except AttributeError:
            return False

    def __str__(self):
        """ A string representation of this pinterest.Pin instance
        The return value is the same as the JSON string representation
        :return: A string representation of this pinterest.Pin instance
        """
        return self.asJsonString()

    def asJsonString(self):
        """ A JSON string representation of this pinterest.Pin instance
        :return: A JSON string representation of this pinterest.Pin instance
        """
        return json.dumps(self.asDict(), sort_keys=True)

    def asDict(self):
        """ A dict representation of this pinterest.Pin instance
        The return value uses the same key names as the JSON representation
        :return: A dict representing this pinterest.Pin instance
        """
        data = {}
        if self.id:
            data['id'] = self.id
        if self.cacheable_id:
            data['cacheable_id'] = self.cacheable_id
        if self.title:
            data['title'] = self.title
        if self.description:
            data['description'] = self.description
        if self.type:
            data['type'] = self.type
        if self.domain:
            data['domain'] = self.domain
        if self.link:
            data['link'] = self.link
        if self.like_count:
            data['like_count'] = self.like_count
        if self.comment_count:
            data['comment_count'] = self.comment_count
        if self.repin_count:
            data['repin_count'] = self.repin_count
        if self.image_square_url:
            data['image_square_url'] = self.image_square_url
        if self.image_square_size_pixels:
            data['image_square_size_pixels'] = self.image_square_size_pixels
        if self.image_square_size_points:
            data['image_square_size_points'] = self.image_square_size_points
        if self.image_medium_url:
            data['image_medium_url'] = self.image_medium_url
        if self.image_medium_size_pixels:
            data['image_medium_size_pixels'] = self.image_medium_size_pixels
        if self.image_medium_size_points:
            data['image_medium_size_points'] = self.image_medium_size_points
        if self.image_large_url:
            data['image_large_url'] = self.image_large_url
        if self.image_large_size_pixels:
            data['image_large_size_pixels'] = self.image_large_size_pixels
        if self.image_square_size_points:
            data['image_large_size_points'] = self.image_large_size_points
        if self.price_value:
            data['price_value'] = self.price_value
        if self.price_currency:
            data['price_currency'] = self.price_currency
        if self.attribution:
            data['attribution'] = self.attribution
        if self.tracked_link:
            data['tracked_link'] = self.tracked_link
        if self.promoter:
            data['promoter'] = self.promoter
        if self.debug:
            data['debug'] = self.debug
        if self.liked_by_me:
            data['liked_by_me'] = self.liked_by_me
        if self.is_repin:
            data['is_repin'] = self.is_repin
        if self.is_uploaded:
            data['is_uploaded'] = self.is_uploaded
        if self.is_playable:
            data['is_playable'] = self.is_playable
        if self.is_video:
            data['is_video'] = self.is_video
        if self.created_at:
            data['created_at'] = self.created_at
        return data

    @staticmethod
    def newFromJsonDict(data):
        """ Create a new instance based on a JSON dict
        :param data:  A JSON dict, as converted from the JSON in the pinterest API
        :return: A pinterest.Pin instance
        """
        return Pin(id=data.get('id', None),
                   cacheable_id=data.get('cacheable_id', None),
                   title=data.get('title', None),
                   description=data.get('description', None),
                   type=data.get('type', None),
                   domain=data.get('domain', None),
                   link=data.get('link', None),
                   like_count=data.get('like_count', 0),
                   comment_count=data.get('comment_count', 0),
                   repin_count=data.get('repin_count', 0),
                   image_square_url=data.get('image_square_url', None),
                   image_square_size_pixels=data.get('image_square_size_pixels', {}),
                   image_square_size_points=data.get('image_square_size_points', {}),
                   image_medium_url=data.get('image_square_url', None),
                   image_medium_size_pixels=data.get('image_medium_size_pixels', {}),
                   image_medium_size_points=data.get('image_medium_size_points', {}),
                   image_large_url=data.get('image_large_url', None),
                   image_large_size_pixels=data.get('image_large_size_pixels', {}),
                   image_large_size_points=data.get('image_large_size_points', {}),
                   price_value=data.get('price_value', 0),
                   price_currency=data.get('price_currency', None),
                   attribution=data.get('attribution', None),
                   tracked_link=data.get('tracked_link', None),
                   promoter=data.get('promoter', None),
                   debug=data.get('debug', None),
                   liked_by_me=data.get('liked_by_me', False),
                   is_repin=data.get('is_repin', False),
                   is_uploaded=data.get('is_uploaded', False),
                   is_playable=data.get('is_playable', False),
                   is_video=data.get('is_video', False),
                   created_at=data.get('created_at', None))