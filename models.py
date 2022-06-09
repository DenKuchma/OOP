import random
from exceptions import EnemyDown, GameOver
from settings import player_choices
from score import Score


class Player:
    def __init__(self, name: str):
        self.name = name
        self.lives = 1
        self.score = 0

    def decrease_lives(self):
        self.lives -= 1
        if self.lives < 1:
            Score.add_score(self.name, self.score)
            raise GameOver()

    @staticmethod
    def fight(attack, defense) -> int:
        if attack == 1 and defense == 2:
            return 1
        if attack == 1 and defense == 3:
            return -1
        if attack == 2 and defense == 1:
            return -1
        if attack == 2 and defense == 3:
            return 1
        if attack == 3 and defense == 1:
            return 1
        if attack == 3 and defense == 2:
            return -1
        else:
            return 0

    def attack(self, enemy_obj):
        attack = None
        while attack not in player_choices:
            try:
                attack = int(input("Your attack, number 1 - 3: "))
            except ValueError:
                pass
        defense = enemy_obj.enemy_choice()
        result = self.fight(attack, defense)
        if result == 0:
            print("It's a draw!")
        if result == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
        if result == -1:
            print("You missed!")

    def defence(self, enemy_obj):
        defense = None
        while defense not in player_choices:
            try:
                defense = int(input("Your defense, number 1 - 3: "))
            except ValueError:
                pass
        attack = enemy_obj.enemy_choice()
        result = self.fight(attack, defense)
        if result == 0:
            print("It's a draw!")
        if result == 1:
            print("Enemy attacked successfully!")
            self.decrease_lives()
        if result == -1:
            print("Enemy missed!")


class Enemy:
    def __init__(self, level: int):
        self.level = level
        self.lives = level

    @staticmethod
    def enemy_choice():
        return random.randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives < 1:
            raise EnemyDown()
