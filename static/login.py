print("--Login--")
username = input("Please enter your username:")
while len(username) == 0:
    username = input(" Please enter your username:")

password = input("Please enter your password:")
while len(password) == 0:
    password = input(" Please enter your password:")

studentlist = []
with open ("studentdetails.txt") as textfile:
    for row in textfile:
        row = row.strip ("\n")
        studentlist.append(row.split())
print (studentlist)

for everything in studentlist:       
    UserName = everything[0]
    PassWord = everything[1]

    if username == UserName and password == PassWord:
        print("<meta http-equiv="refresh" content="time; URL=ubuntu-gui/static/index.html" />")
        quizmenu()

if username == UserName and password == PassWord:
    print("")
    quizmenu()
