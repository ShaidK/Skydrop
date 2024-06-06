#!/usr/bin/env python

"""
    TODO: Module dotstring will be written within the next commit
"""

#
# File: error.py | Note: The following classes are used to maintain custom raise Exceptions
#

#
# MIT License
#
# Copyright (c) 2024 Shaid Khan
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

class APIRequestError(Exception):
    """
        Note: The following class is used to represent an Exception which is raised when calling an
        External API Endpoint 
    """
    def __init__(self, uid : str, status_code : int) -> None:
        """
            TODO: Function docstring will be written within the next commit
        """
        super().__init__(f"\t {uid} - Error raised when calling the External API: {status_code}")
        self.status_code = status_code
