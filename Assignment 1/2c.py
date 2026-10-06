setusername = "python"
setpassword = "123456"

username = input("Enter Username: ")
password = input("Enter Password: ")

if setusername == username and setpassword == password:
    print("Success!")
else:
    print("incorrect credentials, try again!")