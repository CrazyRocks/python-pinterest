#!/usr/bin/env python
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" A library that provides a Python interface to the Pinterest API """

__author__ = 'github/jimbach'
__version__ = '1.0'

import json

try:
    from hashlib import md5
except ImportError:
    from md5 import md5

from api import Api
from board import Board
from comment import Comment
from domain import Domain
from error import PinterestError
from pin import Pin
from user import User