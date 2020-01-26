#!C:\Users\MAHE\AppData\Local\Programs\Python\Python35-32\python.exe

import cgi,sqlite3,cgitb

conn=sqlite3.connect("userdata.db")
conn.execute("drop table logindet")
conn.execute("create table logindet (username varchar(20),password varchar(20));")


conn.execute("insert into logindet values('sush','1234');")


conn.commit()
conn.close()
