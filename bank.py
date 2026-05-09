accounts={
    101:{
        "Name":"Thilak",
        "balance":100

    }
}


def deposite():
    acc_number=int(input("Enter account number"))
    if acc_number in accounts:
        amount=float(input("Enter amount"))
        accounts[acc_number]["balance"]+=amount
        print("Updated Balance after deposite:", accounts[acc_number]["balance"])
    else:
        print("not found")



def check_balance():
    acc_number=int(input("Enter account number"))
    if acc_number in accounts:
        print("Balance in your account is",accounts[acc_number]["balance"])
    else:
        print("Account not found")


def create_new_account():
    acc_number=int(input("Enter account number"))
    if acc_number in accounts:
        print("Account alreday exist")
    else:
        name=input("Enter name:")
        amount=int(input("Enter amount to deposite:"))
        accounts[acc_number]={
            "Name":name,
        "Balance":amount

        }
        print("Account created successfully")
        print("TO check your account detais")
        acc_number=int(input("Enter account number:"))
        if acc_number in accounts:  
            print("Name:",accounts[acc_number]["Name"])
            print("Balance:",accounts[acc_number]["Balance"])
            
        else:
            print("Please Enter correct account number")


def credit():
    acc_number=int(input("Enter account number:"))
    if acc_number in accounts:
        amount=float(input("Enter amount:"))
        if amount<=accounts[acc_number]["balance"]:
            accounts[acc_number]["balance"]-=amount
            print("Remaining Balance after credit:", accounts[acc_number]["balance"])
        else:
            print("Don't have any sufficient balance")
    else:
        print("Account not found")


print("Welcome to our Bank")
print("How can I help you, ")
print("1:To check balance")
print("2: To deposite amount")
print("3:To Credit amount")
print("4: To create new account")
choice=int(input("Enter choice:"))
if choice==1:
    check_balance()
elif choice==2:
    deposite()
elif choice==3:
    credit()
elif choice==4:
    create_new_account()
else:
    print("please Enter correct choice")









       
