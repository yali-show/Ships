import random
import config


class Map:
    """
    control and save map
    """

    def __init__(self):
        alpha = config.alpha
        lines = [[0 for char in range(10)] for line in range(10)]

        self.map = {x: y for x, y in zip(alpha, lines)}  # noqa matrix that created with dict -> {'letter': massive}

        empty_position = "0"
        based_ship = "1"
        tried_positin = "2"
        fordefeated_ship = "3"


class User:
    """
    ability creating your map and attack enemy ships
    """
    def __init__(self, usersmap, enemymap):
        self.score = 0
        self.map = usersmap
        self.enemy_map = enemymap

    def place_ship(self, position, ship_type):
        pass


class Ships:
    """
    control ships and their placement
    """
    def __init__(self):
        self.names = ['4', '3', '3.1', '2', '2.1', '2.2', '1', '1.1', '1.2',
                      '1.3']  # names of ships
        self.alphas_position = {alpha: number for number in range(1, 11)
                                for alpha in config.alpha}

        self.ships_positions = {}  # noqa all positions of ships by names
        # [name: {tuples of positions}]

        self.ships = {}  # positions of ships [tuple of 1 position: name]
        self.ocupated_positions = {name: set() for name in self.names}  # noqa position of grey positions

    def ships_config(self, positions: str, name: str):
        position = sorted(positions.split())
        start_column_position = position[0][0]
        start_line_position = int(position[0][1:]) - 1
        finish_column_position = position[1][0]
        finish_line_position = int(position[1][1:]) - 1

        if start_column_position == finish_column_position or\
                start_line_position == finish_line_position:

            if (start_line_position and finish_line_position in range(0, 11))\
                    and\
                    (start_column_position
                     and finish_column_position in config.alpha):

                if start_column_position == finish_column_position:
                    column = finish_column_position
                    all_positions = \
                        (column, pos for pos in
                         range(start_line_position, finish_line_position + 1))

                    self.ships_positions[name] = set(all_positions)

                    for position in all_positions:
                        self.ships[position] = name

                else:
                    line = finish_line_position
                    column = config.alpha[(self.alphas_position[start_column_position]-1):(self.alphas_position[finish_column_position]-1)]
                    all_positions = (columns, line for columns in column)

                    self.ships_positions[name] = set(all_positions)

                    for position in all_positions:
                        self.ships[position] = name


class MapGenerator:
    """
    create random map
    """
    def generate_random_map(self) -> Map:
        ship_controll = Ships()
        for


class EnemyComputer(MapGenerator):
    """
    generate own map and logic how to attack user`s ships
    """

    def __init__(self, enemymap):
        self.score = 0
        self.enemy_map = enemymap

    def attack(self):
        pass


class Game:
    """
    reload game if in need
    """
    pass


if __name__ == "__main__":
    pass
