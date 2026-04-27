from utilis import books , issue_books
def return_books():
    book_id=int(input("enter book id"))
    if book_id in books:
        books[book_id]=issue_books[book_id]
        del books[book_id]
        print("book returned succesfully")
    else:
        print("book not returned")   