#!/usr/bin/env python

class PinterestError(Exception):
    """ Base class for Pinterest errors """

    @property
    def message(self):
        """
        Returns the first argument used to construct this error
        :return: First argument used to construct this error
        """
        return self.args[0]