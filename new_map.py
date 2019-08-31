from random_map_merger import tuple_constructor, random_map_maker, random_map_filler


class Block:
    def __init__(self, title: str,
                 huge_dic,
                 size: list, is_player: bool = False):
        self.__title = title  # Τιτλος Μπλοκ
        self.__huge_dic = huge_dic  # Το νέο map container
        self.__size = size  # Μέγεθος μπλοκ πχ 3x3
        self.__is_player = is_player  # Αν ειναι ο player στο μπλοκ το default ειναι false για ευνόητους λόγους

    @property
    def title_gen(self):
        return self.__title

    @title_gen.setter
    def title_gen(self, title):
        self.__title = title

    @property
    def huge_dic_gen(self):
        return self.__huge_dic

    @huge_dic_gen.setter
    def huge_dic_gen(self, huge_dic):
        self.__huge_dic = huge_dic

    @property
    def size_gen(self):
        return self.__size

    @size_gen.setter
    def size_gen(self, size):
        self.__size = size

    @property
    def is_player_gen(self):
        return self.__is_player

    @is_player_gen.setter
    def is_player_gen(self, is_player):
        self.__is_player = is_player

    def __str__(self):
        return self


'''Ορίζω τα preset block που θα δομήσουν τον χάρτη μου'''
# main_block
main_block = Block('Start',
                   {1: [1, 0, 1],
                    2: [0, '@', 0],
                    3: [1, 1, 1]},
                   [3, 3], True)
# filler_block_up
filler_block_up = Block('Filler_Up',
                        {1: [0, 0, 1],
                         2: [1, 0, 0]},
                        [3, 2])
# filler_block_bottom
filler_block_bottom = Block('Filler_Bottom',
                            {1: [0, 0, 0],
                             2: [1, 0, 1]},
                            [3, 2])
# mountain_hike
mountain_hike = Block('Mountain',
                      {1: [0, 0, 0, 1, 1, 1],
                       2: [0, 1, 0, 0, 0, 0],
                       3: [1, 0, 0, 0, 0, 0],
                       4: [0, 0, 0, 0, 0, 0]},
                      [6, 4])
# mario_like
mario_like = Block('Mario_Like',
                   {1: [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    2: [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
                    3: [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]},
                   [12, 3])

# cliff_edge
cliff_edge = Block('Cliff_Edge',
                   {1: [1, 1, 1, 0, 0, 0],
                    2: [0, 0, 0, 0, 1, 0],
                    3: [0, 0, 0, 0, 0, 1],
                    4: [0, 0, 0, 0, 0, 0]},
                   [6, 4])

# filler_block_column
filler_block_column = Block('Filler_Column',
                            {1: [0],
                             2: [0],
                             3: [1]},
                            [1, 3])

# filler_block_shelf
filler_block_shelf = Block('Filler_Shelf',
                           {1: [1, 0, 0]},
                           [1, 3])

map_setter = []

# Λίστα/Inventory με τα preset μπλοκ για να τεμπελιάσω κάτω
block_list = [main_block, '', '', '', '', filler_block_up, filler_block_bottom, mountain_hike,
              mario_like, cliff_edge, filler_block_column, filler_block_shelf]


tuple_constructor(map_setter, block_list, 40, 40)
random_map_maker(map_setter)
random_map_filler()
'''############ Αν συμφωνείς πάω στο επόμενο βήμα με τους colliders #############'''
