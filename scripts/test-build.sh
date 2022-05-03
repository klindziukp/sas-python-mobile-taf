pytest --alluredir=build/allure-results test/test_suite_smoke.py
allure generate build/allure-results --clean -o build/allure-report
