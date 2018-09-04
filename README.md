
[![Build Status](https://travis-ci.org/mianusmankhalid/AppiumTestsWithPythonClient.svg?branch=master)](https://travis-ci.org/mianusmankhalid/AppiumTestsWithPythonClient)

# Appium tests with python-client

This project is mainly focused to test android application with appium via Appium-Python-Client and to create CI/CD pipeline using travis

## Prerequisites

For testing on local machine

```
Run Appium Server
Start Android Virtual Device
```

in case of travis pipeline you don't need to run Appium Server and start AVD on your machine

## Requirement

you just need an apk file to run your tests

## Running the tests

you can write down your tests in .py file and can run tests locally via

```
pytest MovieAppTest.py
```

for travis you can change testing file name under script tag in .travis.yml file

### Things involve in this project :

1. appium 
2. appium-doctor
3. Appium-Python-Client
4. travis
5. Appium Server
6. Android SDK 

