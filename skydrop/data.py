#!/usr/bin/env python

"""
    DESCRIPTION
        The following Module contains classes which are used to obtained Airport Information
        from OpenAirportDatasource

    FILE
        data.py

    AUTHOR
        Shaid Khan

    LICENSE
        MIT License

        Copyright (c) 2024 Shaid Khan

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.
"""

#
# File: data.py | Note: The following class is used to obtained data from a Datasource
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

from skydrop.error import InvalidAirportCodeError
from skydrop.base import DatasourceBase
from skydrop.entity import Airport

import re

class OpenAirportDatasource(DatasourceBase):
    """
        DESCRIPTION
            The following class is used to obtained Airport Information from an External Azure 
            Cosmos Datasource 
    """

    def __init__(self, uuid : str):
        """
            DESCRIPTION
                Initialise the OpenAirportDatasource with a unique uuid 

            PARAMETER
                uuid : <str>
                    The unique id which is used to aggregate application logs 
        """
        super().__init__(uuid)

    def get_airport_by_iata(self, iata : str) -> Airport:
        """
            TODO: Function docstring will be written within the next commit
        """
        if not bool(re.match(Airport.IATA_REGEX_PATTERN, iata)):
            raise InvalidAirportCodeError(uuid = self.uuid, airport_code = iata)
     
    def get_airport_by_icao(self, icao : str) -> Airport:
        """
            TODO: Function docstring will be written within the next commit
        """
        if not bool(re.match(Airport.ICAO_REGEX_PATTERN, icao)):
            raise InvalidAirportCodeError(uuid = self.uuid, airport_code = icao)
