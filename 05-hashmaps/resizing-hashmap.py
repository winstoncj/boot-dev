"""
# Resizing
Complete the following methods.

## CURRENT_LOAD()
This method returns the number of *filled buckets* in the hashmap as a percentage of the total number of buckets.

If the length of the underlying list is zero, return 1. Otherwise, divide the number of filled buckets by the length of the underlying list and return it.

## RESIZE()
If the length of the underlying hashmap is 0, make the length 1 (add a None entry).

Get the current load. If it's less then 5%, do nothing, we have plenty of space.

Otherwise, create a new empty hashmap that's 10x the size of the current one, then re-insert all the key-value pairs from the old hashmap into the new one.

## INSERT()
Call resize() before inserting to make sure there's enough space. Then, insert the key-value pair into the hashmap as normal.

"""


class HashMap:
    def insert(self, key, value):
        self.resize()

        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap = [None]
            return

        if self.current_load() < 0.05:
            return

        old_hashmap = self.hashmap.copy()
        self.hashmap = [None for i in range(len(self.hashmap) * 10)]

        for item in old_hashmap:
            if item != None:
                self.insert(item[0], item[1])

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        else:
            return len([i for i in self.hashmap if i != None]) / len(self.hashmap)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final


def test(items):
    hm = HashMap(0)
    for item in items:
        key = item[0]
        val = item[1]
        print(f"insert({key}, {val})")
        hm.insert(key, val)
        print(f"Load: {hm.current_load()}")
        print(f"Size: {len(hm.hashmap)}")
        print("-------------------------------------")
    print("=====================================")


def main():
    test(
        [
            ("apple", 1),
            ("banana", 2),
            ("cherry", 3),
            ("mango", 4),
            ("orange", 5),
            ("pear", 6),
            ("plum", 7),
            ("strawberry", 8),
            ("watermelon", 9),
        ]
    )


main()
