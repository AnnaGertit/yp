import json

translate = {
    "id": "Артикул",
    "name": "Название товара",
    "quantity": "Колличество",
    "price": "Цена"
}

def preview():
    print(
        "####################\n"
        "1. New file\n"
        "2. Add iformation\n"
        "3. View file\n"
        "4. Search\n"
        "5. Sorting\n"
        "6. Delete\n"
        "7. Exit\n"
        "Please select an action:"
    )

    command = input()
    if command == "1":
        new_file()
    elif command == "2":
        add_iformation()
    elif command == "3":
        view_file()
    elif command == "4":
        search()
    elif command == "5":
        sorting()
    elif command == "6":
        delete()
    elif command == "7":
        print("Exit")
        return
    else:
        print("Command not defined")

    preview()


def new_file():
    print("Please write filename: ")
    file_name = input()
    try:
        f = open(file_name)
        print("File exist")
        f.close()
    except FileNotFoundError:
        f = open(file_name, "a+")
        f.write("[]")
        f.close()


def add_iformation():
    print("Please write filename: ")
    file_name = input()
    try:
        f = open(file_name)
        file = f.read()
        data = json.loads(file)
        f.close()
        articles = []
        for i in data:
            articles.append(i["id"])

        new_data = {}
        print("Please write information:")

        for i in translate:
            print(translate[i])
            new_data[i] = input()

        edited = 0
        for i in data:
            if i["id"] == new_data["id"]:
                print("Replace the existing!")
                for j in i:
                    i[j] = new_data[j]
                edited = 1

        if edited == 0:
            print("Add new!")
            data.append(new_data)

        f = open(file_name, "w+")        
        f.write(json.dumps(data))
        f.close()
    except FileNotFoundError:
        print("File not found")
    except json.decoder.JSONDecodeError:
        print("Incorrect data")
    except KeyError:
        print("Incorrect file params")
    



def view_file():
    print("Please write filename: ")
    file_name = input()
    try:
        f = open(file_name)
        data = json.loads(f.read())
        print("\n")
        for i in data:
            for j in i:
                print(f"{translate[j]} ----- {i[j]}")
            print("\n")
        f.close()
    except FileNotFoundError:
        print("File not found")
    except json.decoder.JSONDecodeError:
        print("Incorrect data")
    except KeyError:
        print("Incorrect file params")



def search():
    print("Please write filename: ")
    file_name = input()
    try:
        f = open(file_name)
        data = json.loads(f.read())#преобразовать содержимое файла в обьект
        f.close()

        print(
            "Pleas select sort order:\n"
            "a. Процент торава с ценой более средней\n"
            "b. Название товара с ценой выше заданной\n"
            "c. информация товаров с максимальным количеством\n"
            "d. посчитать и вывести общую стоимость товаров, которые стоят меньше 2р\n"
            "e. посчитать и вывести названия и артикул товаргов в которых есть буква 'а'"
        )

        search = input()
        if search == "a":
            all_price = 0
            for i in data:
                all_price += float(i["price"])
            
            midle_price = all_price / len(data)
            more_average = 0

            for i in data:
                if midle_price < float(i["price"]):
                    more_average += 1

            print(
                f"Percent of product with a price more than average: {more_average / len(data) * 100}%"
            )

        



    except FileNotFoundError:
        print("File not found")
    except json.decoder.JSONDecodeError:
        print("Incorrect data")
    except KeyError:
        print("Incorrect file params")

def sorting():
    print("Please write filename: ")
    file_name = input()
    try:
        f = open(file_name)
        data = json.loads(f.read())#преобразовать содержимое файла в обьект
        f.close()
        print("Please specify number for sorting:")
        for index, key in enumerate(translate):
            print(f"{index+1}. {translate[key]}")

        paragraph = input()

        print(
            "Pleas select sort order:\n"
            "1. Direct sorting\n"
            "2. Reverse sorting\n"
        )
        sorting = input()

        reverse = False
        if sorting == 2:
            reverse = True

        if paragraph == "1":
            for i in data:
                i["id"] = int(i["id"])
            data = sorted(data, key = lambda x: x["id"], reverse = reverse)
        elif paragraph == "2":
            for i in data:
                i["name"] = i["name"]
            data = sorted(data, key = lambda x: x["name"], reverse = reverse)
        elif paragraph == "3":
            for i in data:
                i["quantity"] = i["quantity"]
            data = sorted(data, key = lambda x: x["quantity"], reverse = reverse)
        elif paragraph == "4":
            for i in data:
                i["price"] = float(i["price"])
            data = sorted(data, key = lambda x: x["price"], reverse = reverse)

        print("\n")
        for i in data:
            for j in i:
                print(f"{translate[j]} ----- {i[j]}")
            print("\n")

    except FileNotFoundError:
        print("File not found")
    except json.decoder.JSONDecodeError:
        print("Incorrect data")
    except KeyError:
        print("Incorrect file params")   


def delete():
    print("Please write filename: ")
    file_name = input()
    try:
        f = open(file_name)
        data = json.loads(f.read())#преобразовать содержимое файла в обьект
        f.close()
        print("Please specify number for delete:")
        for index, key in enumerate(translate):
            print(f"{index+1}. {translate[key]}")

        paragraph = input()

        for index, key in enumerate(translate):
            if str(index+1) == paragraph:
                print(f"Please write value of {translate[key]} for deleted")
                deleted_value = input()
                for val in data:
                    if val[key] == deleted_value:
                        data.remove(val)

        f = open(file_name, "w+")        
        f.write(json.dumps(data))
        f.close()

        print("Delete was successful")
    except FileNotFoundError:
        print("File not found")
    except json.decoder.JSONDecodeError:
        print("Incorrect data")
    except KeyError:
        print("Incorrect file params") 
    
preview()
