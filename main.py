from add_books import add_book
from issue import issued_book
from show import show_book
from return_book import return_books

def main():
    while True:
        print("1:add books")
        print("2:return books")
        print("3:show books")
        print("4:issue books")
        print("5:Exit")

        c=int(input("Enter Your choice : "))
        if c==1:
            print("Add books")
            add_book()
        elif c==2:
            print("return books")
            return_books()
        elif c==3:
            print("show books")
            show_book()
        elif c==4:
            print("issue books")
            issued_book()
        else:
            print("exit")
            break

if __name__=="__main__":
    main()
                            
