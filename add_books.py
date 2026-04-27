from utilis import books

def add_book():
    
    book_name=input("enter a book : ")
    book_id=int(input("enter book id : "))
    books[book_id] = book_name
    print("Book added successfully")
