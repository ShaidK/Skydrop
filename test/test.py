#!/usr/bin/env python

"""
    TODO: Module dotstring will be written within the next commit
"""

#
# File: test_api.py | Note: The following classes is used to test the OpenWeatherAPIRequestHandler
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

#
# NOTE: Within this File I have disabled specific pylinting as I don't think the
#       guideline should apply to these Testing
#       - missing-function-docstring:
#       - line-too-long
#       - invalid-name
#

# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=invalid-name

from skydrop.error import APIRequestError, InvalidAirportCodeError
from skydrop.data import OpenAirportDatasource
from skydrop.api import OpenWeatherAPIRequestHandler

from parameterized import parameterized
from dotenv import dotenv_values

import unittest, responses, uuid, json

class RequestHandlerIntegrationTestCategory(unittest.TestCase):
    """
        Note: The following class maintains the test suite for the following OpenAPIRequestHandler Integration
        Tests:

        - GIVEN__A_Latitude_And_Longitude__WHEN__Calling_External_Endpoint__THEN__Return_Successful_Response 
    """

    def setUp(self):
        self.key = dotenv_values(".env")["OPEN_WEATHER_API_KEY"]
        self.url = dotenv_values(".env")["OPEN_WEATHER_API_URL"]
        self.uid = str(uuid.uuid1())
        self.lon = 50.0
        self.lat = 50.0

    @parameterized.expand([
        ( 50.0, 50.0 ), ( 78.1, -34.2 ), ( 10.0, 17.0 ), ( -5.0, 150.0 )
    ])
    def test__GIVEN__A_Latitude_And_Longitude__WHEN__Calling_External_Endpoint__THEN__Return_Successful_Response(self, lati : float, long : float):
        obj = OpenWeatherAPIRequestHandler(self.uid, self.url, self.key).obtain_weather(lati, long)

        self.assertEqual(obj.status_code, 200)
        self.assertEqual(obj.json()["coord"]["lon"], long)
        self.assertEqual(obj.json()["coord"]["lat"], lati)

