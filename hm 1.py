class Hero:
    head = 1
    ability = True

    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage

    def heal(self):
        self.hp += 100

    def two_damage(self):
        self.damage *= 2

    def greetings(self):
        print(f'my name is {self.name}')

    def brand_phrase(self):
        print('good will win')


hero1 = Hero(name='Franko', nickname='Iseeko', hp=2530, damage=500)
hero2 = Hero(name='Ruby', nickname='BinGing', hp=1500, damage=625)
hero3 = Hero(name='Klint', nickname='FastOring', hp=1550, damage=700)
hero4 = Hero(name='Saber', nickname='SaYouNit', hp=1325, damage=650)

hero1.heal()
print(hero1.hp)
hero2.two_damage()
print(hero2.damage)
hero3.greetings()
hero4.brand_phrase()