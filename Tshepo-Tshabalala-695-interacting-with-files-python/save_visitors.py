import json
from datetime import datetime
import os


class Visitor:
    def __init__(self, name, age, visit_date, visit_time, comments, assisted_by):
        self.name = name
        self.age = age
        self.visit_date = visit_date
        self.visit_time = visit_time
        self.comments = comments
        self.assisted_by = assisted_by

    def save(self):
        date = datetime.today()
        visitor_dict = {
            "full_name": self.name,
            "age": self.age,
            "date_of_visit": f"{date.date()}",
            "time_of_visit": f"{date.time()}",
            "comments": self.comments,
            "assisted_by": self.assisted_by,
        }
        file = open(
            "visitor_" + f"{'_'.join(self.name.lower().split())}" + ".json", "w+"
        )
        json.dump(visitor_dict, file)
        file.close()
        return file

    def load(self, name):
        read_files = None
        filename = "_".join(name.lower().split())
        name = "visitor_" + filename + ".json"
        files_list = os.listdir()
        if name in files_list:
            read_files = open(name, "r")
            print(json.dumps(read_files.read()))
            read_files.close()


if __name__ == "__main__":
    d = datetime.today()
    msese = Visitor("Leo Messi", "34", d.day, d.time, "La Masia", "Somebody")
    msese.save()
    msese.load("Leo Messi")
