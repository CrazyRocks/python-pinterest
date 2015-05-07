#!/usr/bin/env python

import json


class User(object):
    """ A class representing a User structure used by the pinterest API

    The User structure exposes the following properties:
    User.id
    User.first_name
    User.last_name
    User.full_name
    User.following_count
    User.follower_count
    User.pin_count
    User.board_count
    User.like_count
    User.email
    User.email_verified
    User.email_verification_code
    User.username
    User.about
    User.location
    User.type
    User.pins
    User.pin_thumbnail_urls
    User.repins_from
    User.followed_boards
    User.image_small_url
    User.image_medium_url
    User.image_large_url
    User.is_default_image
    User.has_password
    User.is_employee
    User.followed_by_me
    User.domain_verified
    User.explicitly_followed_by_me
    User.implicitly_followed_by_me
    User.blocked_by_me
    User.gplus_url
    User.domain_url
    User.is_partner
    User.partner
    User.indexed
    User.website_url
    User.latest_category
    User.ads_customize_from_conversion
    User.low_engagement_board_count
    User.personalize_from_offsite_browsing
    User.verified_domains
    User.tag
    User.debug
    User.created_at
    """

    def __init__(self, **kwargs):
        """ User initializer
        :param kwargs: Keyword arguments
        """
        param_defaults = {
            'id': None,
            'first_name': None,
            'last_name': None,
            'full_name': None,
            'following_count': 0,
            'follower_count': 0,
            'pin_count': 0,
            'board_count': 0,
            'like_count': 0,
            'email': None,
            'email_verified': False,
            'email_verification_code': None,
            'username': None,
            'about': None,
            'location': None,
            'type': 'user',
            'pins': [],
            'pin_thumbnail_urls': [],
            'repins_from': [],
            'followed_boards': [],
            'image_small_url': None,
            'image_medium_url': None,
            'image_large_url': None,
            'is_default_image': False,
            'has_password': False,
            'is_employee': False,
            'followed_by_me': False,
            'domain_verified': False,
            'explicitly_followed_by_me': False,
            'implicitly_followed_by_me': False,
            'blocked_by_me': False,
            'gplus_url': None,
            'domain_url': None,
            'is_partner': False,
            'partner': None,
            'indexed': False,
            'website_url': None,
            'latest_category': [],
            'ads_customize_from_conversion': False,
            'low_engagement_board_count': 0,
            'personalize_from_offsite_browsing': False,
            'verified_domains': [],
            'tag': None,
            'debug': None,
            'created_at': None}

        # Override defaults
        for (param, default) in param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    @property
    def id(self):
        """ Gets the unique ID of the User
        :return: The unique ID of the User
        """
        return self._id

    @id.setter
    def id(self, value):
        """ Sets the unique ID of the User
        :param value: The unique ID of the User
        """
        self._id = value

    @property
    def first_name(self):
        """ Gets the User's first name
        :return: The User's first name
        """
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """ Sets the User's first name
        :param value: The User's first name
        """
        self._first_name = value

    @property
    def last_name(self):
        """ Gets the User's last name
        :return: The User's last name
        """
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """ Sets the User's last name
        :param value: The User's last name
        """
        self._last_name = value

    @property
    def full_name(self):
        """ Gets the User's full name
        :return: The User's full name
        """
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        """ Sets the User's full name
        :param value: The User's full name
        """
        self._full_name = value

    @property
    def following_count(self):
        """ Gets the User's following count
        :return: The User's following count
        """
        return self._following_count

    @following_count.setter
    def following_count(self, value):
        """ Sets the User's following count
        :param value: The User's following count
        """
        self._following_count = value

    @property
    def follower_count(self):
        """ Gets the User's follower count
        :return: The User's follower count
        """
        return self._follower_count

    @follower_count.setter
    def follower_count(self, value):
        """ Sets the User's follower count
        :param value: The User's follower count
        """
        self._follower_count = value

    @property
    def pin_count(self):
        """ Gets the User's pin count
        :return: The User's pin count
        """
        return self._pin_count

    @pin_count.setter
    def pin_count(self, value):
        """ Sets the User's pin count
        :param value: The User's pin count
        """
        self._pin_count = value

    @property
    def board_count(self):
        """ Gets the User's board count
        :return: The User's board count
        """
        return self._board_count

    @board_count.setter
    def board_count(self, value):
        """ Sets the User's board count
        :param value: The User's board count
        """
        self._board_count = value

    @property
    def like_count(self):
        """ Gets the User's like count
        :return: The User's like count
        """
        return self._like_count

    @like_count.setter
    def like_count(self, value):
        """ Sets the User's like count
        :param value: The User's like count
        """
        self._like_count = value

    @property
    def email(self):
        """ Gets the User's email
        :return: The User's email
        """
        return self._email

    @email.setter
    def email(self, value):
        """ Sets the User's email
        :param value: The User's email
        """
        self._email = value

    @property
    def email_verified(self):
        """ Gets the User's email status (if it's verified)
        :return: The User's email status, True if verified, False otherwise
        """
        return self._email_verified

    @email_verified.setter
    def email_verified(self, value):
        """ Sets the User's email status (if it's verified)
        :param value: The User's email status, True if verified, False otherwise
        """
        self._email_verified = value

    @property
    def email_verification_code(self):
        """ Gets the User's email verification code
        :return: The User's email verification code
        """
        return self._email_verification_code

    @email_verification_code.setter
    def email_verification_code(self, value):
        """ Sets the User's email verification code
        :param value: The User's email verification code
        """
        self._email_verification_code = value

    @property
    def username(self):
        """ Gets the User's username
        :return: The User's username
        """
        return self._username

    @username.setter
    def username(self, value):
        """ Sets the User's username
        :param value: The User's username
        """
        self._username = value

    @property
    def about(self):
        """ Gets the User's about info
        :return: The User's about info
        """
        return self._about

    @about.setter
    def about(self, value):
        """ Sets the User's about info
        :param value: The User's about info
        """
        self._about = value

    @property
    def location(self):
        """ Gets the User's location
        :return: The User's location
        """
        return self._location

    @location.setter
    def location(self, value):
        """ Sets the User's location
        :param value: The User's location
        """
        self._location = value

    @property
    def type(self):
        """ Gets the User's type (only known type: user)
        :return: The User's type
        """
        return self._type

    @type.setter
    def type(self, value):
        """ Sets the User's type (only known type: user)
        :param value: The User's type
        """
        self._type = value

    @property
    def pins(self):
        """ Gets the User's pins
        :return: The User's pins
        """
        return self._pins

    @pins.setter
    def pins(self, value):
        """ Sets the User's pins
        :param value: The User's pins
        """
        self._pins = value

    @property
    def pin_thumbnail_urls(self):
        """ Gets the User's pins' thumbnail URLs
        :return: The User's pins' thumbnail URLs
        """
        return self._pin_thumbnail_urls

    @pin_thumbnail_urls.setter
    def pin_thumbnail_urls(self, value):
        """ Sets the User's pins' thumbnail URLs
        :param value: The User's pins' thumbnail URLs
        """
        self._pin_thumbnail_urls = value

    @property
    def repins_from(self):
        """ Gets the User's repins from
        :return: The User's repins from
        """
        return self._repins_from

    @repins_from.setter
    def repins_from(self, value):
        """ Sets the User's repins from
        :param value: The User's repins from
        """
        self._repins_from = value

    @property
    def followed_boards(self):
        """ Gets the User's followed boards
        :return: The User's followed boards
        """
        return self._followed_boards

    @followed_boards.setter
    def followed_boards(self, value):
        """ Sets the User's followed boards
        :param value: The User's followed boards
        """
        self._followed_boards = value

    @property
    def image_small_url(self):
        """ Gets the User's small image URL
        :return: The User's small image URL
        """
        return self._image_small_url

    @image_small_url.setter
    def image_small_url(self, value):
        """ Sets the User's small image URL
        :param value: The User's small image URL
        """
        self._image_small_url = value

    @property
    def image_medium_url(self):
        """ Gets the User's medium image URL
        :return: The User's medium image URL
        """
        return self._image_medium_url

    @image_medium_url.setter
    def image_medium_url(self, value):
        """ Sets the User's medium image URL
        :param value: The User's medium image URL
        """
        self._image_medium_url = value

    @property
    def image_large_url(self):
        """ Gets the User's large image URL
        :return: The User's large image URL
        """
        return self._image_large_url

    @image_large_url.setter
    def image_large_url(self, value):
        """ Sets the User's large image URL
        :param value: The User's large image URL
        """
        self._image_large_url = value

    @property
    def is_default_image(self):
        """ Returns whether the User's image is the default image
        :return: True if the image is the User's default image, False otherwise
        """
        return self._is_default_image

    @is_default_image.setter
    def is_default_image(self, value):
        """ Sets whether the User's image is the default image
        :param value: True if the image is the User's default image, False otherwise
        """
        self._is_default_image = value

    @property
    def has_password(self):
        """ Returns whether the User has a password
        :return: True if the User has a password, False otherwise
        """
        return self._has_password

    @has_password.setter
    def has_password(self, value):
        """ Sets whether the User has a password
        :param value: True if the User has a password, False otherwise
        """
        self._has_password = value

    @property
    def is_employee(self):
        """ Returns whether the User is a Pinterest employee
        :return: True if the User is a Pinterest employee, False otherwise
        """
        return self._is_employee

    @is_employee.setter
    def is_employee(self, value):
        """ Sets whether the User is a Pinterest employee
        :param value: True if the User is a Pinterest employee, False otherwise
        """
        self._is_employee = value

    @property
    def followed_by_me(self):
        """ Returns whether the User is followed by me
        :return: True if the User is followed by me, False otherwise
        """
        return self._followed_by_me

    @followed_by_me.setter
    def followed_by_me(self, value):
        """ Sets whether the User is followed by me
        :param value: True if the User is followed by me, False otherwise
        """
        self._followed_by_me = value

    @property
    def domain_verified(self):
        """ Returns whether the User's domain is verified
        :return: True if the User's domain is verified, False otherwise
        """
        return self._domain_verified

    @domain_verified.setter
    def domain_verified(self, value):
        """ Sets whether the User's domain is verified
        :param value: True if the User's domain is verified, False otherwise
        """
        self._domain_verified = value

    @property
    def explicitly_followed_by_me(self):
        """ Returns whether the User is explicitly followed by me
        :return: True if the User is explicitly followed by me, False otherwise
        """
        return self._explicitly_followed_by_me

    @explicitly_followed_by_me.setter
    def explicitly_followed_by_me(self, value):
        """ Sets whether the User is explicitly followed by me
        :param value: True if the User is explicitly followed by me, False otherwise
        """
        self._explicitly_followed_by_me = value

    @property
    def implicitly_followed_by_me(self):
        """ Returns whether the User is implicitly followed by me
        :return: True if the User is explicitly followed by me, False otherwise
        """
        return self._implicitly_followed_by_me

    @implicitly_followed_by_me.setter
    def implicitly_followed_by_me(self, value):
        """ Sets whether the User is implicitly followed by me
        :param value: True if the User is implicitly followed by me, False otherwise
        """
        self._implicitly_followed_by_me = value

    @property
    def blocked_by_me(self):
        """ Returns whether the User is blocked by me
        :return: True if the User is blocked by me, False otherwise
        """
        return self._blocked_by_me

    @blocked_by_me.setter
    def blocked_by_me(self, value):
        """ Sets whether the User is blocked by me
        :param value: True if the User is blocked by me, False otherwise
        """
        self._blocked_by_me = value

    @property
    def gplus_url(self):
        """ Returns the User's G+ URL
        :return: The User's G+ URL
        """
        return self._gplus_url

    @gplus_url.setter
    def gplus_url(self, value):
        """ Sets the User's G+ URL
        :param value: The User's G+ URL
        """
        self._gplus_url = value

    @property
    def domain_url(self):
        """ Returns the User's domain URL
        :return: The User's domain URL
        """
        return self._domain_url

    @domain_url.setter
    def domain_url(self, value):
        """ Sets the User's domain URL
        :param value: The User's domain URL
        """
        self._domain_url = value

    @property
    def is_partner(self):
        """ Returns whether the User is a partner
        :return: True if the User is a partner, False otherwise
        """
        return self._is_partner

    @is_partner.setter
    def is_partner(self, value):
        """ Sets whether the User is a partner
        :param value: True if the User is a partner, False otherwise
        """
        self._is_partner = value

    @property
    def partner(self):
        """ Returns the User's partner if it exists
        :return: The User's partner if it exists
        """
        return self._partner

    @partner.setter
    def partner(self, value):
        """ Sets the User's partner if it exists
        :param value: THe User's partner if it exists
        """
        self._partner = value

    @property
    def indexed(self):
        """ Returns whether the User is indexed
        :return: True if the User is indexed, False otherwise
        """
        return self._indexed

    @indexed.setter
    def indexed(self, value):
        """ Sets whether the User is indexed
        :param value: True if the User is indexed, False otherwise
        """
        self._indexed = value

    @property
    def website_url(self):
        """ Returns the User's website URL
        :return: The User's website URL
        """
        return self._website_url

    @website_url.setter
    def website_url(self, value):
        """ Sets the User's website URL
        :param value: The User's website URL
        """
        self._website_url = value

    @property
    def latest_category(self):
        """ Returns the User's latest active categories
        :return: The User's latest active categories
        """
        return self._latest_category

    @latest_category.setter
    def latest_category(self, value):
        """ Sets the User's latest active categories
        :param value: The User's latest active categories
        """
        self._latest_category = value

    @property
    def ads_customize_from_conversion(self):
        """ Returns whether User's ads were customized from conversion
        :return: True if the User's ads were customized from conversion, False otherwise
        """
        return self._ads_customize_from_conversion

    @ads_customize_from_conversion.setter
    def ads_customize_from_conversion(self, value):
        """ Sets whether User's ads were customized from conversion
        :param value: True if the User's ads were customized from conversion, False otherwise
        """
        self._ads_customize_from_conversion = value

    @property
    def low_engagement_board_count(self):
        """ Returns the User's low engagement board count
        :return: The User's low engagement board count
        """
        return self._low_engagement_board_count

    @low_engagement_board_count.setter
    def low_engagement_board_count(self, value):
        """ Sets the User's low engagement board count
        :param value: The User's low engagement board count
        """
        self._low_engagement_board_count = value

    @property
    def personalize_from_offsite_browsing(self):
        """ Returns whether User's experience was personalized from offsite browsing
        :return: True if the User's experience was personalized from offsite browsing, False otherwise
        """
        return self._personalize_from_offsite_browsing

    @personalize_from_offsite_browsing.setter
    def personalize_from_offsite_browsing(self, value):
        """ Sets whether User's experience was personalized from offsite browsing
        :param value: True if the User's experience was personalized from offsite browsing, False otherwise
        """
        self._personalize_from_offsite_browsing = value

    @property
    def verified_domains(self):
        """ Returns the User's verified domains
        :return: The User's verified domains
        """
        return self._verified_domains

    @verified_domains.setter
    def verified_domains(self, value):
        """ Sets the User's verified domains
        :param value: The User's verified domains
        """
        self._verified_domains = value

    @property
    def tag(self):
        """ Returns the User's tag
        :return: The User's tag
        """
        return self._tag

    @tag.setter
    def tag(self, value):
        """ Sets the User's tag
        :param value: The User's tag
        """
        self._tag = value

    @property
    def debug(self):
        """ Returns the User's debug flag
        :return: The User's debug flag
        """
        return self._debug

    @debug.setter
    def debug(self, value):
        """ Sets the User's debug flag
        :param value: The User's debug flag
        """
        self._debug = value

    @property
    def created_at(self):
        """ Gets the date and time the User was created
        :return: The date and time the User was created
        """
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """ Sets the date and time the User was created
        :param value: The date and time the User was created
        """
        self._created_at = value

    def __ne__(self, other):
        """ Checks if a User is not equal to another User
        :param other: Other User to compare to
        :return: True if Users are not equal, False otherwise
        """
        return not self.__eq__(other)

    def __eq__(self, other):
        """ Checks if a User is equal to another User
        :param other: Other User to compare to
        :return: True if Users are equal, False otherwise
        """
        try:
            return other and \
                   self.id == other.id

        except AttributeError:
            return False

    def __str__(self):
        """ A string representation of this pinterest.User instance
        The return value is the same as the JSON string representation
        :return: A string representation of this pinterest.User instance
        """
        return self.asJsonString()

    def asJsonString(self):
        """ A JSON string representation of this pinterest.User instance
        :return: A JSON string representation of this pinterest.User instance
        """
        return json.dumps(self.asDict(), sort_keys=True)

    def asDict(self):
        """ A dict representation of this pinterest.User instance
        The return value uses the same key names as the JSON representation
        :return: A dict representing this pinterest.User instance
        """
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'full_name': self.full_name,
            'following_count': self.following_count,
            'follower_count': self.follower_count,
            'pin_count': self.pin_count,
            'board_count': self.board_count,
            'like_count': self.like_count,
            'email': self.email,
            'email_verified': self.email_verified,
            'email_verification_code': self.email_verification_code,
            'username': self.username,
            'about': self.about,
            'location': self.location,
            'type': self.type,
            'pins': self.pins,
            'pin_thumbnail_urls': self.pin_thumbnail_urls,
            'repins_from': self.repins_from,
            'followed_boards': self.followed_boards,
            'image_small_url': self.image_small_url,
            'image_medium_url': self.image_medium_url,
            'image_large_url': self.image_large_url,
            'is_default_image': self.is_default_image,
            'has_password': self.has_password,
            'is_employee': self.is_employee,
            'followed_by_me': self.followed_by_me,
            'domain_verified': self.domain_verified,
            'explicitly_followed_by_me': self.explicitly_followed_by_me,
            'implicitly_followed_by_me': self.implicitly_followed_by_me,
            'blocked_by_me': self.blocked_by_me,
            'gplus_url': self.gplus_url,
            'domain_url': self.domain_url,
            'is_partner': self.is_partner,
            'partner': self.partner,
            'indexed': self.indexed,
            'website_url': self.website_url,
            'latest_category': self.latest_category,
            'ads_customize_from_conversion': self.ads_customize_from_conversion,
            'low_engagement_board_count': self.low_engagement_board_count,
            'personalize_from_offsite_browsing': self.personalize_from_offsite_browsing,
            'verified_domains': self.verified_domains,
            'tag': self.tag,
            'debug': self.debug,
            'created_at': self.created_at
        }

    @staticmethod
    def newFromJsonDict(data):
        """ Create a new instance based on a JSON dict
        :param data:  A JSON dict, as converted from the JSON in the pinterest API
        :return: A pinterest.User instance
        """
        return User(id=data.get('id', None),
                    first_name=data.get('first_name', None),
                    last_name=data.get('last_name', None),
                    full_name=data.get('full_name', None),
                    following_count=data.get('following_count', 0),
                    follower_count=data.get('follower_count', 0),
                    pin_count=data.get('pin_count', 0),
                    board_count=data.get('board_count', 0),
                    like_count=data.get('like_count', 0),
                    email=data.get('email', None),
                    email_verified=data.get('email_verified', False),
                    email_verification_code=data.get('email_verification_code', None),
                    username=data.get('username', None),
                    about=data.get('about', None),
                    location=data.get('location', None),
                    type=data.get('type', 'user'),
                    pins=data.get('pins', []),
                    pin_thumbnail_urls=data.get('pin_thumbnail_urls', []),
                    repins_from=data.get('repins_from', []),
                    followed_boards=data.get('followed_boards', []),
                    image_small_url=data.get('image_small_url', None),
                    image_medium_url=data.get('image_medium_url', None),
                    image_large_url=data.get('image_large_url', None),
                    is_default_image=data.get('is_default_image', False),
                    has_password=data.get('has_password', False),
                    is_employee=data.get('is_employee', False),
                    followed_by_me=data.get('followed_by_me', False),
                    domain_verified=data.get('domain_verified', False),
                    explicitly_followed_by_me=data.get('explicitly_followed_by_me', False),
                    implicitly_followed_by_me=data.get('implicitly_followed_by_me', False),
                    blocked_by_me=data.get('blocked_by_me', False),
                    gplus_url=data.get('gplus_url', None),
                    domain_url=data.get('domain_url', None),
                    is_partner=data.get('is_partner', False),
                    partner=data.get('partner', None),
                    indexed=data.get('indexed', False),
                    website_url=data.get('website_url', None),
                    latest_category=data.get('latest_category', []),
                    ads_customize_from_conversion=data.get('ads_customize_from_conversion', False),
                    low_engagement_board_count=data.get('low_engagement_board_count', 0),
                    personalize_from_offsite_browsing=data.get('personalize_from_offsite_browsing', None),
                    verified_domains=data.get('verified_domains', []),
                    tag=data.get('tag', None),
                    debug=data.get('debug', None),
                    created_at=data.get('created_at', None))