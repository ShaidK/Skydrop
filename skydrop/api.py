#!/usr/bin/env python

#
# File: api.py | Note: The following class is used to obtained Weather Information using Open Weather API
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

from skydrop.error import APIRequestError

import validators, requests

from loguru import logger
from retry import retry

class RequestHandlerBase(object):
    """
        Note: The following base class will maintain the logic for calling the External Endpoints 
    """

    @logger.catch(reraise = True)
    def __init__(self, uid : str, url : str) -> None:
        if not (validators.url(url)):
            raise ValueError(f"\t {uid} - The parameter [url] has failed validation: [{url}]")
        
        self._uid = uid
        self._url = url    

    @retry((requests.ConnectTimeout), tries = 5, delay = 2, backoff = 5)
    @logger.catch(reraise = True)
    def _get_request(self, params : dict = None, **kwargs) -> requests.Response:
        logger.debug(f"\t {self._uid} - Calling External API: {self._url}")
        try:
            response = requests.get(url = self._url, params = params, **kwargs)
            response.raise_for_status()
        except requests.HTTPError as http_err:
            raise APIRequestError(uid = self._uid,  status_code = http_err.response.status_code)
            
        return response

class OpenWeatherAPIRequestHandler(RequestHandlerBase):
    """
        Note: The following class is used to call the API Endpoint to obtained Weather Conditions 
        & Information based upon a specific Location
    """

    def __init__(self, uid : str,  url : str, key : str) -> None:
        logger.info(f"\t {uid} - Initialising class [OpenWeatherAPIRequestHandler]")
        super().__init__(uid, url)

        self._key = key

    @logger.catch(reraise = True)    
    def obtain_weather(self, lati : float, long : float) -> requests.Response:
        logger.info(f"\t {self._uid} - Calling the Open Weather API Endpoint")
        if not (-180 <= long <= 180):
            raise ValueError(f"\t {self._uid} - Invalid Longitude range provided: [{long}]")

        if not (-90 <= lati <= 90):
            raise ValueError(f"\t {self._uid} - Invalid Latitude range provided: [{lati}]")

        return super()._get_request(params = {
            "appid" : self._key, 
            "lat" : lati, 
            "lon" : long
        })

