#student.py
class Student():
    def __init__(self, name, discord_id, fav_food, dream):
        self.name       = name
        self.discord_id = discord_id
        self.fav_food   = fav_food
        self.dream      = dream

    def my_print(self):
        print(self.name + " " + self.discord_id + " " + self.fav_food + " " + self.dream)

    #courtesy of Deb Cupitt's great question!
    def my_iter(self):
        for attr, value in self.__dict__.items():
            print(attr, value)


