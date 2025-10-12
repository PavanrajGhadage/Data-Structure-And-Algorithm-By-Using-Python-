class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.DELETED = -1

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key):
        initial_index = self._hash_function(key)
        index = initial_index

        while self.table[index] is not None and self.table[index] != self.DELETED:
            if self.table[index] == key:
                print(f"Key {key} already exists in the table.")
                return
            index = (index + 1) % self.size
            if index == initial_index:
                print("Hash table is full. Cannot insert key.")
                return
        self.table[index] = key
        print(f"Inserted key {key} at index {index}.")

    def search(self, key):
        initial_index = self._hash_function(key)
        index = initial_index

        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"Key {key} found at index {index}.")
                return index
            index = (index + 1) % self.size
            if index == initial_index:
                break

        print(f"Key {key} not found in table.")
        return -1

    def delete(self, key):
        initial_index = self._hash_function(key)
        index = initial_index

        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = self.DELETED
                print(f"Key {key} deleted from index {index}.")
                return
            index = (index + 1) % self.size
            if index == initial_index:
                break

        print(f"Key {key} not found for deletion.")

    def display(self):
        print("Hash Table:")
        for i in range(self.size):
            val = self.table[i]
            if val == self.DELETED:
                print(f"Index {i}: Deleted")
            else:
                print(f"Index {i}: {val}")

def main():
    size = int(input("Enter size of hash table: "))
    ht = HashTable(size)

    while True:
        print("\nOperations:")
        print("1. Insert key")
        print("2. Search key")
        print("3. Delete key")
        print("4. Display table")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            key = int(input("Enter key to insert: "))
            ht.insert(key)
        elif choice == '2':
            key = int(input("Enter key to search: "))
            ht.search(key)
        elif choice == '3':
            key = int(input("Enter key to delete: "))
            ht.delete(key)
        elif choice == '4':
            ht.display()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()