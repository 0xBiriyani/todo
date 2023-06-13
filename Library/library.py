import json

class Library:
    def __init__(self):
        with open('books.json') as f:
            self.books = json.load(f)

    def store_book(self, book:dict):
        # get All book ids
        bookids = [book['id'] for book in self.books]

        # check if book id is in bookids
        if book['id'] in bookids:
            for _book in self.books:
                # check if book id is equal to _book id
                if _book['id'] == book['id']:
                    # increment quantity
                    _book['quantity'] += book['quantity']
        else:
            # add new books to book
            self.books.append(book)
        
        with open('books.json', 'w') as f:
            json.dump(self.books, f, indent=4)

    def retrive_book(self, id:int):
        return self.books
    
    # def __get_book_by_id(self,id:int):
    #     for book in self.books:
    #         if book['id'] == id:
    #             return book



mylib = Library()

print(mylib.books)


mylib.store_book({
    "id": 5,
    "title": "The Alchemist",
    "quantity": 10
})

print(mylib.books)