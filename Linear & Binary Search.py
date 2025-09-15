#In an e-commerce system, customer account IDs are stored in a list, and you are tasked with writing a program that implements the following:
#• Linear Search: Check if a particular customer account ID exists in the list.
#• Binary Search: Implement Binary search to find if a customer account ID exists, improving the search efficiency over the basic linear


names = [] # Initialize an empty list

#Ask user how many names to add

count = int(input("How many names do you want to add? "))

#Take inputs and append each name to the list

for i in range(count):
    name = input(f"Enter a Name {i+1}: ")
    names.append(name)

print("Updated list:", names)


# ----- Linear Search -----
#Linear search for a name in the list

search_name = input("Enter the name to search for: ")

found = False
for i in range(len(names)):
    if names[i] == search_name:
        print(f"Name '{search_name}' found at position {i}")
        found = True
        break

if not found:
    print("Name '{search_name}' not found in the list.")


# ----- Binary Search -----
# List must be sorted for binary search
names.sort()
print("Sorted list for Binary Search:", names)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

search_name_bin = input("Enter the name to search for (Binary Search): ")
index = binary_search(names, search_name_bin)
if index != -1:
    print(f"Name '{search_name_bin}' found at position {index} (Binary Search)")
else:
    print(f"Name '{search_name_bin}' not found in the list. (Binary Search)")