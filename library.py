class Library:
    def __init__(self,listofbooks):
        self.books=listofbooks 

    def displayavailablebooks(self):
        print("_______books present in this library are:__________")
        for book in self.books:

            print("\t->",book)

    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"you have been issued {bookname}. please keep it safe and return in 30 days\t")
            self.books.remove(bookname)
            return True
        else:
            print("book is already issued to others\t")
            return False

    def returnbook(self,bookname):
        self.books.append(bookname)
        print(f"thanks for returning the {bookname}")

class Student:

    def requestbook(self):
        self.book=input("enter the book you want to borrow\t")
        return self.book
    def returnbook(self):
        self.book=input("enter the book you want to return")
        return self.book
    

if __name__=="__main__":
    centrallibrary=Library(["algo",'django','clrs','python handbook for data science','how to make your own neural n/w' ])
    student=Student()
    while(True):
        wlcmmsg='''
             =======welcome to central library=======
                please choose an option:
                1.listing the bookss
                2.request a book
                3.return/add a book
                4.exit the library prompt\n
             ------------------------------------------
                '''
        print(wlcmmsg)
        a=int(input("enter a choice\t"))
        if a==1:
            centrallibrary.displayavailablebooks()
        elif a==2:
            centrallibrary.borrowbook(student.requestbook())
        elif a==3:
            centrallibrary.returnbook(student.returnbook()) 
        elif a==4:
            print("thanks for choosing central library! have a great day")
            exit()
        
        else:
            print("invalid choice!")
        
