"""
# INSERT
## ASSIGNMENT
Now that we have some building blocks for our hashmap, we need a way to start inserting values. Let's build the insert method and test it with different data types.

Complete the insert method. It takes a key (a string) and a value that can be of any type and stores them in the map as a  [tuple](https://www.w3schools.com/python/python_tuples.asp) .

Use the `key_to_index` method you already created to find which index the tuple should be stored in. When you create the tuple, the key should be in the tuple's index `0` and the value should be in index `1`

The hashmap list will look something like this:

```python
[
    (key, val),
    None,
    None,
    (key, val),
    None,
    ...
]
```

Where indexes with data will have a tuple, and empty indexes will be filled with None.

"""


class HashMap:
    def insert(self, key, value):
        self.hashmap[self.key_to_index(key)] = (key, value)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {i}: {str(v)}\n"
            else:
                final += f" - {i}: None\n"
        return final

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)


def test(size, items):
    hm = HashMap(size)
    print(f"Using hashmap with size: {size}")
    for item in items:
        key = item[0]
        val = item[1]
        hm.insert(key, val)
        print(f"Inserted ({key}, {val})")
    print(f"Final hashmap:\n{hm}")
    print("=====================================")


def main():
    test(1, [("apple", 1), ("banana", 2)])
    test(4, [("apple", 1), ("banana", 2)])
    test(8, [("apple", 1), ("banana", 2), ("apple", 592), ("banana", 54)])


main()
