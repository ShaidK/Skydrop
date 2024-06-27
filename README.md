**INTEGRATION**

The Skydrop Project is a Python Module which is used to obtained Weather 
Conditions & Information based upon a specific Airports Locations

The Project itself is written within Python & can be imported within 
specific Python Projects

**DESCRIPTION**

The Skydrop Project mainly uses the [Open Weather API](https://openweathermap.org/api) 
to obtained Weather Conditions based on a given Longitude & Latitude coordinate

It uses the API known as `Current Weather Data` to obtained Weather Conditions at 
the current moment of time

```
API Endpoint:   https://api.openweathermap.org/data/2.5/weather

Parameters 
- appid         Paramater used to authenticate the API Call
- lon           Location Longitude Coordinate
- lat           Location Latitude  Coordinate           
```

**PROJECT STRUCTURE**

The following displays the directory structure of the Skydrop Project

```
skydrop
|
|   .gitattributes
|   .gitignore
|   .pylintrc
|   CHANGELOG
|   LICENSE
|   README.md
|   pyproject.toml
|   requirements.txt
|
├─── .github
|        workflows
|            build-pipeline.yaml
|
├─── .vscode
|        settings.json
|        launch.json
|        tasks.json
|
├─── skydrop
|        __init__.py
|        error.py
|        base.py
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
astroid==3.2.2
build==1.2.1
certifi==2024.2.2
charset-normalizer==3.3.2
coverage==7.5.3
decorator==5.1.1
dill==0.3.8
idna==3.7
isort==5.13.2
loguru==0.7.2
mccabe==0.7.0
packaging==24.0
parameterized==0.9.0
platformdirs==4.2.2
py==1.11.0
pylint==3.2.2
pyproject_hooks==1.1.0
python-dotenv==1.0.1
PyYAML==6.0.1
requests==2.32.2
responses==0.25.0
retry==0.9.2
tomli==2.0.1
tomlkit==0.12.5
typing_extensions==4.12.1
urllib3==2.2.2
validators==0.28.1
```

**PROJECT BUILD**

The Skydrop Project has been automated to execute linting, testing, coverage &
packaging of the Python Files using the `vscode` file [`tasks.json`](https://code.visualstudio.com/docs/editor/tasks)

This can be executed using the following Keyboard Shortcut when Project is open
within Visual Studio Code: `CTRL` + `SHIFT` + `B`

**TESTING**

The Skydrop Project has set of Unit & Integration Test Suites to confirm the 
functionality of the Project.

The Integration Test Suite need to be configured by creating the File `.env` 
at the root directory.

Within this File you need to configured the [Open Weather API](https://openweathermap.org/api) 
URI & API Key as shown in the following in order to successfully run the 
Integration Test:

```
OPEN_WEATHER_API_URL="https://api.openweathermap.org/data/2.5/weather?"
OPEN_WEATHER_API_KEY="<OPEN_WEATHER_API_KEY>"
```

**PROJECT CI PIPELINE**

The Skydrop Project has been configured to run a Continous Integration 
Pipeline to build the Project during Pull Request or pushes to the 
Branch: `build` 

The Build Pipeline will execute the following set of steps:

- _Download Project Repository_
  - _This checkout the Skydrop Project repository within the GitHub Hosted agents_

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