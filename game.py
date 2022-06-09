from exceptions import GameOver, EnemyDown
from settings import valid_characters
from models import Player, Enemy


def get_name() -> str:
    name = ""
    while not name or not all(char in valid_characters for char in name):
        name = input("ENTER YOUR NAME: ")
    return name


def print_hi(name):
    print(f'Welcome, {name}')


def visual_game(enemy_lives, player_name, player_lives, player_score):
    print('Enemy(' + '*' * enemy_lives + ')\n'
          'VS\n'
          f'{player_name}(' + '*' * player_lives + ')\n'
          + f'Score({player_score})')


def play():
    player_name = get_name()
    print_hi(player_name)
    player = Player(player_name)
    enemy_level = 1
    enemy = Enemy(enemy_level)
    while True:
        try:
            visual_game(enemy.lives, player.name, player.lives, player.score)
            player.attack(enemy)
            visual_game(enemy.lives, player.name, player.lives, player.score)
            player.defence(enemy)
        except EnemyDown:
            enemy_level += 1
            enemy = Enemy(enemy_level)
            player.score += 5
            print('Enemy is down, +5 score')


def show_scores():
    with open('scores.txt', 'r') as scores:
        for line in scores:
            print(line)


menu = {'show scores': show_scores, 'play': play, 'exit': exit}


if __name__ == "__main__":
    while True:
        try:
            command = input('Choose command(show scores, play, exit): ')
            menu[command]()
        except GameOver:
            print('Game Over, you are die...')
        except KeyError:
            print('Try again correct command')
        except KeyboardInterrupt:
            pass



