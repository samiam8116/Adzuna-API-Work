# samanthaSilvia_project01_seniorDesign

Samantha Silvia

Install/run directions:
  To run this project, you need to run the file displayData.py.
  When ran, a GUI will pop up and will prompt you for three filters: technology, location, and salary minimum.
  Once you have entered these three filters, the jobs that fit them will display in a list.
  To show more information about a certain job, you just need to double click on the desired job and a pop up message box will appear displaying more information.
  The jobs that were found will be sent to a database (jobs.db).
  To run tests, go to tests/testAPI.py and run this file.
  
Description of this project:
  This project uses an API that holds job data.
  When running displayData.py, a user interface will guide you through the process of filtering jobs tailored to what you want to retrieve.
  As well as filtering, more information can be found about each job by simply double clicking on the desired job in the list.
  The job data will also go into the database (newJobs.db).

Tests:
  There are several automated tests in this project (these are found in tests/testAPI.py).
  The first one, test_get_data(), tests the get_data function by checking if there are more than 0 results retrieved from the API.
  The second test, test_if_table_exists(), tests if the database exists. It counts the number of tables from the file newJobs.db, and if that count is  <= 1, it tells you that the table exists.
  The third test, test_good_data(), tests if good data is going into the database. I pronounced "good data" as data that has an ID that is numerical. To test this, I had the test go through the jobs and using the isdigit() function I had it find out if the ID's from the API were numerical or not. If they were, the test will print "the id is valid".
  The fourth test, test_bad_data(), tests if bad data is going into the database. I pronounced "bad data" as data that has an ID that is not numerical. To test this, I had the test go through the jobs and using the isdigit() function I had it find out if the ID's from the API were numerical or not. If they were not numerical, the test will print "the id is not valid".

Not Finished:
   I tried my absolute best with this sprint, however, I did not achieve everything that I had hoped for.
   What is unfinished is:
    1. When you double click on a job to show more information, the only information shown is the title of the job. I could not figure out how to grab more of the job's data since I was just SQL selecting the title. I struggled with this problem a lot!
    2. I do not have the tests for the filtering. I was unsure of how to reference the user input and use it in this test...
    
   In summary, this project is close to being finished, but some aspects I was never able to fully grasp.
    
