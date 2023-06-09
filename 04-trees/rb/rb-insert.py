import random

"""
ASSIGNMENT
Our players have been creating and deleting lots of characters, and as a result, our tree is getting very unbalanced and slow! Our systems team has decided we should convert our Binary Search Tree into a Red Black Tree to keep things balanced and fast.

Implement the insert method. It should take a value as input and add the value as a new node if the value doesn't already exist in the tree.

Here are the steps:

CREATE THE NEW NODE
Create a new RBNode from the given input value
The new node shouldn't have a parent yet
The new node's left and right children should be nil
The new node is red. (new_node.red = True)
FIND THE PARENT OF THE NEW_NODE IF THERE WILL BE ONE
Initialize a parent variable to None
Initialize a current variable to the root node of the tree
While the current variable isn't a nil node:
Set parent to the current
If the new_node's value is less than the current node's, set current to its own left child. If it's greater, set to its right child. If the values are equal, just return because this value is a duplicate.
parent should now be a reference to the node that will become the parent of the new node
INSERT THE NEW NODE
Set the new node's parent to the parent we just found
If the parent is None, we are dealing with a new root, so set the tree's root data member to the new node
Otherwise, compare the values of the parent and new node and set the parent's left or right child based on the results
DONE FOR NOW
We've essentially just made another binary tree seeing as it's not a fully-fledged red-black tree yet. The only upgrades we've made so far are:

We've kept a parent point from child->parent
We've added the mechanisms for coloring the nodes, but have defaulted them all to red for now
"""


class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        node = RBNode(val)
        # node.parent = self.nil
        node.left = self.nil
        node.right = self.nil
        node.red = True
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if node.val < current.val:
                current = current.left
            elif node.val > current.val:
                current = current.right
            else:
                return
        node.parent = parent
        if parent == None:
            self.root = node
        elif node.val < parent.val:
            parent.left = node
        else:
            parent.right = node
        # self.insert_fixup(node)

    # don't touch below this line

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
        if not isinstance(other, Character):
            return False
        return self.gamertag == other.gamertag

    def __lt__(self, other):
        if not isinstance(other, Character):
            return False
        return self.gamertag < other.gamertag

    def __gt__(self, other):
        if not isinstance(other, Character):
            return False
        return self.gamertag > other.gamertag

    def __repr__(self):
        return "".join(self.character_name)


def print_tree(node, lines, level=0):
    if node.val is not None:
        print_tree(node.right, lines, level + 1)
        lines.append(
            " " * 4 * level
            + "> "
            + str(node.val)
            + " "
            + ("[red]" if node.red else "[black]")
        )
        print_tree(node.left, lines, level + 1)


def get_characters(num):
    characters = []
    for _ in range(num):
        character = Character(random.randint(1, num - 1))
        characters.append(character)
    return characters


def test(num_characters):
    characters = get_characters(num_characters)
    tree = RBTree()
    for character in characters:
        print(f"Inserting {character} into tree...")
        tree.insert(character)
    print("Tree:")
    print("-------------------------------------")
    print(tree)
    print("=====================================")


def main():
    random.seed(1)
    test(4)
    test(8)
    test(16)


main()
