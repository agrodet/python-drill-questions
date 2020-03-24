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

    def attack(self, target):  # 通常の攻撃
        target.hp -= self.strength


class Healer(Character):
    def __init__(self, name, hp, mp, power=1):
        Character.__init__(self, name, hp, mp)
        self.power = power

    def heal(self, target):  # 回復の呪文
        if self.mp > 2:
            target.hp += self.power
            self.mp -= 2


class HealerAttacker(Healer, Attacker):
    def __init__(self, name, hp, mp, strength=1, power=1):
        Attacker.__init__(self, name, hp, mp, strength)
        self.power = power


can_attack = [character for character in characters if """①"""("""②""", """③""")]
