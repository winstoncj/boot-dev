"""
# RED BLACK TREE - FIX INSERT
Let's finish strong by implementing the fix_insert method. When we're done here, we will have a fully functional (albeit insert-only) red-black tree. As you can see if you look at the bottom of the test suite, we'll be inserting the numbers 1-50 into our tree *in order*. A normal binary tree would break down into a single unruly branch:
# NORMAL BST (UNBALANCED WITH ORDERED INSERTIONS)
```
                  > 7
               > 6
            > 5
         > 4
      > 3
   > 2
> 1
```
# RED-BLACK BST (BALANCED WITH ORDERED INSERTIONS)
```
      > 7
   > 6
      > 5
> 4
      > 3
   > 2
      > 1
```
# ASSIGNMENT
We're nearly there! Our whole team is excited to implement this new tree, but it's not quite ready in its current state.
We need to modify the insert method slightly, let's do that first. At the end of what you have so far:
1. If the new node is a root node, make it black and just return. There's nothing to fix.
2. If the new node's grandparent is None just return. There's nothing to fix.
3. Call the new fix_insert method with the new_node as the input
We've already written the rotation functions, so the fix_insert method is mostly just responsible for recoloring the nodes, and calling the rotation methods when necessary.
1. While the new node isn't the root of the tree and its parent is red:
	1. If the parent is a right child:
		1. Set uncle to the parent's sibling
		2. If the uncle is red:
			1. Change the uncle to black
			2. Set the parent to black
			3. Set the grandparent to red
			4. Set the new node to be equal to the grandparent. This will allow the loop to continue the recoloring process up the tree
		3. Otherwise, if the uncle is black:
			1. If the new node is a left child:
				1. Set the new node to its parent
				2. Rotate the tree right around the new node
			2. Set the parent to black
			3. Set the grandparent to red
			4. Rotate the tree left around the grandparent
	2. Otherwise, if the parent is a left child:
		1. Set uncle to the parent's sibling
		2. If the uncle is red:
			1. Change the uncle to black
			2. Set the parent to black
			3. Set the grandparent to red
			4. Set the new node to its grandparent
		3. Otherwise, if the uncle is black:
			1. If the new node is a right child:
				1. Set the new node to its parent
				2. Rotate the tree left around the new node
			2. Set the parent to black
			3. Set the grandparent to red
			4. Rotate the tree right around the grandparent
2. Set the root to black

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
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.red = False
            return

        if new_node.parent.parent is None:
            return

        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                uncle = new_node.parent.parent.left
                if uncle.red:
                    uncle.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.right
                if uncle.red:
                    uncle.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
            if new_node == self.root:
                break
        self.root.red = False

    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def rotate_left(self, x):
        if x == self.nil or x.right == self.nil:
            return
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
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
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

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
    for i in range(num):
        character = Character(i)
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
    test(4)
    test(8)
    test(16)


main()
