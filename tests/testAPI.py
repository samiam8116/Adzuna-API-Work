import pytest
import sqlite3
import GetJobsData


@pytest.fixture
def grab_data():
    return GetJobsData.get_data()


# test get_data() function
def test_get_data():
    data = GetJobsData.get_data()
    assert len(data) > 0


# test if the table called "jobs" exists
def test_if_table_exists():
    connection = sqlite3.connect("newJobs.db")
    cursor = connection.cursor()

    # get the count of tables
    cursor.execute(''' SELECT count(*) FROM sqlite_master WHERE type='table' AND name LIKE 'newJobs'; ''')
    # if count <= 1, then the table exists
    if cursor.fetchone()[0] <= 1:
        print('Table exists.')
    else:
        print('Table does not exist.')

    # commit the changes to db
    connection.commit()
    # close the connection
    connection.close()


# test if good data goes into the database
# (I am declaring that "good data" has an ID that is an integer)
def test_good_data(grab_data):
    jobs = grab_data
    has_valid_id = False
    # check though all jobs - if their ID is numerical has_valid_id is True
    for job in jobs:
        if job['id'].isdigit():
            has_valid_id = True
            print('The ID is valid')
    assert has_valid_id


# test if bad data goes into the database
# (I am declaring that "bad data" has an ID that is NOT an integer)
def test_bad_data(grab_data):
    jobs = grab_data
    does_not_have_valid_id = False
    # check though all jobs - if their ID is not numerical does_not_have_valid_id is True
    for job in jobs:
        if job['id'].isdigit():
            does_not_have_valid_id = True
            print('The ID is not valid')
    assert does_not_have_valid_id
