import requests

def display_data(to_display):
    for recipe in to_display:
        print(recipe['title'])


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
    loc = f"https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=18381bc0&app_key=f20a9d4e1c0d42e8d120af190ecfb44d&results_per_page=20&what=javascript%20developer&what_exclude={params[0]}&where=london&sort_by=salary&salary_min=30000&full_time=1&permanent=1&content-type=application/json"
    print(loc)
    data = get_data(loc)
    display_data(data)


if __name__ == '__main__':
    main()
