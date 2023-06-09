import random

"""
# RANGE SEARCH
In the Fantasy Quest game, players often want to search for characters based on a given range of gamer tags. To support this feature, we'll need to implement a method that returns all characters within a specified range of gamer tags.

## ASSIGNMENT
Implement the search_range method for the BSTNode class. The method should take two arguments, lower_bound and upper_bound, and return a list of character objects whose gamer tags fall within the specified range, *inclusive*.

To accomplish this, you'll need to traverse the tree and collect the character objects that meet the criteria. You can use any traversal method you prefer (preorder, inorder, or postorder).

Remember to keep the search efficient by not traversing unnecessary branches. For example, if the current node's gamer tag is less than the lower bound, there's no need to search its left subtree.

You can access a gamer tag using the .gamertag property of a character object, which is held in the .val property of a BSTNode.

## TIPS
```python
The  [.extend()](https://docs.python.org/3/tutorial/datastructures.html)  method is a convenient way to add all the elements of a list to another list. For example:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)
# [1, 2, 3, 4, 5, 6]
```

Research notes:
There are three main types of traversal methods in the binary tree: In-order traversal, Pre-order traversal and Post-order traversal¹. 

- In-order traversal: In the in-order traversal method, the left child and left subtree are traversed first, afterward the root tree and then the right children or the right subtree are traversed¹³.
- Pre-order traversal: In pre-order traversal method, the root node is visited first, then the left subtree is visited and finally the right subtree is visited².
- Post-order traversal: In post-order traversal method, the left subtree is visited first, then the right subtree is visited and finally the root node is visited³.

I hope this helps. Let me know if you have any other questions.

Source: Conversation with Bing, 5/28/2023
(1) Traversal of binary tree - TAE - Tutorial And Example. https://www.tutorialandexample.com/traversal-of-binary-tree.
(2) Tree Traversals (Inorder, Preorder and Postorder) - GeeksforGeeks. https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/.
(3) Binary Tree Traversal Methods - Computer & Information Science .... https://www.cise.ufl.edu/~sahni/cop3530/slides/lec216.pdf.
(4) Binary Search Tree Traversal – Inorder, Preorder, Post Order for BST. https://www.freecodecamp.org/news/binary-search-tree-traversal-inorder-preorder-post-order-for-bst/.
(5) Methods of Depth First Traversal and Their Applications. https://www.baeldung.com/cs/depth-first-traversal-methods.

A range search in a binary syntax tree is a search for all nodes within a given range. For example, given two values k1 and k2 where k1 < k2 and a root pointer to a Binary Search Tree, the task is to print all the keys of the tree in the range k1 to k2 in increasing order. Here is an example of how to do it in Python:

```python
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def printRange(root, low, high):
    if root is None:
        return

    if low < root.val:
        printRange(root.left, low, high)

    if low <= root.val and high >= root.val:
        print(root.val)

    if high > root.val:
        printRange(root.right, low, high)
```

This code will print all the keys of the tree in the range k1 to k2 in increasing order. ¹

I hope this helps! Let me know if you have any other questions.

Source: Conversation with Bing, 5/28/2023
(1) Print BST keys in the given range - GeeksforGeeks. https://www.geeksforgeeks.org/print-bst-keys-in-the-given-range/.
(2) Make Binary Search Tree - GeeksforGeeks. https://www.geeksforgeeks.org/make-binary-search-tree/.
(3) Binary Search Trees: BST Explained with Examples - freeCodeCamp.org. https://www.freecodecamp.org/news/binary-search-trees-bst-explained-with-examples/.
(4) Binary search tree filter values in a range - Stack Overflow. https://stackoverflow.com/questions/46918053/binary-search-tree-filter-values-in-a-range.
"""


class BSTNode:
    def search_range(self, lower_bound, upper_bound):
        # YOUR CODE HERE
        pass
        # YOUR CODE HERE

    # don't touch below this line

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

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
        return self.gamertag == other.gamertag

    def __lt__(self, other):
        return self.gamertag < other.gamertag

    def __gt__(self, other):
        return self.gamertag > other.gamertag

    def __repr__(self):
        return "".join(self.character_name)


def print_tree(bst_node, lines, level=0):
    if bst_node != None:
        print_tree(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        print_tree(bst_node.left, lines, level + 1)


def get_characters(num):
    characters = []
    for _ in range(num):
        character = Character(random.randint(0, num - 1))
        characters.append(character)
    return characters


def test(num_characters, lower_bound, upper_bound):
    characters = get_characters(num_characters)
    bst = BSTNode()
    for character in characters:
        bst.insert(character)
    print("Tree:")
    print(bst)
    print("-------------------------------------")
    print(f"Searching for characters between {lower_bound} and {upper_bound}:")
    result = bst.search_range(lower_bound, upper_bound)
    for character in sorted(result):
        print(f" - {character}")
    print("=====================================")


def main():
    random.seed(1)
    test(10, 2, 6)
    test(20, 8, 14)
    test(30, 12, 24)


main()
