import sqlite3

class Database:

    def __init__(self,db):     #it is a constructor and self is the instance of the object calling this function
        conn=sqlite3.connect(db)
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Book(id INTEGER PRIMARY KEY,title text,author text,isbn INTEGER,year INTEGER)")
        conn.commit()
        conn.close()

    def insert(title,author,year,isbn):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO Book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        conn.commit()
        conn.close()

    def show(self):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM Book")
        rows=cur.fetchall()
        conn.close()
        return rows

    def search(title="",author="",year="",isbn=""):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM Book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=cur.fetchall()
        conn.close()
        return rows

    def delete(id):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM Book WHERE id=?",(id,))
        conn.commit()
        conn.close()

    def update(id,title,author,year,isbn):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        year,isbn=isbn,year         #there was a problem in updating the Entry in the database,
                                    #the year and isbn were getting swapped,so i swapped them again
        cur.execute("UPDATE Book SET title='%s' ,author='%s', year=%s, isbn=%s WHERE id=%s"%(title,author,year,isbn,id))
        conn.commit()
        conn.close()

#connect()
#insert("SITA","Amish",2006,892766)
#delete(6)
#print(search(author="Dan Brown"))
#print(show())
#update(7,"SITA","Amish",2015,999888)
#print(show())
