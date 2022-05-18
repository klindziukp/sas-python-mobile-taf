pytest --alluredir=build/allure-results test/test_suite_smoke.py --testrail --tr-config=testrail.cfg
allure generate build/allure-results --clean -o build/allure-report
