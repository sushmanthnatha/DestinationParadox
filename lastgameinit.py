#!C:\Users\MAHE\AppData\Local\Programs\Python\Python35-32\python.exe

import cgi,sqlite3,cgitb

conn=sqlite3.connect("userdata.db")
conn.execute("drop table leaderboard")
conn.execute("create table leaderboard (username varchar(20),score varchar(20));")


conn.execute("insert into leaderboard values('sush','500');")
conn.execute("insert into leaderboard values('jash','900');")


conn.commit()
conn.close()
