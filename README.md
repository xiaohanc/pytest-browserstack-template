# pytest-browserstack-template
A template for cross-browser testing with pytest and browserstack, implemented allure report, download allure and run `allure serve` would have report displaying, also could be integrated with CI(Jenkins, Circleci, etc) and Jira.


## Command Line Examples
`Pytest_addopption` paser flag B in pytest command line, default without B flag will run test on local, if run parameter with B, template will used `pytest_generate_tests` to parametrize the device and generate multiple tests on different platforms with broserstack executor.

**Locally**
`pytest smoke/test_*.py`

**Mobile**
`pytest smoke/test_*.py -v -B mobile`

**Web**
`pytest smoke/test_*.py -v -B web`

**Specific browsers**
`pytest smoke/test_*.py -v -B <specific platform-browser>`

**With allure report**
`pytest smoke/test_*.py --alluredir=test-report`

## Usage
test sample stored in smoke/test_sample.py, contains some very basic usage like parametrize, selenium, pytest-allure and so on.
