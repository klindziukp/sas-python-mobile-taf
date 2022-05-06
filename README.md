# sas-python-mobile-taf

## INSTALLATION
#### INSTALL PYTHON
- Download python from [here](https://www.python.org/downloads/)
#### INSTALL PYTEST
```bash
pip install pytest
```
#### INSTALL ALLURE
 ```bash
pip install allure-pytest
```
#### INSTALL APPIUM
- Download appium  from [here](https://appium.io/docs/en/about-appium/getting-started/?lang=en#installing-appium)

#### INSTALL APPIUM INSPECTOR
- Download appium inspector  from [here](https://github.com/appium/appium-inspector)

#### INSTALL ANDROID STUDIO
- Download Android studio  from [here](https://github.com/appium/appium-inspector)

### TEST SCRIPTS EXECUTION

#### Single test execution
 Just execute `shell` script
 ```bash
pytest --alluredir=build/allure-results test/test_main_page.py
```
#### Suite test script execution
 Just execute `shell` script
 ```bash
pytest --alluredir=build/allure-results test/test_suite_smoke.py
````
