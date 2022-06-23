import os

import pandas as pd
from bs4 import BeautifulSoup

list_link_dir = []
tables = []


def file_details(file_name):
    with open(file_name, "r", encoding="utf-8") as file_write:
        xml_doc = BeautifulSoup(file_write.read(), "lxml")
        blocks_all_elements = xml_doc.find_all("item")

        show_id = []
        title = []
        director = []
        cast = []
        country = []
        date_added = []
        rating = []
        duration = []
        listed_in = []
        description = []

        for block in blocks_all_elements:
            show_id.append(block.find("field", {"name": "show_id"}).text)
            title.append(block.find("field", {"name": "title"}).text)
            director.append(block.find("field", {"name": "director"}).text)
            cast.append(block.find("field", {"name": "cast"}).text)
            country.append(block.find("field", {"name": "country"}).text)
            date_added.append(block.find("field", {"name": "date_added"}).text)
            rating.append(block.find("field", {"name": "rating"}).text)
            duration.append(block.find("field", {"name": "duration"}).text)
            listed_in.append(block.find("field", {"name": "listed_in"}).text)
            description.append(block.find("field", {"name": "description"}).text)

        df = pd.DataFrame({"show_id": show_id})
        df["title"] = title
        df["director"] = director
        df["cast"] = cast
        df["country"] = country
        df["date_added"] = date_added
        df["rating"] = rating
        df["duration"] = duration
        df["listed_in"] = listed_in
        df["description"] = description
        return df


def dir_file(path, list_l):
    for a, b, c in os.walk(path):
        if len(c) == 0:
            continue
        else:
            for _ in c:
                list_l.append(f"{a}/{_}")
                print(f"{a}/{_}")


def record_data(list_link):
    for l in list_link:
        table = file_details(l)
        tables.append(table)


dir_file(f"{os.getcwd()}/task", list_link_dir)
record_data(list_link_dir)
result = pd.concat(tables, sort=True, axis=1)
result.reset_index(level=0,drop=True)
result.head()
