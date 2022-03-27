BOOKS = [
    {'title': 'Book of Fooos', 'author': 'Foo', 'year': 1111},
    {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611},
    {'title': 'The Tempest', 'author': 'Shakespeare', 'year': 1611},
    {'title': 'Book of Foos Barrrs', 'author': 'FooBar', 'year': 2222},
    {'title': 'Still foooing', 'author': 'FooBar', 'year': 333},
    {'title': 'Happy Foo', 'author': 'FooBar', 'year': 4444},
]


def find_where(books, query):
    default = object()
    for item in books:
        for key, value in query.items():
            if item.get(key, default) != value:
                break
        else:
            return item


print(find_where(BOOKS, {}))
print(find_where(BOOKS, {'year': 1111}))
print(find_where(BOOKS, BOOKS[2]))
