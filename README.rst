=========
python-pinterest
=========

A Python wrapper around the Pinterest API.

By Jordan Limbach (limbachjordan@gmail.com) @ Shoutlet, Inc


============
Introduction
============

This library provides a Python interface for the Pinterest API.

This library was developed against Python 3.*

==========
Installing
==========

You can install python-pinterest using::

    $ pip install python-pinterest

Testing::

    $ python test.py

================
Getting the code
================

The code is hosted at https://github.com/jimbach/pinterest

Check out the latest development version anonymously with::

    $ git clone git://github.com/jimbach/pinterest.git
    $ cd pinterest

Setup a virtual environment and install dependencies:

	$ make env

Activate the virtual environment created:

	$ source env/bin/activate

Run tests:

	$ make test

To see other options available, run:

	$ make help


=============
Documentation
=============

View the last release API documentation at: https://developers.pinterest.com/api_docs/

Methods implemented in this library:

def createBoard(self,
                name=None,
                privacy=None,
                category=None,
                layout=None,
                description=None,
                protected=False):
"""
Creates a Board

- param name: The name of the Board
- param privacy: Board privacy settings [public, secret]
- param category: The category key of the Board (see CATEGORIES)
- param layout: The layout assigned to the Board [default, places]
- param description: Free form description text of the Board
- param protected: Whether or not this board will be a protected Board [True, False]
- return: The created Board object
"""


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

- param board_id: The ID of the board to pin onto (must be owned by the user
- param description: The text description for the Pin
- param source_url: The URL from which the Pin's image was returned
- param place: The place at which to tag the pin
- param share_facebook: Whether or not the user wants to share this Pin on Facebook (defaults False)
- param share_twitter: Whether or not the user wants to share this Pin on Twitter (defaults False)
- param image_url: The URL of the image to use for the Pin, if it is not uploaded directly
- param image: The image to use for this Pin as a stream of bytes
- param method: The method that created the pin (defaults to api_sdk) (android, android_tablet, api_other, api_sdk, bad, bookmarklet, button, email, extension, ipad, iphone, scraped, unknown, uploaded)
- param sdk_client_id: The original client id of an application that made an SDK request
- return: The created Pin object
"""


def getBoardPins(self,
		 board_id=None):
"""
Gets the Pins of a specific Board

- param board_id: The Board ID
- return: List of Pins for a specific Board
"""


def getDomain(self,
	      domain_name=None):
"""
Gets a Domain's info

- param domain_name: The Domain name
- return: A Domain object
"""


def getDomainPins(self,
                  domain_name=None):
"""
Gets the Pins for a specific Domain

- param domain_name: The Domain's name
- return: A list of Pins for a specific Domain
"""


def getPinComments(self,
                   pin_id=None):
"""
Gets the comments for a specific Pin

- param pin_id: The Pin ID
- return: A list of Comments for the specific Pin
"""


def getMyInformation(self
                    ):
"""
Gets the User details for the authenticated User

- return: A User object
"""


def getMyBoards(self
               ):
"""
Gets the Boards for the authenticated User

- return: List of Boards for the authenticated User
"""

=====
Using
=====

-----
Model
-----

The five model classes are ``pinterest.Board``, ``pinterest.Comment``, ``pinterest.Domain``, ``pinterest.Pin``, and ``pinterest.User``. The API methods return instances of these classes.

To read the full API for ``pinterest.Board``, ``pinterest.Comment``, ``pinterest.Domain``, ``pinterest.Pin``, or ``pinterest.User``, run::

    $ pydoc pinterest.Board
    $ pydoc pinterest.Comment
    $ pydoc pinterest.Domain
    $ pydoc pinterest.Pin
    $ pydoc pinterest.User

---
API
---

The API is exposed via the ``pinterest.Api`` class.

To create an instance of the ``pinterest.Api`` with login credentials (Pinterest requires a user access token for all API calls)::
    >>> import pinterest
    >>> api = pinterest.Api(access_token='userAccessToken')

To fetch a Board's list of Pins (requires authentication)::
    >>> pins = api.getBoardPins('boardId')
    >>> print [p.title for p in pins]

To create a Board (requires authentication)::
    >>> board = api.createBoard(name='Vacation Destinations',
                                privacy='public',
                                category='travel_places',
                                layout='default',
                                description='Places I want to vacation to',
                                protected=False)
    >>> print board.name
    Vacation Destinations

There are many more API methods, to read the full API documentation::

    $ pydoc pinterest.Api

------------
Contributors
------------

Developed by Jordan Limbach @ Shoutlet, Inc.

-------
License
-------

| Licensed under the Apache License, Version 2.0 (the 'License');
| you may not use this file except in compliance with the License.
| You may obtain a copy of the License at
|
|     http://www.apache.org/licenses/LICENSE-2.0
|
| Unless required by applicable law or agreed to in writing, software
| distributed under the License is distributed on an 'AS IS' BASIS,
| WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
| See the License for the specific language governing permissions and
| limitations under the License.
