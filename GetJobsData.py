import requests
# test


# print company name to terminal
def display_data(to_display):
    for company in to_display:
        print(company['company'].get('display_name'))


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


def get_params():
    key_word = input("What key word do you want to search for?:")
    return key_word


def main():
    params = get_params()
    loc = f"http://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=18381bc0&app_key=f20a9d4e1c0d42e8d120af190ecfb44d" \
          f"&results_per_page=20&what={params} "
    print(loc)
    data = get_data(loc)
    display_data(data)
    write_data(data, "jobs_data.txt")


if __name__ == '__main__':
    main()
