#!C:\Users\MAHE\AppData\Local\Programs\Python\Python35-32\python.exe

import cgi,sqlite3,cgitb



conn=sqlite3.connect("userdata.db")




cursor=conn.execute("select * from leaderboard;")

def Sort(sub_li): 
  
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of  
    # sublist lambda has been used 
    sub_li.sort(key = lambda x: x[1]) 
    return sub_li

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print('<head></head>')
print ('<body>')


sub_li=[]
for row in cursor:
    a2=[]
    a2.append(row[0])
    a2.append(row[1])
    sub_li.append(a2)
    print('<p>'+row[0]+'  -- '+row[1]+'</p>')


print("<table style='border: 2px solid grey;padding: 10px; text-align: center;border-collapse: collapse; width:50%;padding: 10px;'><tr><th>Username</th><th>Score</th></tr>")  

def Sort(sub_li): 
    l = len(sub_li) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (sub_li[j][1] > sub_li[j + 1][1]): 
                tempo = sub_li[j] 
                sub_li[j]= sub_li[j + 1] 
                sub_li[j + 1]= tempo 
    return sub_li 

sub_li=Sort(sub_li)
i=0



for row in sub_li:
    print("<tr style='background-color: green; }><td>"+row[0]+"</td><td>"+row[1]+"</td></tr>")
print('</table>')


for row in sub_li:
    print('<p>'+row[0]+'  -- '+row[1]+'</p>')


print('</body></html>')
    
