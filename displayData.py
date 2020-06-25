from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import sqlite3
import sys


class JobWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QtWidgets.QHBoxLayout()

        self.list_control = QtWidgets.QListWidget()
        main_layout.addWidget(self.list_control)

        data_display_layout = QtWidgets.QVBoxLayout()
        main_layout.addItem(data_display_layout)

        self.list_control.itemClicked.connect(self.clicked_item)

        self.setLayout(main_layout)

    def display_data(self, job_data: list):
        for job in job_data:
            current_item = QtWidgets.QListWidgetItem(job[0], self.list_control)
            current_item.setData(Qt.UserRole, job[0])

    def clicked_item(self):
        QMessageBox.information(self, "More Information", "Job Title: " + self.list_control.currentItem().text())


def get_filtered_data(cursor: sqlite3.Cursor):
    # FILTER #1: TECHNOLOGY --------------------------------------------------------------
    technologies, technologies_ok = QtWidgets.QInputDialog.getText(None, "Choose Technology",
                                                                   "Choose a technology term to filter data")
    # FILTER #2: LOCATION ----------------------------------------------------------------
    locations, locations_ok = QtWidgets.QInputDialog.getText(None, "Choose Location",
                                                             "Choose a location to filter data")
    # FILTER #3: COMPANY -----------------------------------------------------------------
    salary_mins, salary_mins_ok = QtWidgets.QInputDialog.getText(None, "Choose Salary Minimum",
                                                                 "Choose a salary minimum to filter data")

    sql_select = f"SELECT title FROM newJobs WHERE title LIKE '%{technologies}%' OR location LIKE '%{locations}%' OR " \
                 f"salary_min > '%{salary_mins}%';"

    results = cursor.execute(sql_select)
    return results


def main():
    app = QApplication(sys.argv)
    connection = sqlite3.connect("newJobs.db")
    cursor = connection.cursor()
    newJobs = get_filtered_data(cursor)
    window = JobWindow()
    window.display_data(newJobs)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
