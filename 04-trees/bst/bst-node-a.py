import random


class BSTNode(object):
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if val < self.val:
            if self.left == None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right == None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)

        # -- TEST SUITE, DON'T TOUCH BELOW THIS LINE --

    def __repr__(self):
        lines = []
        print_tree(self, lines)
        return "\n".join(lines)


class Character:
    def __init__(self, gamertag):
        self.gamertag = gamertag
        character_names = [
            "Ebork",
            "Astram",
            "Elian",
            "Tarlock",
            "Grog",
            "Myra",
            "Sullivan",
            "Marlo",
            "Jax",
            "Anthony",
            "Bhurdan",
            "Thoreuth",
            "Bob",
            "Varis",
            "Nyx",
            "Luna",
            "Ash",
            "Rhogar",
            "Ember",
            "Mikel",
            "Yamil",
            "Velithria",
        ]
        self.character_name = (
            f"{character_names[gamertag%len(character_names)]}#{gamertag}"
        )

    def __eq__(self, other):
        return self.gamertag == other

    def __lt__(self, other):
        return self.gamertag < other

    def __gt__(self, other):
        return self.gamertag > other

    def __repr__(self):
        return "".join(self.character_name)


def print_tree(bst_node, lines, level=0):
    if bst_node != None:
        print_tree(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        print_tree(bst_node.left, lines, level + 1)


def get_characters(num):
    random.seed(1)
    characters = []
    for _ in range(num):
        character = Character(random.randint(0, num - 1))
        characters.append(character)
    return characters


def main():
    characters = get_characters(10)
    bst = BSTNode(Character(5))
    for character in characters:
        bst.insert(character)
    print(bst)


main()
