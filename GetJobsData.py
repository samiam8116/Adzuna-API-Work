import requests
import sqlite3
import sys
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets


class JobWindow(QWidget):
    def __init__(self, to_display):
        super().__init__()
        self.data_to_display = to_display
        self.data_item_displayed = 0
        current_data = self.data_to_display[self.data_item_displayed]
        layout = QFormLayout()
        filters_caption = QLabel("Filters:")
        layout.addRow(filters_caption)

        # TECHNOLOGY FILTER
        self.technology_filter_button = QPushButton("Technology Filter")
        self.technology_filter_button.clicked.connect(self.get_technology)
        self.technology_line_edit = QLineEdit()
        layout.addRow(self.technology_filter_button, self.technology_line_edit)

        # LOCATION FILTER
        self.location_filter_button = QPushButton("Location Filter")
        self.location_filter_button.clicked.connect(self.get_location)
        self.location_line_edit = QLineEdit()
        layout.addRow(self.location_filter_button, self.location_line_edit)

        # COMPANY FILTER
        self.company_filter_button = QPushButton("Company Filter")
        self.company_filter_button.clicked.connect(self.get_company)
        self.company_line_edit = QLineEdit()
        layout.addRow(self.company_filter_button, self.company_line_edit)

        # Button to start search with filters
        self.apply_filters = QPushButton("Apply Filters")
        # self.apply_filters.clicked.connect(??????)
        layout.addRow(self.apply_filters)

        # Jobs are displayed in this line edit
        jobs_caption = QLabel("Jobs:")
        layout.addRow(jobs_caption)
        title_caption = QLabel("Title:")
        self.job_title = QLineEdit()
        self.job_title.setReadOnly(True)
        self.job_title.setFixedWidth(500)
        self.job_title.setText(current_data['title'])
        layout.addRow(title_caption, self.job_title)

        # Get more information
        get_more_info = QPushButton("Get More Information")
        self.job_description = QLineEdit()
        self.job_description.setReadOnly(True)
        self.job_description.setFixedWidth(500)
        layout.addRow(get_more_info, self.job_description)

        # Get next job
        get_next_job = QPushButton("Get Next Job")
        layout.addRow(get_next_job)

        # Button presses
        get_more_info.pressed.connect(self.show_more_information)
        get_next_job.pressed.connect(self.show_next_job)

        self.setLayout(layout)
        self.setWindowTitle("Job Search")

    def show_next_job(self):
        self.data_item_displayed += 1
        current_data = self.data_to_display[self.data_item_displayed]
        self.job_title.setText(current_data['title'])

    def show_more_information(self):
        self.data_item_displayed += 1
        current_data = self.data_to_display[self.data_item_displayed]
        self.job_description.setText(current_data['description'])

    def get_data_extension(self):
        # technology input
        technology_input, ok = QInputDialog.getText(self, 'Location Filter', 'Enter location:')
        if ok:
            self.technology_line_edit.setText(str(technology_input))
            return technology_input

        # location input
        location_input, ok = QInputDialog.getText(self, 'Location Filter', 'Enter location:')
        if ok:
            self.location_line_edit.setText(str(location_input))

        # company input
        company_input, ok = QInputDialog.getText(self, "Company Filter", "Enter company")
        if ok:
            self.company_line_edit.setText(str(company_input))

        return technology_input, location_input, company_input

        # Put user input into the URL
        loc = f"https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=18381bc0&app_key=f20a9d4e1c0d42e8d120af190ecfb44d" \
              f"&results_per_page=20&what={technology_input}&where={location_input}&salary_min={company_input}"

        # Call get_data() with that user input to retrieve the API data
        get_data(loc)

    # GET USER INPUT FOR FILTERS
    def get_technology(self):
        technology_input, ok = QInputDialog.getText(self, 'Location Filter', 'Enter location:')
        if ok:
            self.technology_line_edit.setText(str(technology_input))
            return technology_input

    def get_location(self):
        location_input, ok = QInputDialog.getText(self, 'Location Filter', 'Enter location:')
        if ok:
            self.location_line_edit.setText(str(location_input))
            return location_input

    def get_company(self):
        company_input, ok = QInputDialog.getText(self, "Company Filter", "Enter company")
        if ok:
            self.company_line_edit.setText(str(company_input))
            return company_input


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


def save_data(jobs: list, cursor: sqlite3.Cursor):
    for job in jobs:
        cursor.execute("INSERT OR IGNORE INTO jobs(id, title, category, company, location, description) "
                       "VALUES(?,?,?,?,?,?);",
                       [job['id'], job['title'], job['category'].get('label'), job['company'].get('display_name'),
                        job['location'].get('display_name'), job['description']])


def setup_database(cursor: sqlite3.Cursor):
    create_statement = """CREATE TABLE IF NOT EXISTS jobs (
    id TEXT PRIMARY KEY,
    category TEXT,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    location TEXT,
    description TEXT);"""
    cursor.execute(create_statement)


# def get_params():
#     technology = input("what technology?:")
#     location = input("what location?:")
#     salary_min = input("salary minimum?:")
#     return technology, location, salary_min


# def stuff():
#     loc = f"https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=18381bc0&app_key=f20a9d4e1c0d42e8d120af190ecfb44d" \
#           f"&results_per_page=20&what={params[0]}&where={params[1]}&salary_min={params[2]}"
#     print(loc)
#     data = get_data(loc)
#     save_data(data, cursor)


def main():
    app = QApplication(sys.argv)
    # params = get_params()
    loc = f"https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=18381bc0&app_key=f20a9d4e1c0d42e8d120af190ecfb44d" \
          f"&results_per_page=20&what={JobWindow.get_technology}&where={JobWindow.get_location}&salary_min={JobWindow.get_company}"
    print(loc)
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()
    setup_database(cursor)
    data = get_data(loc)
    save_data(data, cursor)
    connection.commit()
    connection.close()
    write_data(data, "jobs_data.txt")
    window = display_data(data)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
