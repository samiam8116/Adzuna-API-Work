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
  There are two automated tests in this project (these are found in tests/testAPI.py).
  The first one tests the get_data function by checking if there are more than 0 results retreived from the API.
  The second one also tests the get_data function, but this time in the opposite way. It tests a faulty link from the API checking if there are 0 results.
  
Nothing is missing from this project
