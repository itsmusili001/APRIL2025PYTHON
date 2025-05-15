import sqlite3
from tkinter import*

root = Tk()
root.title("LIBRARY")
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
        display_books += f"{record[0]}-{record[1]} {record[2]}\n"

    lblShowBooks=Label(root,text=display_books,justify="left")
    lblShowBooks.grid(row=9,column=0,columnspan=2)

    
    lblShowBooks.config(text=display_books)
    conn.close()

def deleteBook():
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    queryString="DELETE FROM BOOKS WHERE oid ="+txtBookId.get()
    c.execute(queryString)
    conn.commit()

def updateBook():
    updateWindow= Tk()
    updateWindow.title("update book record")
    updateWindow.geometry("500x500")
    bookId=txtBookId.get()
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    queryString="SELECT* FROM BOOKS WHERE oid =" +txtBookId.get()
    c.execute(queryString)
    records = c.fetchall()
    
    lblTitleUpdate =Label(updateWindow,text="update Books")
    lblBookTitleUpdate=Label(updateWindow,text="update Book Title")
    txtBookTitleUpdate=Entry(updateWindow, width=50)
    lblTitleUpdate.grid(row=0,column=0,pady=10)
    lblBookTitleUpdate.grid(row=0 ,column=0,pady=10)
    txtBookTitleUpdate.grid(row=0 ,column=1,pady=10)

    lblBookPriceUpdate =Label(updateWindow,text="update Book Price")
    txtBookPriceUpdate =Entry(updateWindow, width=50)
    lblBookPriceUpdate.grid(row=2 ,column=0,pady=10)
    txtBookPriceUpdate.grid(row=2 ,column=1,pady=10)

    for record in records:
        txtBookTitleUpdate.insert(0,record[0])
        txtBookPriceUpdate.insert(0,record[1])
    def saveChanges():
        conn = sqlite3.connect("books.db")
        c = conn.cursor()
        btitle=txtBookTitleUpdate.get()
        bprice = txtBookPriceUpdate.get()
        queryString = f"""UPDATE Books SET 
        BookTitle = {btitle},
        BookPrice = {bprice},
        WHERE oid ={bookId},
        """



        # queryString="""UPDATE BOOKS SET
        # BookTitle=:btitle,
        # BookPrice=:bprice,
        # WHERE rowid = oid
        # """,{
        #     'btitle':txtBookTitleUpdate.get(),
        #     'bprice':txtBookPriceUpdate.get()
        # 
        c.execute(queryString)
        conn.commit()
        conn.close()
        
    btnUpdateBook=Button(updateWindow, text="save changes",command=saveChanges)
    btnUpdateBook.grid(row=3,column=0 ,columnspan=2 ,pady=20)

    conn.commit()
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

lblBookId=Label(root,text = "Enter book ID")
lblBookId.grid(row=6,column=0,pady=10)
txtBookId=Entry(root,width=50)
txtBookId.grid(row=6,column=1,pady=10)

btnAddRecord=Button(root, text="add new book",command=addBook)
btnAddRecord.grid(row=4,column=0 ,columnspan=2 ,ipadx=90)

btnShowBooks= Button(root, text="show books",command=showBooks)
btnShowBooks.grid(row=5,column=0,columnspan=2 ,ipadx=100)

btnDeleteBook= Button(root,text="delete book record",command=deleteBook)
btnDeleteBook.grid(row=7,column=0,columnspan=2,ipadx=90)

btnUpdateBook=Button(root,text="update books",command=updateBook)
btnUpdateBook.grid(row=8,column=0,columnspan=2,ipadx=100)


conn.commit()
conn.close()
root.mainloop()


