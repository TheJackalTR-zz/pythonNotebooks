print("""********************
User Login
********************
""")

sys_username = 'aryen'
sys_password = "12345"

username = input("Enter Username:")
password = input("Enter Password:")

if username == sys_username and password != sys_password:
    print("Password is wrong")
elif username != sys_username and password == sys_password:
    print("Username is wrong")
elif username != sys_username and password != sys_password:
    print("Username and Password are wrong")
else:
    print("Welcome {}".format(username))
