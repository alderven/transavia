# General information

This project contains UI tests written in Python+Selenium and [Allure Report](https://cdn.rawgit.com/alderven/transavia/master/allure-report/index.html)

# Test Cases and Test Run Results
№ | Test Script                    | Test Description                                                                                       | Test Result (Link to Allure) | Comment
-- | ------------------------------ | ------------------------------------------------------------------------------------------------------ | ---------------------------- | --------
1  | test_1_one_way_ticket.py       | One way ticket                                                                                         | [Passed]()                   | -
2  | test_2_total_amount.py         | Check total amount for tickets from Edinburgh to Paris for 2 adults and 1 children, hold Luggage: 20kg | [Passed]()                   | -
3  | test_3_arrival_time.py         | Check arrival time                                                                                     | [Failed]()                   | -
4  | test_4_payment_amount.py       | Check payment amount                                                                                   | [Failed]()                   | -
5  | test_5_video_link.py           | Check Name and Author for "Handluggage" video instruction                                              | [Passed]()                   | -
6  | test_6_perfect_destination.py  | Find the perfect destination from "Innsbruck, Austria" with budget less than 200 euro                  | [Passed]()                   | -
7  | test_8_from_dubai_to_agadir.py | Find flight from Dubai to Agadir, Morocco (negative test)                                              | [Passed]()                   | -
8  | test_9_complicated_route.py    | Complicated route "Bologna-Eindhoven" (1st date) and "Amsterdam-Casablanca" (2nd date)                 | [Passed]()                   | -


# How to install
1. Download and unzip this project: https://github.com/alderven/transavia/archive/master.zip
1. Install Python 3.6 or higher: https://www.python.org/downloads/
1. Install following Python libs:
   * pytest: https://docs.pytest.org/en/latest/getting-started.html
   * selenium: https://pypi.python.org/pypi/selenium
   * pytest-allure-adaptor: https://pypi.python.org/pypi/pytest-allure-adaptor
   * names: https://pypi.python.org/pypi/names/
   * configparser: https://pypi.python.org/pypi/configparser
1. Download and unzip Edge driver to the project root folder:
   https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads
1. Install Allure Framework. See detailed instruction: https://docs.qameta.io/allure/latest/


# How to run tests
Execute following line in CMD in the project folder:
```
python -m pytest --alluredir /full/path/to/report/folder
```

# How to generate Allure report
Execute following line in CMD in the project folder:
```
allure serve /full/path/to/report/folder
```