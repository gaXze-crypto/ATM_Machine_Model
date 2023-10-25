
User = input("Welcome to Parallex bank ATM please what is your name? \n")
if(User == "Gabe"):
    
    Pin = int(input(f"welcome {User} Please Enter your Pin\n"))
    if(Pin == 1357):
        Assistance = input("How can may we assist you?\n1.Check Balance\n2.Withdraw\n3.Recharge\n4.Deposit\n")
        
        
else:
    print(f"Sorry {User} we cannot find you in our database")
