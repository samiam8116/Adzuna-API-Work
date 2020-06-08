# import pytest
# import sqlite3

import GetJobsData


def test_get_data():
    test_location = "http://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=18381bc0&app_key" \
                    "=f20a9d4e1c0d42e8d120af190ecfb44d&results_per_page=20&what=javascript%20developer&content-type" \
                    "=application/json"
    test_results = GetJobsData.get_data(test_location)
    # if there are more than 0 results ...
    assert len(test_results) > 0


def test_get_bad_data():
    test_location = "http://api.adzuna.com/v1/apidev/jobs/gb/search/1?app_id=18381bc0&app_key" \
                    "=f20a9d4e1c0d42e8d120af190ecfb44d&results_per_page=20&what=javascript%20developer&content-type" \
                    "=application/json"
    test_results = GetJobsData.get_data(test_location)
    assert type(test_results) == list
    assert len(test_results) == 0
