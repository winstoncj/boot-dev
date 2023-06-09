"""
# GET
## ASSIGNMENT
Now that we can insert our players and their characters into our hashmap, we need a way to retrieve that information when requested!

Complete the get method. It takes a key (a string) and returns the value stored at that location (not the whole key/value tuple).

Use the key_to_index method to find the correct index to lookup in the self.hashmap datastore, and if a value doesn't exist at that index, raise the following  [Exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions)  to indicate no key was found.

```
raise Exception("sorry, key not found")
```
"""


class HashMap:
    def get(self, key):
        return (
            self.hashmap[self.key_to_index(key)][1]
            if self.hashmap[self.key_to_index(key)]
            else Exception("sorry, key not found")
        )

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def insert(self, key, value):
        i = self.key_to_index(key)
        self.hashmap[i] = (key, value)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final


def test(size, items, keys_to_get):
    hm = HashMap(size)
    for item in items:
        key = item[0]
        val = item[1]
        hm.insert(key, val)
    print(f"Hashmap:\n{hm}")
    print("-------------------------------------")
    for key in keys_to_get:
        try:
            val = hm.get(key)
            print(f"get({key}) -> {val}")
        except Exception as e:
            print(f"get({key}) -> {e}")
            continue
    print("=====================================")


def main():
    test(
        256,
        [
            ("apple", 1),
            ("banana", 2),
            ("cherry", 3),
            ("mango", 4),
        ],
        ["apple", "banana", "garbage"],
    )
    test(
        512,
        [
            ("golang", 1),
            ("python", 2),
            ("java", 3),
            ("javascript", 4),
            ("rust", 5),
            ("c", 6),
            ("c++", 7),
        ],
        ["golang", "python", "garbage"],
    )


main()
