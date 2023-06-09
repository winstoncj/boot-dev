import random


class BSTNode(object):
    """
    Binary Search Tree - Exists
    We need a method to check if a value already exists in the tree.

    Assignment
    Oh no! We have some characters with the same character tag. We need a way to check for the existence of a tag before creating a new character.

    Implement the exists method. It should take a value as input and return True if the value exists in the tree, and False if it doesn't.
    """

    def exists(self, val):
        # YOUR CODE HERE
        if self.val == val:
            return True
        elif val < self.val:
            if self.left:
                return self.left.exists(val)
            else:
                return False
        elif val > self.val:
            if self.right:
                return self.right.exists(val)
            else:
                return False
        else:
            return False

        # -- TEST SUITE, DON'T TOUCH BELOW THIS LINE --

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

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
    characters = get_characters(1000)
    bst = BSTNode(Character(50))
    for character in characters:
        bst.insert(character)

    characters = get_characters(25)
    for character in characters:
        print(str(character) + " exists:")
        print(bst.exists(character))


main()
