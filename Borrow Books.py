borroweddata= {
    "child1":["chem", "mec", "pps", "grap"],
    "child2":[],
    "child3":["mec", "pps", "grap"],
    "child4":["mec","pps"],
    }
print("Borrowed Data:", borroweddata)
total_books=0

for books in borroweddata.values():
    total_books+=len(books)
average=total_books/len(borroweddata)
print("Average is borrowed", average)

#highest and lowest
book_counts={}
for book in borroweddata.values():
    for book in books:
        if book in book_counts:
         book_counts [book] += 1
        else:
         book_counts[book] = 1
if book_counts:

 max_count = max(book_counts.values())
 min_count = min(book_counts.values())

max_BORROWED_books = [book for book, count in book_counts.items() if count== max_count]
min_borrowed_books = [book for book, count in book_counts.items() if count == min_count]


print("most borrowed book(s):", max_BORROWED_books)
print("least borrowed book(s):", min_borrowed_books)


#counting members who borrowed books
Z_borrowers = sum(1 for books in borroweddata.values() if len(books)==0)
print("members who borrowed zero books are", Z_borrowers)

#most frequently
mode_books = (borroweddata)
if mode_books:
    print("most frequently borrowed book(s):",".".join(mode_books))
else:
    print("no of books found to determine mode")