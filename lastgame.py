#!C:\Users\MAHE\AppData\Local\Programs\Python\Python35-32\python.exe

import cgi,sqlite3,cgitb


form=cgi.FieldStorage()

u1=str(form.getvalue("quname"))
u2=str(form.getvalue("qscore"))


conn=sqlite3.connect("userdata.db")



conn.execute("insert into leaderboard values('" +u1+ "','" +u2+ "');")



print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print("""<head></head>""")
print ('<body  style="background-color:black;">')
print('br><br><br><br><br><center><h2 style="color:white;">Successful</h2></center>')          
print ('<br><br><br><br><br><center><a href="/mainpage.html" target="_self" style="padding:30px;background-color:white;color:#1e90ff ;text-decoration:none" >Back to Login</a><center>');    
print ('</body>')
print ('</html>')
 

conn.commit()
conn.close()


#https://fussedblogger.com/
#window.open = "https://fussedblogger.com/"; 
