#diy.py
class Diy():
    def __init__(self, first_n, last_n, email, country_code, tel, github, discord_id, country_birth, country_loc, gender, motivation, coding_level, groups, extra):
        self.first_n = first_n
        self.last_n = last_n
        self.email = email
        self.country_code = country_code
        self.tel = tel
        self.github = github
        self.discord_id = discord_id
        self.country_birth = country_birth
        self.country_loc = country_loc
        self.gender = gender
        self.motivation = motivation
        self.coding_level= coding_level
        self.groups =groups
        self.extra = extra
        
    def my_print(self):
        for attr, value in self.__dict__.items():
            print(attr, ": ", value)   


    


