username = input("Enter username: ")
password = input("Enter password: ")

stored_username = "admin"
stored_password = "1234"

if username == stored_username and password == stored_password:
    print("Login Successful")
else:
    print("Invalid Login")

print("\nSecurity Warning:")
print("This program uses hardcoded credentials and is vulnerable.")
