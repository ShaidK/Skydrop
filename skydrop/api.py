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

from skydrop.base import EntityBase, RequestHandlerBase

import requests

from loguru import logger

class Coordinate(EntityBase):
    """
        Note: The following class will maintain the Latitude & Longitude Functionality  
    """
    def __init__(self, uuid : str, lati : float, long : float) -> None:
        logger.debug(f"\t {uuid} - Initialising class [ Coordinate ]")
        super().__init__(uuid = uuid)

        self.lati = lati 
        self.long = long

    @property
    def lati(self) -> float:
        return self._lati
    
    @property
    def long(self) -> float:
        return self._long
    
    @lati.setter
    def lati(self, obj : float) -> None:
        if not (-90 <= obj <= 90):
            raise ValueError(f"\t {self.uuid} - Invalid Latitude range provided: [{obj}]")
        self._lati = obj

    @long.setter
    def long(self, obj : float) -> None:
        if not (-180 <= obj <= 180):
            raise ValueError(f"\t {self.uuid} - Invalid Longitude range provided: [{obj}]")
        self._long = obj

    def __eq__(self, obj : object) -> bool:
        return self.lati == obj.lati and self.long == obj.long 
    
    def __ne__(self, obj : object) -> bool:
        return not self.__eq__(obj)

    def __call__(self) -> dict:
        return { "lat" : self.lati, "lon" : self.long } 

class OpenWeatherAPIRequestHandler(RequestHandlerBase):
    """
        Note: The following class is used to call the API Endpoint to obtained Weather Conditions 
        & Information based upon a specific Location
    """

    def __init__(self, uuid : str,  url : str, key : str) -> None:
        logger.info(f"\t {uuid} - Initialising class [ OpenWeatherAPIRequestHandler ]")
        super().__init__(uuid, url)

        self.key = key

    @property
    def key(self) -> str:
        return self._key
    
    @key.setter
    def key(self, obj) -> None:
        if not obj:
            raise ValueError(f"\t {self.uuid} - The parameter [key] has failed validation: [{obj}]")
        self._key = obj

    @logger.catch(reraise = True)    
    def obtain_weather(self, lati : float, long : float) -> requests.Response:
        logger.info(f"\t {self.uuid} - Calling the Open Weather API Endpoint")
        params = Coordinate(self.uuid, lati, long).__call__()
        params["appid"] = self.key

        return super()._get_request(params = params)

