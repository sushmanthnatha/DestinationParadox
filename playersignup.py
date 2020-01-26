#!C:\Users\MAHE\AppData\Local\Programs\Python\Python35-32\python.exe

import cgi,sqlite3,cgitb


form=cgi.FieldStorage()

u1=str(form.getvalue("qname"))
u2=str(form.getvalue("qemail"))
u3=str(form.getvalue("quname"))
u4=str(form.getvalue("qpass"))

conn=sqlite3.connect("userdata.db")




# conn.execute("insert into logindet values('jash','5678');")

cursor=conn.execute("select * from signupdet;")



print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print("""<head></head>""")
#window.open("http://localhost:8000/l8q3.html,"homeframe");
flag=1
for row in cursor:
    if row[2] == u3 :
        print ('<body  style="background-color:black;">')
        print('br><br><br><br><br><center><h2 style="color:white;">UnSuccessful. Username already exists</h2></center>')
        print ('<br><br><br><br><br><center><a href="/playersignup.html" target="_self" style="padding:30px;background-color:white;color:#1e90ff ;text-decoration:none" >Back to Signup</a><center>'); 
        flag=0
        break

    
if flag == 1 :
        conn.execute("insert into signupdet values('" +u1+ "','" +u2+ "','" +u3+ "','" +u4+ "');")
        conn.execute("insert into logindet values('" +u3+ "','" +u4+ "');")     
        print ('<body  style="background-color:black;">')
        print('br><br><br><br><br><center><h2 style="color:white;">Successful</h2></center>')          
        print ('<br><br><br><br><br><center><a href="/playerlogin1.html" target="_self" style="padding:30px;background-color:white;color:#1e90ff ;text-decoration:none" >Back to Login</a><center>');
       
print ('</body>')
print ('</html>')
 

conn.commit()
conn.close()


#https://fussedblogger.com/
#window.open = "https://fussedblogger.com/"; 
