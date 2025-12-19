books = [
    {"title": "Python", "pages": 200},
    {"title": "DSA", "pages": 350},
    {"title": "OS", "pages": 300}
]

def calculate_average_pages(book_list):
    total_pages = sum(book["pages"] for book in book_list)
    return total_pages / len(book_list)

def find_book(book_list, title):
    for book in book_list:
        if book["title"] == title:
            return book
    return None

average_pages = calculate_average_pages(books)
print("Average pages:", average_pages)

result = find_book(books, "DSA")
if result:
    print("Book found:", result)
else:
    print("Book not found")