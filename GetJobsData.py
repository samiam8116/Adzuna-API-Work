import requests
import sqlite3
import random


# print company name to terminal
def display_data(to_display):
    for job in to_display:
        print(job['company'].get('display_name'))


# write all data to file "jobs_data.txt"
def write_data(data, filename='jobs_data.txt'):
    with open(filename, 'w') as file:
        for job in data:
            print(job, file=file)


def get_data():
    key_word = ['python', 'java', 'golang', 'javascript', 'devops', 'database', 'web', 'design']
    results = []
    for term in key_word:
        location = f"http://api.adzuna.com/v1/api/jobs/us/search/1?app_id=18381bc0&app_key=f20a9d4e1c0d42e8d120af190ecfb44d" \
               f"&results_per_page=20&what={random.choice(key_word)}"
        response = requests.get(location)
        if response.status_code != 200:
            continue
        data = response.json()
        print(location)
        for item in data["results"]:
            results.append(item)
    return results


def save_data(jobs: list, cursor: sqlite3.Cursor):
    for job in jobs:
        cursor.execute("INSERT INTO jobs(title, category, company, location, description) VALUES(?,?,?,?,?);",
                       [job['title'], job['category'].get('label'), job['company'].get('display_name'),
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
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()
    setup_database(cursor)
    data = get_data()
    save_data(data, cursor)
    connection.commit()
    connection.close()
    display_data(data)
    write_data(data, "jobs_data.txt")


if __name__ == '__main__':
    main()
