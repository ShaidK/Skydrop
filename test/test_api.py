#!/usr/bin/env python

#
# File: test_api.py | Note: The following class is used to maintain the testing for the OpenWeatherAPIRequestHandler
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

from skydrop.api import OpenWeatherAPIRequestHandler

from parameterized import parameterized

import unittest

class OpenAPIRequestHandler_Unit_TestCategory(unittest.TestCase):
    """
        Note: The following class maintains the test suite for the following OpenAPIRequestHandler tests:

        - GIVEN__Invalid_URL__WHEN__Initialising_Request_Handler__THEN__Raise_ValueError 
    """

    @parameterized.expand([
        ( None ), ( str() ), ( "invalid_url" )
    ])
    def test__GIVEN__Invalid_URL__WHEN__Initialising_Request_Handler__THEN__Raise_ValueError(self, invalid_url):
        with self.assertRaises(ValueError) as value_err:
            OpenWeatherAPIRequestHandler(invalid_url)
        
        self.assertEqual(value_err.exception.__str__(), f"The parameter [url] has failed validation: [{invalid_url}]")

if __name__ == '__main__':
    unittest.main(verbosity=2)