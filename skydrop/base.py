#!/usr/bin/env python

"""
    DESCRIPTION
        The following Module contains the base classes which are used within the Skydrop
        Project

    FILE
        base.py

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
# File: base.py | Note: The following file is used to maintain the Base Classes within the Project
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
from skydrop import dataclass, logger

from retry import retry

import validators, requests

@dataclass
class EntityBase:
    """
        DESCRIPTION
            The following class is used to represent the base class which is used to retains 
            the uuid

        ATTRIBUTES
            uuid : <str>
                The unique id which is used to aggregate application logs
    """
    uuid : str

class DatasourceBase(EntityBase):
    """
        DESCRIPTION
            The following class is used to represent the base class to obtained data from an
            External Datasource
    """

    def __init__(self, uuid : str):
        """
            DESCRIPTION
                Initialise the DatasourceBase with a unique uuid 

            PARAMETER
                uuid : <str>
                    The unique id which is used to aggregate application logs 
        """
        super().__init__(uuid)

class RequestHandlerBase(EntityBase):
    """
        DESCRIPTION
            The following class is used to represent the base class which is used to call
            the External API

        PROPERTIES
            url : <str>
                The following string represent the url of the External API
    """

    @logger.catch(reraise = True)
    def __init__(self, uuid : str, url : str) -> None:
        """
            TODO: Function docstring will be written within the next commit
        """
        logger.debug(f"\t {uuid} - Initialising class [ RequestHandlerBase ]")
        super().__init__(uuid = uuid)

        self.url = url

    @property
    def url(self) -> str:
        """
            TODO: Function docstring will be written within the next commit
        """
        return self._url

    @url.setter
    def url(self, obj : str) -> None:
        """
            TODO: Function docstring will be written within the next commit
        """
        if not validators.url(obj):
            raise ValueError(f"\t {self.uuid} - The parameter [url] has failed validation: [{obj}]")
        self._url = obj

    @retry((requests.ConnectTimeout), tries = 5, delay = 2, backoff = 5)
    @logger.catch(reraise = True)
    def _get_request(self, params : dict = None, **kwargs) -> requests.Response:
        """
            TODO: Function docstring will be written within the next commit
        """
        logger.debug(f"\t {self.uuid} - Calling the External API: [ {self._url} ]")
        try:
            response = requests.get(url = self._url, params = params, timeout = 10, **kwargs)
            response.raise_for_status()
        except requests.HTTPError as http_err:
            raise APIRequestError(self.uuid, http_err.response.status_code) from http_err

        return response
