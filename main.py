print("Hello! You can logon in our system using the user: adimin and the password: 1234 ")
user = input("Username: ")
password = input("Password: ")

true_user = "adimin"
true_password = "1234"

if user == true_user and password == true_password:
    print("Succeed Login")
else:
    print("User or password is wrong, try again")




