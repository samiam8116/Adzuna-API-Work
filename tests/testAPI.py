import pytest
import sqlite3
import GetJobsData


@pytest.fixture
def grab_data():
    technology = ["java", "python", "javascript", "web", "design", "c", "code", "program"]
    location = ["london", "boston", "chicago", "berlin", "detroit", "paris"]
    salary_minimum = ["10000", "50000", "80000", "100000"]
    for tech in technology:
        for loc in location:
            for sal in salary_minimum:
                loc = f"https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=18381bc0&app_key" \
                      f"=f20a9d4e1c0d42e8d120af190ecfb44d" \
                      f"&results_per_page=20&what={tech}&where={loc}&salary_min={sal}"
                return GetJobsData.get_data(loc)


# test get_data() function
def test_get_data():
    technology = "python"
    location = "london"
    salary_minimum = "10000"
    loc = f"https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=18381bc0&app_key" \
          f"=f20a9d4e1c0d42e8d120af190ecfb44d" \
          f"&results_per_page=20&what={technology}&where={location}&salary_min={salary_minimum}"
    data = GetJobsData.get_data(loc)
    assert len(data) > 0


# test if the table called "newJobs" exists
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
