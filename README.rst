Pinterest

A Python wrapper around the Pinterest API.

By github/jimbach (limbachjordan@gmail.com) @ Shoutlet, Inc


============
Introduction
============

This library provides a Python interface for the `Pinterest API https://developers.pinterest.com/api_docs/`.
This library was developed against Python 3.*

==========
Installing
==========

You can install pinterest using::

    $ pip install pinterest

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

=====
Using
=====

The library provides a Python wrapper around the Pinterest API and the Pinterest data model.

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
    >>> board = api.PostUpdate(name='Vacation Destinations',
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

Developed by Jordan Limbach in collaboration with Shoutlet, Inc.

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