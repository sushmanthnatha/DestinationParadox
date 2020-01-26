#!C:\Users\MAHE\AppData\Local\Programs\Python\Python35-32\python.exe

import cgi,sqlite3,cgitb


form=cgi.FieldStorage()

u1=str(form.getvalue("uname"))
u2=str(form.getvalue("pass"))

conn=sqlite3.connect("userdata.db")
#conn.execute("drop table logindet")
#conn.execute("create table logindet (username varchar(20),password varchar(20));")


#conn.execute("insert into logindet values('sush','1234');")
# conn.execute("insert into logindet values('jash','5678');")

cursor=conn.execute("select * from logindet;")


print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print("""<head></head>""")
#window.open("http://localhost:8000/l8q3.html,"homeframe");
flag=0
for row in cursor:
    if row[0] == u1 and row[1] == u2:
        print ('<body  style="background-color:black;">')
        print('<br><br><br><br><br><center><h2 style="color:white;">Successful</h2></center>')
        print ('<br><br><br><br><br><center><a href="/mainpage.html" target="_self" style="padding:20px;background-color:white;color:#1e90ff ;text-decoration:none" >Start the Game</a><center>'); 
        flag=1
        break
if flag==0:
        print ('<body  style="background-color:black;">')
        print('<br><br><br><br><br><center><h2 style="color:white;">UnSuccessful</h2></center>')
        print ('<br><br><br><br><br><center><a href="/playerlogin1.html" target="_self" style="padding:20px;background-color:white;color:#1e90ff ;text-decoration:none" >Back to Login</a><center>');
print ('</body>')
print ('</html>')
 

conn.commit()
conn.close()


#https://fussedblogger.com/
#window.open = "https://fussedblogger.com/"; 
