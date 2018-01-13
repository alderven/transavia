# General information

This project contains UI tests written in Python+Selenium and [Allure Report](https://cdn.rawgit.com/alderven/transavia/master/allure-report/index.html)

# Test Cases and Test Run Results
№ | Test Script                                                                                                        | Test Description                                                                                       | Test Steps and Run Results (Allure Report)                                                                                                       | Comment
-- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1  | [test_1_one_way_ticket.py](https://github.com/alderven/transavia/blob/master/test_1_one_way_ticket.py)             | One way ticket                                                                                         | [Passed](https://cdn.rawgit.com/alderven/transavia/master/allure-report/index.html#packages/a3ba69d38a1588df4d97ea47e185269a/5aedd3359b72a51a/)  | -
2  | [test_2_total_amount.py](https://github.com/alderven/transavia/blob/master/test_2_total_amount.py)                 | Check total amount for tickets from Edinburgh to Paris for 2 adults and 1 children, hold Luggage: 20kg | [Passed](https://cdn.rawgit.com/alderven/transavia/master/allure-report/index.html#packages/d03e3e81aac0bc6b70bda7eaac05e270/d4c7307cabc0bc64/)  | -
3  | [test_3_arrival_time.py](https://github.com/alderven/transavia/blob/master/test_3_arrival_time.py)                 | Check arrival time                                                                                     | [Skipped](https://cdn.rawgit.com/alderven/transavia/master/allure-report/index.html#packages/351b9856f01f97abd8f9511be28e49bd/1a7734fcaba7b09f/) | Booking credentials (booking no. "MF8C9R"; last name "kukharau", flight date "9 June 2016") are not valid. It is not possible to create new credentials since real booking required
4  | [test_4_payment_amount.py](https://github.com/alderven/transavia/blob/master/test_4_payment_amount.py)             | Check payment amount                                                                                   | [Skipped](https://cdn.rawgit.com/alderven/transavia/master/allure-report/index.html#packages/a58fc56cd7232f12c0703e7479ab1433/365aaa548ef840e0/) | Booking credentials (booking no. "MF8C9R"; last name "kukharau", flight date "9 June 2016") are not valid. It is not possible to create new credentials since real booking required
5  | [test_5_video_link.py](https://github.com/alderven/transavia/blob/master/test_5_video_link.py)                     | Check Name and Author for "Handluggage" video instruction                                              | [Passed](https://cdn.rawgit.com/alderven/transavia/master/allure-report/index.html#packages/b99248b04f800ac967e6ca8210ac9610/3366ab0dcbca1371/)  | -
6  | [test_6_perfect_destination.py](https://github.com/alderven/transavia/blob/master/test_6_perfect_destination.py)   | Find the perfect destination from "Innsbruck, Austria" with budget less than 200 euro                  | [Passed](https://cdn.rawgit.com/alderven/transavia/master/allure-report/index.html#packages/42071b2132c680a6d649d5a041bcf547/66f122d0595f2197/)  | -
7  | [test_7_cheapest_ticket.py](https://github.com/alderven/transavia/blob/master/test_7_cheapest_ticket.py)           | Find cheapest ticket for Netherlands-France destination for specific month and day                     | [Passed](https://cdn.rawgit.com/alderven/transavia/master/allure-report/index.html#packages/0def3f1cd4fdb6ed5e62f0f242a26811/4a41675a4eea464a/)  | -
8  | [test_8_from_dubai_to_agadir.py](https://github.com/alderven/transavia/blob/master/test_8_from_dubai_to_agadir.py) | Find flight from Dubai to Agadir, Morocco (negative test)                                              | [Passed](https://cdn.rawgit.com/alderven/transavia/master/allure-report/index.html#packages/833c64f80cbf9eb7c8e4f442149dedcb/c0b6dd57e62564e5/)  | -
9  | [test_9_complicated_route.py](https://github.com/alderven/transavia/blob/master/test_9_complicated_route.py)       | Complicated route "Bologna-Eindhoven" (1st date) and "Amsterdam-Casablanca" (2nd date)                 | [Passed](https://cdn.rawgit.com/alderven/transavia/master/allure-report/index.html#packages/162b15f0e1a5cb195b02e9424a990a76/1fdf06d552eaa7e6/)  | -


# How to install
1. Download and unzip this project: https://github.com/alderven/transavia/archive/master.zip
1. Install Python 3.6 or higher: https://www.python.org/downloads/
1. Install following Python libs:
   * pytest: https://docs.pytest.org/en/latest/getting-started.html
   * selenium: https://pypi.python.org/pypi/selenium
   * allure-pytest: https://pypi.python.org/pypi/allure-pytest
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