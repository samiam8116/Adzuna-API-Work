from tkinter.tix import Form

import requests
import sqlite3
import random
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFormLayout
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtWidgets


class FilterWindow(QWidget):

    def __init__(self, to_display):
        super().__init__()

        layout = QFormLayout()
        self.data_to_display = to_display
        self.data_item_displayed = 0

        # TECHNOLOGY FILTER
        self.technology_filter_button = QPushButton("Technology Filter")
        self.technology_filter_button.clicked.connect(self.get_technology)
        self.technology_line_edit = QLineEdit()
        layout.addRow(self.technology_filter_button, self.technology_line_edit)

        # FIND TECHNOLOGY JOBS - switch to technology window
        self.technology_apply_button = QtWidgets.QPushButton('Apply Technology Filter')
        self.technology_apply_button.clicked.connect(self.technology_window)
        layout.addWidget(self.technology_apply_button)

        # LOCATION FILTER
        self.location_filter_button = QPushButton("Location Filter")
        self.location_filter_button.clicked.connect(self.get_location)
        self.location_line_edit = QLineEdit()
        layout.addRow(self.location_filter_button, self.location_line_edit)

        # FIND LOCATION JOBS - switch to location window
        self.location_apply_button = QtWidgets.QPushButton('Apply Location Filter')
        self.location_apply_button.clicked.connect(self.location_window)
        layout.addWidget(self.location_apply_button)

        # COMPANY FILTER
        self.company_filter_button = QPushButton("Company Filter")
        self.company_filter_button.clicked.connect(self.get_company)
        self.company_line_edit = QLineEdit()
        layout.addRow(self.company_filter_button, self.company_line_edit)

        # FIND COMPANY JOBS - switch to company window
        self.company_apply_button = QtWidgets.QPushButton('Apply Company Filter')
        self.company_apply_button.clicked.connect(self.company_window)
        layout.addWidget(self.company_apply_button)

        self.setLayout(layout)
        self.setWindowTitle("Filter Window")

    # GET USER INPUT FOR FILTERS
    def get_technology(self):
        technology_input, ok = QInputDialog.getText(self, 'Location Filter', 'Enter location:')
        if ok:
            self.technology_line_edit.setText(str(technology_input))

    def get_location(self):
        location_input, ok = QInputDialog.getText(self, 'Location Filter', 'Enter location:')
        if ok:
            self.location_line_edit.setText(str(location_input))

    def get_company(self):
        company_input, ok = QInputDialog.getText(self, "Company Filter", "Enter company")
        if ok:
            self.company_line_edit.setText(str(company_input))

    # OPEN NEW WINDOWS FOR EACH FILTER
    def technology_window(self):
        technology_window = QDialog(self)
        technology_window.show()

    def location_window(self):
        location_window = QDialog(self)
        location_window.show()

    def company_window(self):
        company_window = QDialog(self)
        company_window.show()


# print company name to terminal
def display_data(to_display):
    # for job in to_display:
    #     print(job['company'].get('display_name'))

    window = FilterWindow(to_display)
    return window


# write all data to file "jobs_data.txt"
def write_data(data, filename='jobs_data.txt'):
    with open(filename, 'w') as file:
        for job in data:
            print(job, file=file)


def get_data():
    # key_word = ['python', 'java', 'golang', 'javascript', 'devops', 'database', 'web', 'design'] location =
    # f"http://api.adzuna.com/v1/api/jobs/us/search/1?app_id=18381bc0&app_key=f20a9d4e1c0d42e8d120af190ecfb44d" \
    # f"&results_per_page=20&what={random.choice(key_word)}"

    # key_word = input("What key word do you want to search for?:") location =
    # f"http://api.adzuna.com/v1/api/jobs/us/search/1?app_id=18381bc0&app_key=f20a9d4e1c0d42e8d120af190ecfb44d" \
    # f"&results_per_page=20&what={key_word}"

    location = f"http://api.adzuna.com/v1/api/jobs/us/search/1?app_id=18381bc0&app_key=f20a9d4e1c0d42e8d120af190ecfb44d" \
               f"&results_per_page=20"
    response = requests.get(location)
    if response.status_code != 200:
        return []
    data = response.json()
    print(location)
    return data["results"]


def save_data(jobs: list, cursor: sqlite3.Cursor):
    for job in jobs:
        cursor.execute("INSERT OR IGNORE INTO jobs(id, title, category, company, location, description) VALUES(?,?,?,"
                       "?,?,?);",
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


def main():
    app = QApplication(sys.argv)
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()
    setup_database(cursor)
    data = get_data()
    save_data(data, cursor)
    connection.commit()
    connection.close()
    display_data(data)
    write_data(data, "jobs_data.txt")
    window = display_data(data)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
