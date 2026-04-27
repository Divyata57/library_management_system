from utilis import books,issue_books
def show_book():
    print("Available books ")
    
    for book_id ,book_name in books.items():
        print(f"book id:{book_id},book name:{book_name}")
    print("issued books")
    for book_id,book_name in issue_books.items():
        print(f"book id:{book_id},book name:{book_name}")    