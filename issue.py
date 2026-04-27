from utilis import books , issue_books
def issued_book():
    book_id=int(input("enter book id : "))
    if book_id in books:
        issue_books[book_id]=books[book_id]
        del books[book_id]
        print("book issued sucessfully")
    else:
        print("book not issued")    
