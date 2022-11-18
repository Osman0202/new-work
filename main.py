class Hero:
    def __init__(self, nickname, agility=True):
        self.nickname = nickname
        self.agility = agility


class Hero_Super(Hero):
    def __str__(self):
        self.nickname = str

    def pr(self):
        print(f'{self.nickname} it is super_hero')
