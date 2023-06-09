import random

"""
Let's write the rotate_left and rotate_right methods for our red-black tree. These methods will be fundamental to the "fix" method that we will implement in the next assignment.

The rotations are tools we'll use to keep our tree balanced. Every time one branch of the tree starts to get too long, we will just rotate those branches to keep the tree shallow. A shallow tree is a healthy (fast) tree!

A properly-ordered tree pre-rotation remains a properly-ordered tree post-rotation
Rotations are O(1) operations
When rotating left:
The "pivot" node's right child becomes its parent
The new parent's old left child becomes the pivot node's new right child
ASSIGNMENT
Our system manager's main concern with our old BST was that it was getting unbalanced and slow. Now that we can add characters to our new Red Black Tree, we need to add the building blocks to help keep it balanced and running fast!

Implement the rotate_left class method. It takes a single pivot node, x, as input and rotates the tree around that node. The steps are as follows:

If x is nil or x's right child is nil, return. Nothing to do here.
Let y be x's right child.
Set x's right child to be y's left child.
If y's left child isn't a leaf node, set y's left-child's parent to x
Set y's parent to x's parent
If x is the root, set the root to y
Otherwise, if x is its parent's left child, set x's parent's left child to y
Otherwise, if x is its parent's right child, set x's parent's right child to y
Set y's left child to be x
Set x's parent to be y
Implement the same algorithm for rotate_right with all the directionality inverted
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

    def rotate_left(self, x):
        if x == self.nil or x.right == self.nil:
            return
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        if x == self.nil or x.left == self.nil:
            return
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

        # don't touch below this line

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
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
        if parent == None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

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
        return self.gamertag == other.gamertag

    def __lt__(self, other):
        return self.gamertag < other.gamertag

    def __gt__(self, other):
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


def test_rotate(tree, node, direction):
    print(f"Rotating {direction} at {node.val}...")
    print("-------------------------------------")
    if direction == "left":
        tree.rotate_left(node)
    else:
        tree.rotate_right(node)
    print(tree)
    print("-------------------------------------")


def test(num_characters):
    characters = get_characters(num_characters)
    tree = RBTree()
    for character in characters:
        tree.insert(character)

    print("Original Tree:")
    print("-------------------------------------")
    print(tree)
    print("-------------------------------------")
    test_rotate(tree, tree.root, "left")
    test_rotate(tree, tree.root, "right")
    test_rotate(tree, tree.root.right, "left")
    test_rotate(tree, tree.root.left, "right")
    print("=====================================")


def main():
    random.seed(1)
    test(8)
    test(12)


main()
