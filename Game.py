from Actors import Player, Enemy
import random

def main():
    print_intro()
    play()

def print_intro():
    print('''
        Monster Slash!!!
        Ready Player One?
        [Press Enter to Continue...]
    ''')
    input()

def play():
    enemies = [
        Enemy('Ogre', 1),
        Enemy('Imp', 1)
    ]
    player = Player('Hercules', 1)
    while True:
        next_enemy = random.choice(enemies)
        cmd = input('You see a {}. [r]un, [a]ttack, [p]ass?\n'.format(next_enemy.kind))
        if cmd == 'r':
            print('\n{} runs away!'.format(player.name))
        elif cmd == 'a':
            print('\n{} attacks the {}!'.format(player.name, next_enemy.kind))
            if player.attacks(next_enemy):
                enemies.remove(next_enemy)
            else:
                print('\n{} hides to plan next move.'.format(player.name))
        elif cmd == 'p':
            print('\nYou think about life...')
        else:
            print('\nPlease select a valid choice.')

        print()
        print('*'*30)
        print()

        if not enemies:
            print('You have won! Congratulations!')
            break

if __name__ == '__main__':
    main()
