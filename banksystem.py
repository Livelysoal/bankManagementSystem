import random
from pathlib import Path
import json

class Bank:
    storage = "database.json"
    data =[]

    try:
        if Path(storage).exists() :
            with open(storage,"r") as fs:
                data = json.loads(fs.read())
         
        else:
            print("Sorry the database do not exist in your  directory")
        
    except Exception as e:
        print(f"something went wrong as {e}")

    @classmethod
    def __update(cls):
        with open(cls.storage,"w") as fs:
            json.dump(cls.data, fs)

    def createaccount(self):
        try:

            user = {"name":input("enter your name "),
                    "age": input("enter you age "),
                    "email": input("enter your email "),
                    "phone": input("enter your phone number "),
                    "pin": input("enter the pin for your account ")}
            if (int)(user["age"])<18:
                print("you are not eligible to create the accoun as you are underage")
                return   #to avoid checking next cases
            elif "@"  not in user["email"] or not  user["email"].endswith(".com"):
                print("please enter a valid email address")
                return
            elif len(user["phone"]) !=10:
                print(" please enter a valid mobile number")
                return
            elif len(user["pin"])!= 4:
                print("please enter a 4 digit pin only")
                return
            else:
                user["accountno"] = random.randint(100000,10000000)
                user["balance"] = 0.0
                print("your account have been created successfully!!!!")
                print("plese note down the account details given below for future refrences.....")
                print("**************************") 
                for i in user:
                    print(f"{i}:{user[i]}")          
                print("**************************")
                Bank.data.append(user)
                Bank.__update()
        except Exception as e:
            print(f"something went wrong as {e}")

    def deposit(self):
        try:
            acc = int(input("please enter the account number at which you want to deposit the money: "))
            for i in Bank.data:
                if(i["accountno"]==acc):
                    amt = float(input("enter the amount you want to deposit in your bank account"))
                    if amt<0:
                        print("please enter a valid amount to deposit")
                    else:
                        i["balance"]+=amt
                        Bank.__update()
                        print(f"your updated balance is : {i['balance']}")
                        print(i)
                        break
            else:
                print("account do not exist")
        except Exception as e:
            print(f"something wrong as {e}")

    def withdraw(self):
        try:
            acc = int(input("please enter the account number from which you want to withdraw the money: "))
            for i in Bank.data:
                if(i["accountno"]==acc):
                    p = input("please enter the pin of your bank account")
                    if(i["pin"]==p):
                        amt = float(input("enter the amount you want to withdraw from your bank account"))
                        if amt<0:
                            print("negitive money cannot be withdrawn..")
                        elif amt<= i["balance"]:
                            i["balance"]-=amt
                            print("money withdraw successfull")
                            print(f"your updated balance is : {i['balance']}")
                            Bank.__update()
                            break
                        else:
                            print("your bank account do not have that much money...")   
                    else:
                        print("wrong pin")
                        break      
            else:
                print("account do not exist")
        except Exception as e:
            print(f"something wrong as {e}")
        
    def accdetails(self):
        try:
            acc = int(input("please enter the account number you want to see details of: "))
            for i in Bank.data:
                if(i["accountno"]==acc):
                    p = input("please enter the pin of your bank account")
                    if(i["pin"]==p):
                            self.printdetails(i)
                            break
                    else:
                        print("you have entered the wrong pin")
                
            else:
                print("account do not exists")
        except Exception as e:
            print(f"something went wrong as {e}")



    def printdetails(self,user):
            for key in user:
                print(f"{key}:{user[key]}")



    def updetails(self):
        try:
            acc = int(input("please enter the account number you want to see details of: "))
            for i in Bank.data:
                if(i["accountno"]==acc):
                    p = input("please enter the pin of your bank account")
                    if(i["pin"]==p):
                        print("details you can update are:")
                        print("1.email address")
                        print("2.phone number")
                        print("3.pin")
                        ch = int(input("enter the choice from above "))

                        if ch ==1:
                            new_em = input("please enter the new email address: ")
                            if "@"  not in new_em or not  new_em.endswith(".com"):
                                print("please enter a valid email address")
                            else:
                                i["email"]= new_em
                                Bank.__update()
                                print("your updated bank details are as follows: ")
                                self.printdetails(i)
                                break

                        elif ch ==2:
                            new_ph = input("please enter the new phone number: ")
                            if len(new_ph) !=10:
                                print(" please enter a valid mobile number")
                            else:
                                i["phone"]= new_ph
                                Bank.__update()
                                print("your updated bank details are as follows: ")
                                self.printdetails(i)
                                break
                    
                        elif ch ==3:
                            new_pi = input("please enter the new pin: ")
                            if len(new_pi)!= 4:
                                print("please enter a 4 digit pin only ")
                            else:
                                i["pin"]= new_pi
                                Bank.__update()
                                print("your updated bank details are as follows: ")
                                self.printdetails(i)
                                break
                        
                        else:
                            print("please enter a valid choice")
            else:
                print("account do not exists")

      

        except Exception as e:
            print(f"something went wrong as {e}")


print("***********************************************")
print("     welcome to laximi chit fund bank..😁😊   ")
print("***********************************************")
while(True):
    print("1.create a new bank account")
    print("2.deposit money in account")
    print("3.withdraw money from account")
    print("4.view accoount details")
    print("5.update account details")
    print("6.exit")
    choice  = int(input("enter your choice from the above list "))
    bank = Bank()
    try :
        if(choice == 1):
            bank.createaccount()
        
        elif(choice ==2):
            bank.deposit()
        
        elif choice ==3:
            bank.withdraw()
        
        elif choice ==4:
            bank.accdetails()

        elif choice ==5:
            bank.updetails()

        elif choice ==6:
            print("thank you visiting our bank.....")
            break
        else:
            print("please enter a valid choice")
        
    except Exception as e:
        print(f"something went wrong as {e}")




    