#!/usr/bin/env python
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" A library that provides a Python interface to the Pinterest API """

from urllib.parse import urlparse, urlunparse, urlencode
import requests

from .board import Board
from .comment import Comment
from .domain import Domain
from .error import PinterestError
from .pin import Pin
from .user import User

PRIVACY = ['public', 'secret']
CATEGORIES = ['animals', 'apparel', 'architecture', 'art', 'art_arch', 'cars_motorcycles', 'celebrities',
              'celebrities_public_figures', 'corgis', 'design', 'diy_crafts', 'education', 'everything',
              'fashion', 'featured', 'film_music_books', 'fitness', 'food_drink', 'for_dad', 'gardening',
              'geek', 'gift_guides', 'gifts', 'hair_beauty', 'health_fitness', 'history', 'holidays',
              'holidays_events', 'home', 'home_decor', 'home_improvement', 'humor', 'illustrations_posters',
              'kids', 'men_apparel', 'mens_fashion', 'mylife', 'other', 'outdoors', 'people', 'pets',
              'photography', 'popular', 'prints_posters', 'products', 'quotes', 'science', 'science_nature',
              'sports', 'tattoos', 'technology', 'travel', 'travel_places', 'videos', 'wedding_events',
              'weddings', 'women_apparel', 'womens_fashion']
LAYOUTS = ['default', 'places']
METHODS = ['android', 'android_tablet', 'api_other', 'api_sdk', 'bad', 'bookmarklet', 'button', 'email',
           'extension', 'ipad', 'iphone', 'scraped', 'unknown', 'uploaded']


