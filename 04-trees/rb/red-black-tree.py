import random


class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    """
    Red Black Tree - Insert
    Let's write the insert method for a red-black tree. The raw-insert part (what we'll be doing in this assignment) is very similar to that of the normal Binary Search Tree we just finished.

    We're going to implement it a little differently this time, however. We're going to forgo the idea of recursion completely to keep things a little simpler when dealing with parent-child relationships.

    In a normal BST, the child nodes don't need to know about, or carry a reference to their parent, the same is not true for Red-Black trees.

    The RBNode class is already implemented for you, as well as the __init__ constructor method of the RBTree class. There's also a data member, self.nil created for you in the constructor. self.nil contains the value we'll use to designate all the nil leaf nodes, which are used for rebalancing purposes but contain no useful value.

    red_black

    Assignment
    Our players have been creating and deleting lots of characters, and as a result, our tree is getting very unbalanced and slow! Our systems team has decided we should convert our Binary Search Tree into a Red Black Tree to keep things balanced and fast.

    Implement the insert method. It should take a value as input and add the value as a new node if the value doesn't already exist in the tree.

    Here are the steps:

    Create the new node
    Create a new RBNode from the given input value
    The new node shouldn't have a parent yet
    The new node's left and right children should be nil
    The new node is red. (new_node.red = True)
    Find the parent of the new_node if there will be one
    Initialize a parent variable to None
    Initialize a current variable to the root node of the tree
    While the current variable isn't a nil node:
    Set parent to the current
    If the new_node's value is less than the current node's, set current to its own left child. If it's greater, set to its right child. If the values are equal, just return because this value is a duplicate.
    parent should now be a reference to the node that will become the parent of the new node
    Insert the new node
    Set the new node's parent to the parent we just found
    If the parent is None, we are dealing with a new root, so set the tree's root data member to the new node
    Otherwise, compare the values of the parent and new node and set the parent's left or right child based on the results
    Done for now
    We've essentially just made another binary tree seeing as it's not a fully-fledged red-black tree yet. The only upgrades we've made so far are:

    We've kept a parent point from child->parent
    We've added the mechanisms for coloring the nodes, but have defaulted them all to red for now
    """

    def __init__(self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        new_node = RBNode(val)
        new_node.red = True
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # -- TEST SUITE, DON'T TOUCH BELOW THIS LINE --

    def __repr__(self):
        lines = []
        print_tree(self.root, lines)
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


def print_tree(node, lines, level=0):
    if node.val != 0:
        print_tree(node.right, lines, level + 1)
        lines.append(
            "-" * 4 * level + "> " + str(node.val) + " " + ("r" if node.red else "b")
        )
        print_tree(node.left, lines, level + 1)


def get_characters(num):
    random.seed(1)
    characters = []
    for _ in range(num):
        character = Character(random.randint(1, num - 1))
        characters.append(character)
    return characters


def main():
    characters = get_characters(25)
    tree = RBTree()
    for character in characters:
        tree.insert(character)
    print(tree)


main()
