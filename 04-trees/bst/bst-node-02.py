import random


class BSTNode(object):
    """
    Binary Search Tree - Traverse Preorder
    Sometimes it's useful, albeit a bit slow, to iterate over all the nodes in the tree, rather than searching for a specific one.

    In the next few assignments, we will explore different ways of traversing a BST.

    Assignment
    We now have a bunch of characters in our tree! Our analytics team needs a way to copy the data and create a backup. To make a copy while preserving the structure, we need to recursively traverse our BST.

    Implement the recursive preorder method. It returns a list of the values in the order they are visited, and it takes as an argument the ordering of values we have visited so far.

    For example, the first call to preorder on an entire tree would be:

    # an empty list is passed in the first call
    bst_node.preorder([])
    Here are the algorithm's steps:

    Visit the value of the current node by appending its value to the visited array
    Recursively traverse the left subtree
    Recursively traverse the right subtree
    Return the array of visited nodes
    The following tree:

        > 7
            > 6
    > 4
        > 2
            > 1
    Would return the following list:

    [4, 2, 1, 7, 6]
    """

    def preorder(self, visited):
        visited.append(self.val)
        if self.left:
            self.left.preorder(visited)
        if self.right:
            self.right.preorder(visited)
        return visited

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
    characters = get_characters(8)
    bst = BSTNode(Character(4))
    for character in characters:
        bst.insert(character)
    print(bst)
    print("#")
    print("preorder:")
    print(bst.preorder([]))
    print("#########")

    characters = get_characters(25)
    bst = BSTNode(Character(12))
    for character in characters:
        bst.insert(character)
    print(bst)
    print("#########")
    print("preorder:")
    print(bst.preorder([]))


main()
