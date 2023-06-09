import random


class BSTNode(object):
    """
    Binary Search Tree - Traverse Postorder
    Assignment
    Our analytics team wants another way to visualize our player data.

    Implement the recursive postorder method. It returns a list of the values in the order they are visited, and it takes as an argument the ordering of values we have visited so far.

    For example, the first call to postorder on an entire tree would be:

    # an empty list is passed in the first call
    bst_node.postorder([])
    Here are the algorithm's steps:

    Recursively traverse the left subtree
    Recursively traverse the right subtree
    Visit the value of the current node by appending its value to the visited array
    Return array of visited nodes
    The following tree:

        > 7
            > 6
    > 4
        > 2
            > 1
    Would return the following list:

    [1, 2, 6, 7, 4]
    """

    def postorder(self, visited):
        # YOUR CODE HERE
        if self.left:
            self.left.postorder(visited)
        if self.right:
            self.right.postorder(visited)
        visited.append(self.val)
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
    print("postorder:")
    print(bst.postorder([]))
    print("#########")

    characters = get_characters(25)
    bst = BSTNode(Character(12))
    for character in characters:
        bst.insert(character)
    print(bst)
    print("#########")
    print("postorder:")
    print(bst.postorder([]))


main()
