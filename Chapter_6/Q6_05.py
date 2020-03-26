import """①"""


def save_characters(characters):
    with open('characters', 'w"""②"""') as f:
        pickler = """①""".Pickler(f)
        pickler."""③"""(characters)


# ここからは関数を使うためのコード
class Character:
    def __init__(self, name, hp, mp):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp


class Attacker(Character):
    def __init__(self, name, hp, mp, strength=1):
        Character.__init__(self, name, hp, mp)
        self.strength = strength

    def attack(self, target):
        target.hp -= self.strength


class Healer(Character):
    def __init__(self, name, hp, mp, power=1):
        Character.__init__(self, name, hp, mp)
        self.power = power

    def heal(self, target):
        if self.mp > 2:
            target.hp += self.power
            self.mp -= 2


class HealerAttacker(Healer, Attacker):
    def __init__(self, name, hp, mp, strength=1, power=1):
        Attacker.__init__(self, name, hp, mp, strength)
        self.power = power


bary = Attacker('Bary', 142, 21, 12)
camille = Healer('Camille', 65, 45, 7)
corin = HealerAttacker('Corin', 95, 38, 10, 5)

characters = [bary, camille, corin]

save_characters(characters)
