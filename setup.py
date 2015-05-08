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
""" The setup and build script for the pinterest library """

import os

from setuptools import setup, find_packages


def read(*paths):
    """
    Builds a file path from *paths and returns the contents.
    :param paths: List of file paths
    :return: Contents of the list of file paths
    """
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='python-pinterest',
    version='1.0',
    author='Jordan Limbach github/jimbach',
    author_email='limbachjordan@gmail.com',
    license='Apache License 2.0',
    url='https://github.com/jimbach/pinterest',
    keywords='pinterest api',
    description='A Python wrapper around the Pinterest API',
    long_description=(read('README.rst')),
    packages=find_packages(exclude=['tests*']),
    install_requires=['requests', 'flake8'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)