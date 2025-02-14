import random


class Actor:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return 'Actor: {}, Level: {}'.format(self.name, self.level)

    def get_attack_power(self):
        return random.randint(1, 100) * self.level

    def attacks(self, other):
        raise NotImplementedError()


class Player(Actor):

    def attacks(self, enemy):
        power = self.get_attack_power()
        enemy_power = enemy.get_attack_power()

        print('You deal {} damage!'.format(power))
        print('The {} deals {} damage!'.format(enemy.kind, enemy_power))

        if power >= enemy_power:
            print('You slay the {}!'.format(enemy.kind))
            return True
        else:
            print('You were defeated.')
            return False


class Enemy(Actor):
    def __init__(self, name, level, kind):
        super().__init__(name, level)
        self.kind = kind



if __name__ == '__main__':
    player = Player(name = 'Hercules', level = 1)
    enemy = Enemy(kind = 'Ogre', level = 1, name='Bob')
    print(player)
    print(player.get_attack_power())
    print(enemy)
    print(enemy.get_attack_power())

