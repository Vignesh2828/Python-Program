import mysql.connector
from datetime import date
from datetime import datetime

# enter ATM card
print(" ********************************\n")
print("PLEASE INSERT YOUR CARD ")
print("DONOT REMOVE THE CARD UNTILL TRANSACTION COMPLETE")
print(" ********************************\n")

mydb= mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root123",
    database = "atm"
)

class mysql():
    #mysql connecting
        mydb= mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root123",
        database = "atm")

print('''enter your transaction\n
            1. withdraw
            2. Balance enquiry
            3. deposit
            4. pin change
            5. bill generation''')

#balance checking
class BALANCE(mysql):
    def bal(self):
        mycursor = mydb.cursor()
        pin = input("ENTER YOUR  PIN:")
        mycursor.execute("select atm_pin from test where atm_pin='"+pin+"'")
        row = mycursor.fetchall()
        for i in row:
            a = list(i)
        if a[0] == str(pin):
            mycursor.execute("select balance from test where atm_pin='"+pin+"'")
            row = mycursor.fetchall()
            for i in row:
                a = list(i)
            print(f"YOUR CURRENT BALANCE IS:{a}")
        reciept = int(input("you want receipt yes-->1 / no-->2"))
        if reciept == 1:
            print("please collect your receipt")
            print(f''' 
                                    ******besant bank*****
                        date: {date.today()} time: {datetime.now().strftime("%H:%M:%S")}       location: Trichy
                        ac/no: xxxxxxxxxxx                  
                        
                                            current balance          
                                                 {a}             
                            
                                                 thank you

                                     ******besant bank*****''')
#cash deposit
class DEPOSIT(BALANCE):
    def dep(self):
        #self.balance=balance
        #self.deposit=deposit
        mycursor = mydb.cursor()
        pin = input("ENTER YOUR  PIN:")
        mycursor.execute("select atm_pin from test where atm_pin='"+pin+"'")
        row = mycursor.fetchall()
        for i in row:
            a = list(i)
        if a[0] == str(pin):
            a = int(input("enter the amount to be deposited: "))
            mycursor.execute("select balance from test where atm_pin='"+pin+"'")
            col = mycursor.fetchone()
            x = list(col)
            for i in x:
                z = int(i)
                c = z+a
                b = str(c)
            mycursor.execute("update test set balance = '"+b+"' where atm_pin = '"+pin+"' ")
            mydb.commit()
            print("INSERT THE AMOUNT INTO THE CASH BOX")
#withdraw amount from bank        
class WITHDRAWAL(DEPOSIT):        
    def wit(self,amount):
        mycursor = mydb.cursor()
        pin = input("ENTER YOUR  PIN:")
        mycursor.execute("select atm_pin from test where atm_pin='"+pin+"'")
        row = mycursor.fetchall()
        for i in row:
            a = list(i)
        if a[0] == str(pin):
            print(f"AMOUNT WITHDRAWAL FROM YOUR ACCOUNNT IS {amount}")
            #update_balance = a-amount
            mycursor.execute("select balance from test where atm_pin= '"+pin+"'")
            col = mycursor.fetchone()
            x = list(col)
            for i in x:
                z = int(i)
                c = z - amount
                b = str(c)
                mycursor.execute("update test set balance = '"+b+"' where atm_pin = '"+pin+"' ")
                mydb.commit()
            print(f"YOUR CURRENT BALANCE IS:{b}")
            reciept = int(input("you want receipt yes-->1 / no-->2"))
            if reciept == 1:
                print("please collect your receipt")
                print(f''' 
                                    ******besant bank*****
                        date: {date.today()} time: {datetime.now().strftime("%H:%M:%S")}       location: Trichy
                        ac/no: xxxxxxxxxxx                  
                        
                        amount                      balance
                        {amount}                 {b}        
                        
                                        thank you

                                     ******besant bank*****''')
            elif reciept == 2:
                print("thank you visit again")
        else:
            print("please enter valid pin")

#changing new pin for atm card        
class CHANGE_PIN(WITHDRAWAL):    
    def chpin(self):
        mycursor = mydb.cursor()
        pin = input("ENTER YOUR  PIN:")
        mycursor.execute("select atm_pin from test where atm_pin='"+pin+"'")
        row = mycursor.fetchall()
        for i in row:
            a = list(i)
        if a[0] == str(pin):
            mobile_number=int(input("ENTER YOUR 10 DIGIT MOBILE NUMBER:"))
        import random
        generate_otp=random.randint(0000,9999)
        print(generate_otp)
        mobile_otp=int(input("ENTER YOUR OTP NUMBER:"))
        if mobile_otp==generate_otp:
            print("******NOW YOU CAN CHANGE YOUR PIN****")#change new pin 
            new_pin=int(input("CREATE YOUR NEW PIN:"))
            mycursor.execute("select atm_pin from test where atm_pin= '"+pin+"'")
            col = mycursor.fetchone()
            x = list(col)
            for i in x:
                z = int(i)
                z = new_pin
                b = str(z)
                mycursor.execute("update test set atm_pin = '"+b+"' where atm_pin = '"+pin+"' ")
                mydb.commit()
            print("PIN CHANGED SUCCESSFULLY")
        else:
            print("PLEASE ENTER VALID OTP NUMBER!!")
#bill generation
class BILL_GENERATION:
    def transaction(self):
        self.balance=a
        import datetime
        print(f''' 
                                    ******besant bank*****
                        date: {self.date.today()} time: {datetime.now().strftime("%H:%M:%S")}       location: Trichy
                        ac/no: xxxxxxxxxxx                  
                        
                        amount              balance
                        {self.amount}              {self.balance}        thank you
                                     ******besant bank*****''')
        print("*****************RESHMA BANK*****************")


obj1=CHANGE_PIN()
user=int(input("ENTER YOUR TYPE OF TRANSACTION:"))

if user == 2:
    obj1.bal()
elif user == 3:
    #deposit=int(input("enter your amount to be deposited:"))
    obj1.dep()
elif user == 1:
    amount=int(input("ENTER THE AMOUNT FOR WITHDRAWAL:"))
    obj1.wit(amount)
elif user== 4:
    obj1.chpin()
#elif user==5:
 #   obj7.transaction()
else:
    print("ENTER VALID TRANSACTION")
