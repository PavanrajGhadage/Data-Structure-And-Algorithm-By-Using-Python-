from collections import Counter

data1 = {"vidhi": 3, "srushti": 2, "sejal": 0, "prachi": 1}
data2 = {"DEL": 4, "END": 2, "DM": 5, "OS": 1}
data3 = {
    "vidhi": ["DEL", "DM", "DEL"],
    "srushti": ["DEL", "OS", "END"],
    "sejal": ["DEL", "DM", "END"],
    "prachi": ["DM", "OS", "END"]
}

# avg of books borrowed
total = sum(data2.values())
length = len(data2)
avg = total / length
print("Average of the books borrowed is", avg)

# highest and lowest borrowed books
max_book = max(data2, key=data2.get)
min_book = min(data2, key=data2.get)
print("The highest number of borrowed book is", data2[max_book], "and the book is", max_book)
print("The lowest number of borrowed book is", data2[min_book], "and the book is", min_book)

# number of members who haven't borrowed any book
count = sum(1 for i in data1.values() if i == 0)
print("Number of members who haven't borrowed any book is", count)

# most frequently borrowed book
def findmode(data3):
    # Flatten all lists of borrowed books into one list
    all_books = []
    for books in data3.values():
        all_books.extend(books)
    
    # Count frequency of each book
    freq = Counter(all_books)
    most_common_book, borrow_count = freq.most_common(1)[0]
    return most_common_book, borrow_count

book, count = findmode(data3)
print(f"Most frequently borrowed book is '{book}' with {count} borrows")
