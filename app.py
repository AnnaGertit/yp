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
    elif command == "5":
        sorting()
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


def sorting():
    print("Please write filename: ")
    file_name = input()
    try:
        f = open(file_name)
        data = json.loads(f.read())#преобразовать содержимое файла в обьект
        print(
            "Please specify number: "
            "1. Артикул\n"
            "2. Название товара\n"
            "3. Количество\n"
            "4. Цена\n"
        )
        paragraph = input()
        if paragraph == "1":
            sorted({1:'id',2:'name',3:'quantity',4:'price'})
            [1,2,3,4]

    except FileNotFoundError:
        print("File not found")
    except json.decoder.JSONDecodeError:
        print("Incorrect data")
    except KeyError:
        print("Incorrect file params")   
    
preview()
