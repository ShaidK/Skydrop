**INTEGRATION**

_The Skydrop Project is a Python Module which is used to obtained Weather 
Conditions & Information based upon a specific Airports Locations_

_The Project itself is written within Python & can be imported within 
specific Python Projects_

**DESCRIPTION**

_The Skydrop Project mainly uses the Open Weather API to obtained Weather 
Conditions based on a given Longitude & Latitude coordinate_

_It uses the Open Weather API known as `Current Weather Data` to obtained 
Weather Conditions at the current moment of time_

```
API Endpoint:   https://api.openweathermap.org/data/2.5/weather

Parameters 
- appid         Paramater used to authenticate the API Call
- lon           Location Longitude Coordinate
- lat           Location Latitude  Coordinate           
```

**PROJECT STRUCTURE**

_The following displays the directory structure of the Skydrop Project_

```
skydrop
|
|   .gitattributes
|   .gitignore
|   CHANGELOG
|   LICENSE
|   README.md
|   pyproject.toml
|   requirements.txt
|
├─── skydrop
|        __init__.py
|        error.py
|        api.py
|
└─── test
         res
             open_api_success.json
         __init__.py
         test_api.py
```

**PROJECT DEPENDENCIES**

_The following Project Dependencies are required for the Skydrop Project in 
order to execute & run the Project:_

```
certifi==2024.2.2
charset-normalizer==3.3.2
decorator==5.1.1
idna==3.7
loguru==0.7.2
parameterized==0.9.0
py==1.11.0
python-dotenv==1.0.1
PyYAML==6.0.1
requests==2.32.2
responses==0.25.0
retry==0.9.2
urllib3==2.2.1
validators==0.28.1
```

**TESTING**

_The Skydrop Project has set of Unit & Integration Test Suites to confirm the 
functionality of the Project._

_The Integration Test Suite need to be configured by creating the File `.env` 
at the root directory._

_Within this File you need to configured the Open Weather API URI & API Key
as shown in the following in order to successfully run the Integration Test:_

```
OPEN_WEATHER_API_URL="https://api.openweathermap.org/data/2.5/weather?"
OPEN_WEATHER_API_KEY="<OPEN_WEATHER_API_KEY>"
```

**LICENSE**

```
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
```