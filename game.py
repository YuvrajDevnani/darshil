

def Login():
    user_id = int(input("Enter your user id : "))
    if user_id == 100001 :
        user_pass = input("Enter your password 100001 : ")
        if user_pass == "Nikhil11":
            print("Login Successful ADMIN")

def Register():
    user_id = int(input("chosse your 6 digit ID number : "))
    user_pass1 = input("Set your password : ")
    user_pass2 = input("Re-enter your password : ")
    if user_pass1 == user_pass2 :
        print("Your account is successfully created!!\nYour user id is ->",user_id,"\nYour password is ->" + user_pass1)
    else:
        print("Try again later Buddy!")

def Forget():
    fid = input("Enter Your user id to reset password\n")
    if fid == "RA2011042010095" :
        print("Hello, Nikhil")
    elif fid == "RA2011042010084" :
        print("Hello, Darshil ")


for i in range(1) :
    print("Select the option\n1. login\n2. register\n3. Forget Password")
    var = int(input())
    if var == 1:
        Login()
    elif var == 2:
        Register()
    elif var == 3:
        Forget()
