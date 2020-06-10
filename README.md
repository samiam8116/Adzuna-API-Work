# samanthaSilvia_project01_seniorDesign

Samantha Silvia

Install/run directions:
  To run this project, you need to run the file GetJobsData.py.
  When ran, the program will randomly choose one of the eight keywords and search for jobs with that key word.
  The jobs that were found will be sent to a database (jobs.db).
  To run tests, go to tests/testAPI.py and run this file.
  
Description of this project:
  This project uses an API that holds job data.
  When running GetJobsData.py, it will randomly choose one of the eight keywords provided and search for jobs with that chosen key word.
  The job data will go into the database (jobs.db) and the terminal will print the names of the companies found.

Tests:
  There are several automated tests in this project (these are found in tests/testAPI.py).
  The first one, test_get_data(), tests the get_data function by checking if there are more than 0 results retrieved from the API.
  The second test, test_if_table_exists(), tests if the database exists. It counts the number of tables from the file jobs.db, and if that count is  <= 0, it tells you that the table exists.
  The third test, test_good_data(), tests if good data is going into the database. I pronounced "good data" as data that has an ID that is numerical. To test this, I had the test go through the jobs and using the isdigit() function I had it find out if the ID's from the API were numerical or not. If they were, the test will print "the id is valid".
  The fourth test, test_bad_data(), tests if bad data is going into the database. I pronounced "bad data" as data that has an ID that is not numerical. To test this, I had the test go through the jobs and using the isdigit() function I had it find out if the ID's from the API were numerical or not. If they were not numerical, the test will print "the id is not valid".

Nothing is missing from this project
