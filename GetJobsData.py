import requests
import sqlite3
import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication


class JobWindow(QWidget):
    def __init__(self, to_display):
        super().__init__()
        self.data_to_display = to_display
        self.data_item_displayed = 0


def display_data(to_display):
    window = JobWindow(to_display)
    return window


# write all data to file "jobs_data.txt"
def write_data(data, filename='jobs_data.txt'):
    with open(filename, 'w') as file:
        for job in data:
            print(job, file=file)


def get_data(location):
    response = requests.get(location)
    if response.status_code != 200:
        return []
    data = response.json()
    return data["results"]


def save_data(newJobs: list, cursor: sqlite3.Cursor):
    for job in newJobs:
        cursor.execute("INSERT OR IGNORE INTO newJobs(id, title, category, company, location, description, salary_min) "
                       "VALUES(?,?,?,?,?,?,?);",
                       [job['id'], job['title'], job['category'].get('label'), job['company'].get('display_name'),
                        job['location'].get('display_name'), job['description'], job['salary_min']])


def setup_database(cursor: sqlite3.Cursor):
    create_statement = """CREATE TABLE IF NOT EXISTS newJobs (
    id TEXT PRIMARY KEY,
    category TEXT,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    location TEXT,
    description TEXT,
    salary_min INTEGER);"""
    cursor.execute(create_statement)


def main():
    app = QApplication(sys.argv)
    data = []
    technology = ["java", "python", "javascript", "web", "design", "c", "code", "program"]
    location = ["london", "boston", "chicago", "berlin", "detroit", "paris"]
    salary_minimum = ["10000", "50000", "80000", "100000"]
    for tech in technology:
        for loc in location:
            for sal in salary_minimum:
                loc = f"https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=18381bc0&app_key" \
                      f"=f20a9d4e1c0d42e8d120af190ecfb44d" \
                      f"&results_per_page=20&what={tech}&where={loc}&salary_min={sal}"
                print(loc)
                data.extend(get_data(loc))
    connection = sqlite3.connect("newJobs.db")
    cursor = connection.cursor()
    setup_database(cursor)
    save_data(data, cursor)
    connection.commit()
    connection.close()
    write_data(data, "jobs_data.txt")
    window = display_data(data)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
