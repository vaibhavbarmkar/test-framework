# Test automation framework

## UI automation framework using Pytest+ selenium

### Features

- Web Automation using page object model
- Logger
- Screenshot on failure
- Parallel execution of test cases
- Externalised configuration
- API calling support 

### Tech
- Python 
- pytest
- selenium

### Installation

#### Prerequisite
- Python 3.7 or above should be installed on the system

#### Setup
- Install pipenv package using *pip install pipenv*
- Navigate to project folder and run "pipenv install"


#### How to run

- Run "pipenv shell" 
- Add required configuration in the .env file
- Run command ``` pytest -s -v``` to execute tests. on default browser and sequentially
- Run command ``` BROWSER=firefox pytest -s -v``` to execute tests on provided browser and sequentially
- Run command ``` pytest -s -v --workers 2``` to execute tests parallel with multiple processes. refer https://pypi.org/project/pytest-parallel/ for more details




