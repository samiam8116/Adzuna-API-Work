# samanthaSilvia_project01_seniorDesign

Samantha Silvia

Install/run directions:
  To run this project, you need to run the file GetJobsData.py.
  When ran, you will be promted to enter a key word descirbing the job you want to search. Do this.
  To run tests, go to tests/testAPI.py and run this file.
  
Description of this project:
  This project uses an API that holds job data.
  When running GetJobsData.py, the user will be promted to enter a key word descirbing a job they would like to search for.
  When the desired key word is entered by the user, the terminal will print the names of the companies found. (20 jobs are found).
  All of the data concerning these 20 jobs will then be written to the file jobs_data.txt

Tests:
  There are two automated tests in this project (these are found in tests/testAPI.py).
  The first one tests the get_data function by checking if there are more than 0 results retreived from the API.
  The second one also tests the get_data function, but this time in the opposite way. It tests a faulty link from the API checking if there are 0 results.
  
Nothing is missing from this project
