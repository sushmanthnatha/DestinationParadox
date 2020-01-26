#!C:\Users\MAHE\AppData\Local\Programs\Python\Python35-32\python.exe

import cgi,sqlite3,cgitb

conn=sqlite3.connect("userdata.db")
conn.execute("drop table signupdet")
conn.execute("create table signupdet(name varchar(20),email varchar(40),username varchar(20),password varchar(20));")


conn.execute("insert into signupdet values('sushmanth','sushmanthnatha@gmail.com','sush','1234');")


conn.commit()
conn.close()
