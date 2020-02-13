class Person:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def __str__(self):
        return "{0} {1}".format(self.last_name, self.first_name)


class SpecialAgent(Person):
    def __init__(self, last_name, first_name, number):
      super().__init__(last_name, first_name)
      self.number = number

    def __str__(self):
      return "Agent {0}. {1}, {2} {1}".format(self.number, self.last_name, self.first_name)


agent = SpecialAgent("Bond", "James", "007")
print(agent)  # 出力は　"""①"""
