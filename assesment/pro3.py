books = [ ]
no = int(input("enter number of books: "))

for i in range(no):
    print("enter details for book", i + 1)

    book_id = input("enter book ID: ")
    title = input("enter title: ")
    author = input("enter author: ")
    price = float(input("enter price: "))
    book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "price": price
    }

    books.append(book)

print("all book details:")

for book in books:
    print(
        book["book_id"],
        book["title"],
        book["author"],
        book["price"]
    )
most_expensive = books[0]

for book in books:
    if book["price"] > most_expensive["price"]:
        most_expensive = book

print("most expensive book:")
print(
    most_expensive["book_id"],
    most_expensive["title"],
    most_expensive["author"],
    most_expensive["price"]
)
cheapest = books[0]

for book in books:
    if book["price"] < cheapest["price"]:
        cheapest = book

print("cheapest book:")
print(
    cheapest["book_id"],
    cheapest["title"],
    cheapest["author"],
    cheapest["price"]
)

total = 0

for book in books:
    total = total + book["price"]

average = total / no

print("vverage book price:")
print(average)


print("books with price greater then verage:")

for book in books:
    if book["price"] > average:
        print(
            book["book_id"],
            book["title"],
            book["author"],
            book["price"]
        )