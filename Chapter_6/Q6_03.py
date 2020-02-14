class Character:
    def __init__(self, name='', hp=0, mp=0):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp


with open('characters.csv', 'r') as f:
    lines = f.readlines()
attributes = lines["""①"""].rstrip('\n')."""②"""(',')
characters = []
for i in range(1, len(lines)):
    character = Character()
    values = lines["""③"""].rstrip('\n')."""②"""(',')
    for j in range(0, len(attributes)):
        """④"""(character, attributes["""⑤"""], values["""⑤"""])
    characters.append(character)
