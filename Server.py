def Server(servername,dbname,username,password):
    connectstring="servname="+servername+";dbname="+dbname+";username="+username+";password="+password
    return connectstring
servername=input("servname:")
dbname=input("dbname:")
username=input("username:")
password=input("password:")

c=Server(servername,dbname,username,password)
print(c)
