import sqlite3
from tkinter import*

root = Tk()
root.title("books library")
root.geometry("500x500")
conn=sqlite3.connect("books.db")
c=conn.cursor()

def addBook():
    conn=sqlite3.connect("books.db")
    c=conn.cursor()
    
    
    queryString=f"INSERT INTO Books VALUES ('{txtBookTitle.get()}','{txtBookPrice.get()}')"
    c.execute(queryString)
    conn.commit()
    conn.close()

    txtBookTitle.delete(0,END)
    txtBookPrice.delete(0,END)

def showBooks():
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    queryString="select *, rowid FROM Books"
    c.execute(queryString)
    records = c.fetchall()
    
    display_books = ""
    for record in records:
        display_books += f"{record[0]}- Price: {record[1]}\n"
    
    lblShowBooks.config(text=display_books)
    
    conn.close()

lblTitle=Label(root,text="Books")
lblBookTitle=Label(root,text="Book Title")
txtBookTitle=Entry(root, width=50)
lblTitle.grid(row=0,column=0,pady=10)
lblBookTitle.grid(row=0 ,column=0,pady=10)
txtBookTitle.grid(row=0 ,column=1,pady=10)

lblBookPrice=Label(root,text="Book Price")
txtBookPrice=Entry(root, width=50)
lblBookPrice.grid(row=2 ,column=0,pady=10)
txtBookPrice.grid(row=2 ,column=1,pady=10)

lblShowBooks=Label(root,text="display all books")
lblShowBooks.grid(row=3,column=0,columnspan=2)

btnAddRecord=Button(root, text="add new book",command=addBook)
btnAddRecord.grid(row=4,column=0 ,columnspan=2 ,ipadx=100)

btnShowBooks= Button(root, text="show books",command=showBooks)
btnShowBooks.grid(row=5,column=0,columnspan=2 ,ipadx=100)

conn.commit()
conn.close()
root.mainloop()


