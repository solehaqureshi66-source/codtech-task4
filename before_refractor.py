books = [
    {"title": "Python", "pages": 200},
    {"title": "DSA", "pages": 350},
    {"title": "OS", "pages": 300}
]

total = 0
for i in range(len(books)):
    total = total + books[i]["pages"]

avg = total / len(books)
print("Average pages:", avg)

for i in range(len(books)):
    if books[i]["title"] == "DSA":
        print("Book found:", books[i])