from Actors import Player, Enemy
import random


class Game:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def main(self):
        self.print_intro()
        self.play()

    def print_intro(self):
        print('''
            Monster Slash!!!
            Ready Player One?
            [Press Enter to Continue...]
        ''')
        input()

    def print_linebreak(self):
        print()
        print('*' * 30)
        print()

    def play(self):
        while True:
            next_enemy = random.choice(self.enemies)

            cmd = input('You see a {}. [r]un, [a]ttack, [p]ass?\n'.format(next_enemy.kind))
            if cmd == 'r':
                print('\n{} runs away!'.format(self.player.name))
            elif cmd == 'a':
                print('\n{} attacks the {}!'.format(self.player.name, next_enemy.kind))
                if self.player.attacks(next_enemy):
                    self.enemies.remove(next_enemy)
                else:
                    print('\n{} hides to plan next move.'.format(self.player.name))
            elif cmd == 'p':
                print('\nYou think about life...')
            else:
                print('\nPlease select a valid choice.')

            self.print_linebreak()

            if not enemies:
                print('You have won! Congratulations!')
                break


if __name__ == '__main__':
    enemies = [
        Enemy('Ogre', 1),
        Enemy('Imp', 1)
    ]
    player = Player('Hercules', 1)
    Game(player, enemies).main()

