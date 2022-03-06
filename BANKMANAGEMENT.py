
def accept_info():
    accept_info.ac_num = int(input("Please Enter your Account number :"))
    accept_info.ac_bal = int(input("Please Enter your Account balance :"))
    accept_info.ac_pin = int(input("Please Enter your Pin :"))

# function for deposit amount

def deposite_amt():
    amt_add = int(input("Enter amount to deposite in account :"))
    accept_info.ac_bal = accept_info.ac_bal + amt_add
    print("Amount deposited sucessfully, now your account balance is" ,accept_info.ac_bal)

# function for withdrawl user amount
def withdrawl_amt():
    print("Please enter the Pin :")
    t_pin = int(input())
    if t_pin == accept_info.ac_pin:
        amt = int(input("Enter amount to withdraw from your account :"))
        if amt > accept_info.ac_bal:
            print("Hard luck ! Insufficient Funds")
        else:
            accept_info.ac_bal = accept_info.ac_bal - amt
            print("Amount sucessfully withdrawn,now your balance is" ,accept_info.ac_bal)
    else:
        print("Invalid Password")

def change_password():
    old_pass= int(input("Enter old password to change password :"))
    if old_pass== accept_info.ac_pin :
        new_pass = int(input("Enter new password to set :"))
        accept_info.ac_pin = new_pass
        print("Now your new password is " ,new_pass)
    else :
        print("Incorrect password")


def show_bal():
    password = int(input("Please Enter your password to see balance :"))
    if password ==accept_info.ac_pin:
        print("Your account balance is " ,accept_info.ac_bal)
    else:
        print("Invalid password ")




print("________Welcome to our ICIC bank service_____________ \n")

while True:
    print("1 : ACCEPT INFO :")
    print("2 : DEPOSITE AMOUNT :")
    print("3 : WITHDRAWL AMOUNT :")
    print("4 : CHANGE  PIN PASSWORD :")
    print("5 : SHOW ACCOUNT BALANCE :")
    print("6 : SHOW ACCOUNT INFO:")
    print("7 : Exit ")

    print("Provide your choice :")
    ch = int(input())
    if  ch ==1:
        accept_info()
    elif ch ==2:
        deposite_amt()
    elif ch ==3:
        withdrawl_amt()
    elif ch ==4:
        change_password()
    elif ch ==5:
        show_bal()
    elif ch ==6:
        ShowAccountinformation()
    elif ch ==7:
        exit(0)

