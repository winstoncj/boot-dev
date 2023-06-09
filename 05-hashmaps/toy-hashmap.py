"""
# TOY HASH MAP
Let's build a toy hash map in Python. In the real world, you would almost always use the built-in  [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)  if you need a hash map. However, just using a dictionary doesn't teach us about what's going on under the hood!

As usual, we'll be building out a class, and we'll call it HashMap. The map will use a simple Python List underneath to store the data, and we'll call that list hashmap. As you can see in the provided constructor, we are initializing the hashmap to the size provided.

## ASSIGNMENT
We have been receiving great feedback on "Fantasy Quest"! We have been making significant progress in speeding things up and making the game more accessible. The friends list feature has been well received. However, we've found that our players often don't know the names of their friends' characters. Our players would like to lookup their friend's character by their friend's real name. Let's build a hashmap that maps real names to character names.

Let's get started on the building blocks of our hashmap.

Before we can build the `insert` and `get` methods, we need a way to map an arbitrary key (in our case just `string`s) to an index in the map.
Implement the hashing function, which we'll call `key_to_index`. It should:

1. Take a key (string) as input
2. Add the ASCII values of all the characters in the string
3. Mod ( % ) the sum by the size of the hashtable to get an index which should be an int
4. Return the index

"""


class HashMap:
    def key_to_index(self, key):
        return sum([ord(c) for c in key]) % len(self.hashmap)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)


def test(size, keys):
    hm = HashMap(size)
    print(f"Using hashmap with size: {size}")
    for key in keys:
        index = hm.key_to_index(key)
        print(f"{key} hashes to index {index}")
    print("=====================================")


def main():
    test(4, ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
    test(256, ["hello", "world"])
    test(512, ["golang", "python", "java", "javascript", "rust", "c", "c++"])


main()
