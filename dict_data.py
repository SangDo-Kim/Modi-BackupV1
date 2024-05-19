"""Dictionary V1.0
The class handles a dictionary attribute, save it to a json file and load from it.

Dictionary.load_from_file() return True or False to notify if loading was successful.
"""
import json


class DictData:
    def __init__(self, filename="dict_data.json"):
        self.filename = filename
        self.dict = {}

    def save_to_file(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.dict, file, ensure_ascii=False, indent="\t")

    def load_from_file(self) -> bool:
        try:
            with open(self.filename, "r", encoding='utf-8') as file:
                self.dict = json.load(file)
        except FileNotFoundError:
            return False

        if len(self.dict.items()) > 0:
            return True
        else:
            return False


if __name__ == "__main__":
    my_data = DictData("test_data.json")
    my_data.dict["D:\\"] = "20240519"
    my_data.dict["E:\\"] = "20240518"

    my_data.save_to_file()
    my_data.dict["D:\\"] = "20240101"
    print(my_data.dict.items())

    my_data.load_from_file()
    print(my_data.dict.items())




