import csv
import json
import random 


DATASET_PATH = "books.csv"


def get_title(dataset):
    dataset.seek(0)
    title = next(dataset)
    title = title.split(";")
    title = [col.strip() for col in title]

    return title


def get_object_alt(line, title):
    reader = csv.DictReader([line], title, delimiter=';', quotechar='"')
    result = next(reader)
    return result


# def filter_value(dataset, title, value):
#     filtered = []

#     for line in dataset:
#         obj = get_object_alt(line, title)
#         book_value = obj["Цена поступления"]

#         if float(book_value) < value:
#             filtered.append(obj)

#     dataset.seek(0)
#     return filtered


# def search(object, author):
#     search_res = []
#     for i in object:
#         if i["Автор (ФИО)"] == author:
#             search_res.append(i["Название"])
#     return search_res


# def filter_title(dataset, title, length):
#     filtered = []

#     for line in dataset:
#         obj = get_object_alt(line, title)
#         book_title = obj["Название"]

#         if len(book_title) > length:
#             filtered.append(obj)

#     dataset.seek(0)
#     return filtered


if __name__ == "__main__":
    with open(DATASET_PATH, encoding="windows-1251") as dataset:
        title = get_title(dataset)
        data = []

        for line in dataset:
            obj = get_object_alt(line,title)
            data.append(obj)


        with open("bibliography.txt", "w") as file:
            for i in range(1, 21):
                book = random.choice(data)
                author = book['Автор']
                name = book['Название']
                year = book['Дата поступления'][6:10]
        
                entry = f"{i}. {author}. {name} - {year}"
        
                file.write(entry + "\n")
        

        