class RequestHandlerUnitTestCategory(unittest.TestCase):
    """
        Note: The following class maintains the test suite for the following OpenAPIRequestHandler Unit Tests:

        - GIVEN__Invalid_URL__WHEN__Initialising_Request_Handler__THEN__Raise_ValueError 
        - GIVEN__Invalid_Longitude__WHEN__Obtaining_Calling_Endpoint__THEN__Raise_ValueError
        - GIVEN__Invalid_Latitude__WHEN__Obtaining_Calling_Endpoint__THEN__Raise_ValueError
        - GIVEN__Success_Response__WHEN__Calling_External_Endpoint__THEN__Raise_APIRequestError
        - GIVEN__Not_Found_Response__WHEN__Calling_External_Endpoint__THEN__Raise_APIRequestError
        - GIVEN__Bad_Request_Response__WHEN__Calling_External_Endpoint__THEN__Raise_APIRequestError
    """

    def setUp(self) -> None:
        self.url = "https://randomurl.com"
        self.uid = str(uuid.uuid1())
        self.key = str(uuid.uuid1())
        self.lon = 50.0
        self.lat = 50.0

    @parameterized.expand([
        ( None ), ( str() ), ( "invalid_url" )
    ])
    def test__GIVEN__Invalid_URL__WHEN__Initialising_Request_Handler__THEN__Raise_ValueError(self, invalid_url):
        with self.assertRaises(ValueError) as value_err:
            OpenWeatherAPIRequestHandler(self.uid, invalid_url, self.key)

        self.assertEqual(value_err.exception.__str__(), f"\t {self.uid} - The parameter [url] has failed validation: [{invalid_url}]")

    @parameterized.expand([
        ( None ), ( str() ), ( "" )
    ])
    def test__GIVEN__Invalid_API_Key__WHEN__Initialising_Request_Handler__THEN__Raise_ValueError(self, invalid_key):
        with self.assertRaises(ValueError) as value_err:
            OpenWeatherAPIRequestHandler(self.uid, self.url, invalid_key)

        self.assertEqual(value_err.exception.__str__(), f"\t {self.uid} - The parameter [key] has failed validation: [{invalid_key}]")

    @parameterized.expand([
        ( 190.0 ), ( -190.0 ), ( 200.0 ), ( -200.0 )
    ])
    def test__GIVEN__Invalid_Longitude__WHEN__Obtaining_Calling_Endpoint__THEN__Raise_ValueError(self, invalid_lon):
        with self.assertRaises(ValueError) as value_err:
            OpenWeatherAPIRequestHandler(self.uid, self.url, self.key).obtain_weather(self.lat, invalid_lon)

        self.assertEqual(value_err.exception.__str__(), f"\t {self.uid} - Invalid Longitude range provided: [{invalid_lon}]")

    @parameterized.expand([
        ( 95.0 ), ( -95.0 ), ( 100.0 ), ( -100.0 )
    ])
    def test__GIVEN__Invalid_Latitude__WHEN__Obtaining_Calling_Endpoint__THEN__Raise_ValueError(self, invalid_lat):
        with self.assertRaises(ValueError) as value_err:
            OpenWeatherAPIRequestHandler(self.uid, self.url, self.key).obtain_weather(invalid_lat, self.lon)

        self.assertEqual(value_err.exception.__str__(), f"\t {self.uid} - Invalid Latitude range provided: [{invalid_lat}]")

    @responses.activate
    def test__GIVEN__Success_Response__WHEN__Calling_External_Endpoint__THEN__Raise_APIRequestError(self):
        json_response = self.read_json_file("./test/res/open_api_success.json")
        responses.add(responses.GET, self.url, json = json_response, status = 200)

        obj = OpenWeatherAPIRequestHandler(self.uid, self.url, self.key).obtain_weather(self.lat, self.lon)

        self.assertEqual(obj.status_code, 200)
        self.assertEqual(obj.json()["coord"]["lon"], self.lon)
        self.assertEqual(obj.json()["coord"]["lat"], self.lat)

    @responses.activate
    def test__GIVEN__Not_Found_Response__WHEN__Calling_External_Endpoint__THEN__Raise_APIRequestError(self):
        responses.add(responses.GET, self.url, json = { "code" : "Not Found" }, status = 404)

        with self.assertRaises(APIRequestError) as api_err:
            OpenWeatherAPIRequestHandler(self.uid, self.url, self.key).obtain_weather(self.lat, self.lon)

        self.assertEqual(api_err.exception.status_code, 404)

    @responses.activate
    def test__GIVEN__Bad_Request_Response__WHEN__Calling_External_Endpoint__THEN__Raise_APIRequestError(self):
        responses.add(responses.GET, self.url, json = { "code" : "Bad Request" }, status = 400)

        with self.assertRaises(APIRequestError) as api_err:
            OpenWeatherAPIRequestHandler(self.uid, self.url, self.key).obtain_weather(self.lat, self.lon)

        self.assertEqual(api_err.exception.status_code, 400)

    @parameterized.expand([
        ( "LONG_STRING" ), ( "S" )
    ])
    def test__GIVEN__An_Invalid_IATA_Code__WHEN__Obtaining_The_Airport_Information__THEN__Raise_InvalidAirportCodeError(self, invalid_iata):
        with self.assertRaises(InvalidAirportCodeError) as code_error:
            OpenAirportDatasource(self.uid).get_airport_by_iata(iata = invalid_iata)

        self.assertEqual(code_error.exception.__str__(), f"\t {self.uid} - Error raised when Airport Code fail Validation: [ {invalid_iata} ]")

    @parameterized.expand([
        ( "LONG_STRING" ), ( "S" )
    ])
    def test__GIVEN__An_Invalid_ICAO_Code__WHEN__Obtaining_The_Airport_Information__THEN__Raise_InvalidAirportCodeError(self, invalid_icao):
        with self.assertRaises(InvalidAirportCodeError) as code_error:
            OpenAirportDatasource(self.uid).get_airport_by_icao(icao = invalid_icao)

        self.assertEqual(code_error.exception.__str__(), f"\t {self.uid} - Error raised when Airport Code fail Validation: [ {invalid_icao} ]")

    @parameterized.expand([
        ( "BHX" ), ( "LHR" )
    ])
    def test__GIVEN__An_Valid_IATA_Code__WHEN__Obtaining_The_Airport_Information__THEN__InvalidAirportCodeError_Not_Raised(self, valid_iata):
        OpenAirportDatasource(self.uid).get_airport_by_iata(iata = valid_iata)

    @parameterized.expand([
        ( "EGBB" ), ( "EGLL" )
    ])
    def test__GIVEN__An_Valid_ICAO_Code__WHEN__Obtaining_The_Airport_Information__THEN__InvalidAirportCodeError_Not_Raised(self, valid_icao):
        OpenAirportDatasource(self.uid).get_airport_by_icao(icao = valid_icao)

    def read_json_file(self, path : str) -> dict:
        #
        # NOTE: This Function is mainly used within testing so we want to raise the following
        #       Exception to help debug any issues
        #       - json.JSONDecodeError
        #       - FileNotFoundError
        #
        with open(file = path, mode = "r", encoding="UTF-8") as json_file:
            return json.load(json_file)
