#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
#mydata1 = cgi.FieldStorage()
myx = mydata.getvalue("x")

#myy = mydata.getvalue("y")
if (myx[1] == "d" and myx[2]=="o" and myx[3]=="c" and myx[4]=="k" and myx[5]=="e" and myx[6]=="r"):
    output = subprocess.getoutput("sudo " + myx)
    print(output)
else:
    print("Other than docker command is not allowed to execute")
#outputy = subprocess.getoutput("sudo " + imyy)
#print(outputy)