class Api(object):
    """
    A Python interface into the Pinterest API

    Example usage:

      To create an instance of the pinterest.Api class
        >>> import pinterest
        >>> api = pinterest.Api(access_token='userAccessToken')

      To fetch your user's information
        >>> me = api.getMyInformation()
        >>> print(me.full_name)

      To fetch a board's pins
        >>> pins = api.getBoardPins(board_id='boardId')
        >>> print [p.title for p in pins]

      Here are all the methods:
        >>> api.createBoard(**board_meta)
        >>> api.createPin(**pin_meta)
        >>> api.updateBoard(board_id, **board_meta)
        >>> api.getBoardPins(board_id)
        >>> api.getDomain(domain_name)
        >>> api.getDomainPins(domain_name)
        >>> api.getPinComments(pin_id)
        >>> api.getMyInformation()
        >>> api.getMyBoards()
    """

    def __init__(self,
                 access_token=None,
                 input_encoding=None,
                 base_url=None):
        """
        Instantiates a new pinterest.Api object
        :param access_token: A user's Pinterest access token
        :param input_encoding: The encoding used to encode input strings [Optional]
        :param base_url: The base URL to use to contact the Pinterest API
                         Defaults to https://api.pinterest.com/v3 [Optional]
        :return:
        """
        self._input_encoding = input_encoding

        if base_url is None:
            self.base_url = 'https://api.pinterest.com/v3'
        else:
            self.base_url = base_url

        if access_token is None:
            raise PinterestError({'message': "Pinterest requires an access token for all API access."})
        self._access_token = access_token

    def clearCredentials(self):
        """
        Clears any credentials for this instance
        """
        self._access_token = None

    def createBoard(self,
                    name=None,
                    privacy=None,
                    category=None,
                    layout=None,
                    description=None,
                    protected=False):
        """
        Creates a Board
        :param name: The name of the Board
        :param privacy: Board privacy settings [public, secret]
        :param category: The category key of the Board (see CATEGORIES)
        :param layout: The layout assigned to the Board [default, places]
        :param description: Free form description text of the Board
        :param protected: Whether or not this board will be a protected Board [True, False]
        :return: The created Board object
        """
        url = '{}/boards/'.format(self.base_url)

        if not self._access_token:
            raise PinterestError({'message': 'API must be authenticated.'})

        parameters = {}

        if name is None:
            raise PinterestError({'message': 'The Board name is required.'})
        parameters['name'] = name

        if privacy is not None and privacy not in PRIVACY:
            raise PinterestError({'message': 'The Board privacy must be either public or secret.'})
        parameters['privacy'] = privacy if not None else 'public'

        if category is not None and category not in CATEGORIES:
            raise PinterestError({'message': 'The Board category must be one of the following: {}'.format(
                                 ', '.join(CATEGORIES))})
        elif category is not None:
            parameters['category'] = category

        if layout is not None and layout not in LAYOUTS:
            raise PinterestError({'message': 'The Board layout must be either default or places.'})
        parameters['layout'] = layout if not None else 'default'

        parameters['description'] = description if not None else ''

        parameters['protected'] = protected if not None and isinstance(protected, bool) else False

        response = self._requestUrl(url, 'PUT', data=parameters)
        data = self._parseAndCheckPinterest(response)

        return Board.newFromJsonDict(data['data'])

    def updateBoard(self,
                    board_id=None,
                    name=None,
                    privacy=None,
                    category=None,
                    layout=None,
                    description=None,
                    protected=False):
        """
        Edits an existing board
        :param board_id: The ID of the Board
        :param name: The name of the Board
        :param privacy: Board privacy settings [public, secret]
        :param category: The category key of the board (see CATEGORIES)
        :param layout: The layout assigned to the board [default, places]
        :param description: Free form description text of the Board
        :param protected: Whether or not this board will be a protected Board [True, False]
        :return: The updated board object
        """
        url = '{}/boards/{}/'.format(self.base_url, board_id)

        if not self._access_token:
            raise PinterestError({'message': 'API must be authenticated.'})

        parameters = {}

        if name is not None and name == '':
            raise PinterestError({'message': 'The Board name cannot be blank.'})
        elif name is not None:
            parameters['name'] = name

        if privacy is not None and privacy not in PRIVACY:
            raise PinterestError({'message': 'The Board privacy must be either public or secret.'})
        elif privacy is not None:
            parameters['privacy'] = privacy

        if category is not None and category not in CATEGORIES:
            raise PinterestError({'message': 'The Board category must be one of the following: {}'.format(
                                 ', '.join(CATEGORIES))})
        elif category is not None:
            parameters['category'] = category

        if layout is not None and layout not in LAYOUTS:
            raise PinterestError({'message': 'The Board layout must be either default or places.'})
        elif layout is not None:
            parameters['layout'] = layout

        if description is not None:
            parameters['description'] = description

        if protected is not None and isinstance(protected, bool):
            parameters['protected'] = protected

        response = self._requestUrl(url, 'POST', data=parameters)
        data = self._parseAndCheckPinterest(response)

        return Board.newFromJsonDict(data['data'])

    def createPin(self,
                  board_id=None,
                  description=None,
                  source_url=None,
                  place=None,
                  share_facebook=None,
                  share_twitter=None,
                  image_url=None,
                  image=None,
                  method=None,
                  sdk_client_id=None):
        """
        Creates a Pin
        :param board_id: The ID of the board to pin onto (must be owned by the user
        :param description: The text description for the Pin
        :param source_url: The URL from which the Pin's image was returned
        :param place: The place at which to tag the pin
        :param share_facebook: Whether or not the user wants to share this Pin on Facebook (defaults False)
        :param share_twitter: Whether or not the user wants to share this Pin on Twitter (defaults False)
        :param image_url: The URL of the image to use for the Pin, if it is not uploaded directly
        :param image: The image to use for this Pin as a stream of bytes
        :param method: The method that created the pin (defaults to api_sdk)
                       [android, android_tablet, api_other, api_sdk, bad, bookmarklet, button, email, extension, ipad,
                       iphone, scraped, unknown, uploaded]
        :param sdk_client_id: The original client id of an application that made an SDK request
        :return: The created Pin object
        """
        url = '{}/pins/'.format(self.base_url)

        if not self._access_token:
            raise PinterestError({'message': 'API must be authenticated.'})

        parameters = {}

        if board_id is None:
            raise PinterestError({'message': 'A Board ID is required.'})
        parameters['board_id'] = board_id

        if description is None or description == '':
            raise PinterestError({'message': 'A Pin description is required.'})
        parameters['board_id'] = board_id

        if source_url is None or source_url == '':
            raise PinterestError({'message': 'A Pin source URL is required.'})
        parameters['source_url'] = source_url

        if place is not None:
            parameters['place'] = place

        if share_facebook is not None and isinstance(share_facebook, bool):
            parameters['share_facebook'] = share_facebook
        else:
            parameters['share_facebook'] = False

        if share_twitter is not None and isinstance(share_twitter, bool):
            parameters['share_twitter'] = share_twitter
        else:
            parameters['share_twitter'] = False

        if image_url is not None:
            parameters['image_url'] = image_url

        if image is not None:
            parameters['image'] = image

        if (image_url is None or image_url == '') and (image is None or image == ''):
            raise PinterestError({'message': 'Either an image URL or image file is required.'})

        if method is not None and method not in METHODS:
            raise PinterestError({'message': 'The Pin upload method must be one of the following: {}'.format(
                ', '.join(METHODS)
            )})
        parameters['method'] = method if method is not None else 'api_sdk'

        if sdk_client_id is not None:
            parameters['sdk_client_id'] = sdk_client_id

        response = self._requestUrl(url, 'PUT', data=parameters)
        data = self._parseAndCheckPinterest(response)

        return Board.newFromJsonDict(data['data'])

    def getBoardPins(self, board_id=None, bookmark=False):
        """
        Gets the Pins of a specific Board
        :param board_id: The Board ID
        :return: List of Pins for a specific Board
        """
        url = '{}/boards/{}/pins/'.format(self.base_url, board_id)
        extra_params = {}  # Check for pagination
        if bookmark:
            extra_params['bookmark'] = bookmark
        response = self._requestUrl(url, 'GET', data=extra_params)
        data = self._parseAndCheckPinterest(response)
        bookmark = data['bookmark'] if 'bookmark' in data and data['bookmark'] != '' else False

        return [Pin.newFromJsonDict(x) for x in data['data']], bookmark

    def getDomain(self, domain_name=None):
        """
        Gets a Domain's info
        :param domain_name: The Domain name
        :return: A Domain object
        """
        url = '{}/domains/{}/'.format(self.base_url, domain_name)

        if not self._access_token:
            raise PinterestError({'message': 'API must be authenticated.'})

        if domain_name is None:
            raise PinterestError({'message': 'A Domain name is required.'})

        response = self._requestUrl(url, 'GET')
        data = self._parseAndCheckPinterest(response)

        return Domain.newFromJsonDict(data['data'])

    def getDomainPins(self, domain_name=None, bookmark=False):
        """
        Gets the Pins for a specific Domain
        :param domain_name: The Domain's name
        :return: A list of Pins for a specific Domain
        """
        url = '{}/domains/{}/pins/'.format(self.base_url, domain_name)

        if not self._access_token:
            raise PinterestError({'message': 'API must be authenticated.'})

        if domain_name is None:
            raise PinterestError({'message': 'A Domain name is required.'})

        extra_params = {}  # Check for pagination
        if bookmark:
            extra_params['bookmark'] = bookmark
        response = self._requestUrl(url, 'GET', data=extra_params)
        data = self._parseAndCheckPinterest(response)
        bookmark = data['bookmark'] if 'bookmark' in data and data['bookmark'] != '' else False

        return [Pin.newFromJsonDict(x) for x in data['data']], bookmark

    def getPinComments(self, pin_id=None, bookmark=False):
        """
        Gets the comments for a specific Pin
        :param pin_id: The Pin ID
        :return: A list of Comments for the specific Pin
        """
        url = '{}/pins/{}/comments/'.format(self.base_url, pin_id)

        if not self._access_token:
            raise PinterestError({'message': 'API must be authenticated.'})

        if pin_id is None:
            raise PinterestError({'message': 'A Pin ID is required.'})

        extra_params = {}  # Check for pagination
        if bookmark:
            extra_params['bookmark'] = bookmark
        response = self._requestUrl(url, 'GET', data=extra_params)
        data = self._parseAndCheckPinterest(response)
        bookmark = data['bookmark'] if 'bookmark' in data and data['bookmark'] != '' else False

        return [Comment.newFromJsonDict(x) for x in data['data']], bookmark

    def getMyInformation(self):
        """
        Gets the User details for the authenticated User
        :return: A User object
        """
        url = '{}/users/me/'.format(self.base_url)

        if not self._access_token:
            raise PinterestError({'message': 'API must be authenticated.'})

        response = self._requestUrl(url, 'GET')
        data = self._parseAndCheckPinterest(response)

        return User.newFromJsonDict(data['data'])

    def getMyBoards(self, bookmark=False):
        """
        Gets the Boards for the authenticated User
        :return: List of Boards for the authenticated User
        """
        url = '{}/users/me/boards/'.format(self.base_url)

        if not self._access_token:
            raise PinterestError({'message': 'API must be authenticated.'})

        extra_params = {}  # Check for pagination
        if bookmark:
            extra_params['bookmark'] = bookmark
        response = self._requestUrl(url, 'GET', data=extra_params)
        data = self._parseAndCheckPinterest(response)
        bookmark = data['bookmark'] if 'bookmark' in data and data['bookmark'] != '' else False

        return [Board.newFromJsonDict(x) for x in data['data']], bookmark

    def _buildUrl(self, url, path_elements=None, extra_params=None):
        """
        Builds a request URL
        :param url: Base URL
        :param path_elements: Any extra path elements
        :param extra_params: Any extra parameters
        :return: URL with extra path elements and parameter
        """
        # Break url into constituent parts
        (scheme, netloc, path, params, query, fragment) = urlparse(url)

        # Add any additional path elements to the path
        if path_elements:
            # Filter out the path elements that have a value of None
            p = [i for i in path_elements if i]
            if not path.endswith('/'):
                path += '/'
            path += '/'.join(p)

        # Add the access token as part of the query
        if query:
            query += '&access_token={}'.format(self._access_token)
        else:
            query = 'access_token={}'.format(self._access_token)

        # Add any additional query parameters to the query string
        if extra_params and len(extra_params) > 0:
            extra_query = self._encodeParameters(extra_params)
            # Add it to the existing query
            if query:
                query += '&' + extra_query
            else:
                query = extra_query

        # Return the rebuilt URL
        return urlunparse((scheme, netloc, path, params, query, fragment))

    def _encode(self, s):
        """
        Encodes a string based on self._input_encoding
        :param s: String to encode
        :return: Encoded string
        """
        if self._input_encoding:
            return str(s, self._input_encoding).encode('utf-8')
        else:
            return str(s).encode('utf-8')

    def _encodeParameters(self, parameters):
        """
        Return a tring in key=value&key=value form

        Values of None are not included in the output string
        :param parameters: A dict of (key, value) tuples where value is encoded as specified by self._input_encoding
        :return: A URL-encoded string in key=value&key=value form
        """
        if parameters is None:
            return None
        else:
            return urlencode(dict([(k, self._encode(v)) for k, v in parameters.items() if v is not None]))

    def _encodePostData(self, post_data):
        """
        Returns a string in key=value&key=value form

        Values are assumed to be encoded in the format specified by self._input_encoding
        and are subsequently URL encoded
        :param post_data: A dict of (key, value) tuples, where value is encoded as specified by self._input_encoding
        :return:
        """
        if post_data is None:
            return None
        else:
            return urlencode(dict([(k, self._encode(v)) for k, v in post_data.items()]))

    def _requestUrl(self, url, verb, data=None):
        """
        Submits a request to a URL
        :param url: The web location we want to retrieve
        :param verb: POST, GET, PUT
        :param data: A dictionary of key/value pairs
        :param bookmark: A field used for pagination
        :return: A JSON object
        """
        if verb == 'PUT':
            url = self._buildUrl(url)
            try:
                return requests.put(url, data=data)
            except requests.RequestException as e:
                raise PinterestError(str(e))
        elif verb == 'POST':
            url = self._buildUrl(url)
            try:
                return requests.post(url, data=data)
            except requests.RequestException as e:
                raise PinterestError(str(e))
        elif verb == 'GET':
            url = self._buildUrl(url, extra_params=data)
            try:
                return requests.get(url)
            except requests.RequestException as e:
                raise PinterestError(str(e))
        return 0

    def _parseAndCheckPinterest(self, response):
        """
        Trys to parse the JSON returned from Pinterest
        Returns an empty dictionary if there is an error
        :param response: Request response returned from Pinterest
        :return: Parsed JSON
        """
        try:
            data = response.json()
            self._checkForPinterestError(data)
        except ValueError:
            raise PinterestError({'message': "An error occurred while parsing a Pinterest response."})

        return data

    def _checkForPinterestError(self, data):
        """
        Raises a PinterestError if Pinterest returns an error message
        :param data: A python dict created from the Pinterest JSON response
        :return: PinterestError wrapping the Pinterest error message if one exists
        """
        if 'status' in data and data['status'] == 'failure':
            raise PinterestError(data['message'])
