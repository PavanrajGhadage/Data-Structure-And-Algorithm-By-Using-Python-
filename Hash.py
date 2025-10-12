class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # List of empty lists (chaining)

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        # Check if key already exists and update
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Updated key {key} with value {value}")
                return
        # Else insert new key-value pair
        self.table[index].append([key, value])
        print(f"Inserted key {key} with value {value}")

    def search(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Not found

    def delete(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                print(f"Deleted key {key}")
                return
        print(f"Key {key} not found for deletion.")

    def display(self):
        print("Hash Table:")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

ht = HashTable()

ht.insert(15, "apple")
ht.insert(25, "banana")  # Collision with 15
ht.insert(35, "cherry")  # Collision again

print("Search 25:", ht.search(25))  # Output: banana
ht.delete(25)
print("Search 25 after deletion:", ht.search(25))  # Output: None

ht.display()
Output
Inserted key 15 with value apple
Inserted key 25 with value banana
Inserted key 35 with value cherry
Search 25: banana
Deleted key 25
Search 25 after deletion: None
Hash Table:
Index 0: []
Index 1: []
Index 2: []
Index 3: []
Index 4: []
Index 5: [[15, 'apple'], [35, 'cherry']]
Index 6: []
Index 7: []
Index 8: []
Index 9: []
