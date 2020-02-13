"""①""" Person:
    def """②"""(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def description(self):
        return self.last_name + " " + self.first_name + ", " + """③"""(self.age) + "歳です！"


sanae = Person("ヤマモト", "サナエ", 29)
print(sanae.description())
