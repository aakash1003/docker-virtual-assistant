#!/usr/bin/python36

import subprocess
print("content-type: text/html")
print()

print("hello")
z=subprocess.getoutput('date')
y=subprocess.getoutput('sudo docker ps -a')
print(z)
#print(y)
x=y.split("\n")
print("<iframe width='100%' name='myconsole'></iframe>")
print("<style>.but{background-color:grey;border-radius:10px;margin:2px;padding:3px 13px;}.but:hover{background-color:green;}</style>")
print("""
<table border='5' width ='100%'>
<tr>
       <th>NAME</th>
       <th>IMAGE</th>
       <th>STATUS</th>
       <th>START</th>
       <th>STOP</th>
       <th>TERMINATE</th>
</tr>""")
for i in x[1:]:
    if "Up" in i:
        dockstat="running"
	
    elif "Exited" in i:
        dockstat="stopped"
    else:
        dockstat="unknown"
    z = i.split()
    zname = z[-1]
    zimage = z[1]
    print(""" 
    <tr>
    <td>{}</td>
    <td>{}</td>
    <td>{}</td>
    <td><a href='http://192.168.56.3/cgi-bin/l.py?n={}'><button class="but">Start</button></a></td>
    <td><a href='http://192.168.56.3/cgi-bin/stop.py?n={}'><button class="but">Stop</button></a></td>
    <td><a href='http://192.168.56.3/cgi-bin/terminate.py?n={}'><button class="but">Terminate</button></a></td>
    <td><a href='http://192.168.56.3:4200' target='myconsole'><button class="but">Console</button></a></td>
    </tr>
    """.format(zname , zimage , dockstat , zname , zname , zname))
print("</table>")
