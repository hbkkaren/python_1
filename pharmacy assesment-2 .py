
import mysql.connector
conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "pharmacy")
cur = conn.cursor()


class Pharmacy:

    def register_logg(self,username,password,rpassword):
        import mysql.connector
        conn = mysql.connector.connect(host = "localhost",user = "root",password = "",database = "pharmacy")
        while True:
            self.user = username
            self.pa = password
            self.rpa =rpassword
            if self.pa==self.rpa:
                query = "insert into passowords(username,password) value(%s,%s)"
                args = (self.user,self.pa)
                cur = conn.cursor()
                cur.execute(query,args)
                conn.commit()
                conn.close()
                print("\n")
                print(" you logged in succsessfully")
                print("\n")
                break

            else:
                print("\n")
                print("Your repeat_password is wrong :")
                

    def register(Self,Mname,Pname):
        Self.Mname = Mname
        Self.Pname = Pname
        cur = conn.cursor()
        query  = "insert into managertable(Manager_Name,Pharmacy_Name) values(%s,%s)"
        args = (Self.Mname,Self.Pname)
        cur.execute(query,args)
        conn.commit()
        conn.close()
    
    
    def login(self,username,Password):
        passlist = []
        self.name = username
        self.password = Password
        cur = conn.cursor()
        query= "select * from passowords where username=%s and password = %s"
        args = (self.name,self.password)
        cur.execute(query,args)
        row = cur.fetchall()
        for i in row:
        
            if (self.name,self.password) == i:
                
                return True
            

class Admin(Pharmacy):
    def __init__(self):
        print("\n\n")
        print("1. Press  for Register : ")
        print("2. Press  for login : ")
        print("3. Press  for View all Manager : ")
        print("4. Press  for View all Medicine : ")
        print("5. press  for exit : ")
        print("\n\n")
    
    def view_manager(self):
        cur=conn.cursor()
        query ="select Manager_Name from managertable"
        cur.execute(query)
        row=cur.fetchall()
        show = []
        for i in row:
            show.append(i)
        print(show,"\n")    
        
        cur.close()
    
    def view_medicine(self):
        cur= conn.cursor()
        query ="select SRNO,medicine_name,Added_date,price from medicine "
        cur.execute(query)
        med =cur.fetchall()
        for i in med:
            print(i,"\n")
        cur.close()

    

class Phrmacy_manager(Pharmacy):
    def __init__(self) -> None:
        super().__init__()   
        print("\n\n")
        print("1. press for Register")
        print("2. Add medicine ")
        print("3. press for  View Medicine  ")
        print("4. press for view Delete Medicine")
    
    def ADD_medicine(self,medicine_name,qty,Added_date,price):
        
        self.medicine_name = medicine_name
        self.qty = qty
        self.Added_date = Added_date
        self.price = price

        cur =conn.cursor()
        query = "insert into   medicine(medicine_name,qty,Added_date , price ) values(%s,%s,%s,%s)"
        args = (self.medicine_name,self.qty,self.Added_date,self.price)
        cur.execute(query,args)
        
        cur.close()
    
    def view_Pharma(self):
        cur= conn.cursor()
        query ="select * from medicine "
        cur.execute(query)
        
        med =cur.fetchall()
        
        for i in med:
            print(i,"\n")
        cur.close()





while True:
    
    print(" choose one opetion  ")
    print("1 Press for Admin")
    print("2 Press for Pharmacy Manager")
        
    
    input1 = int(input("please write your choice here : "))
    
        
    if input1 == 1:
        print("welcome to the admin panal")
        ad = Admin()
        
        Choise = int(input(" write your Choise  : "))
        print("\n")
        
        if Choise == 1 :
            
            while True:
                print("\n\n")
                print( "this is register page ")
                
                print("\n")
                
                username = input("Please enter your user Name :")
                print("\n")
                password = input("please enter your password : ")
                print("\n")
                rpassword = input("please repeat your password : ")
                print("\n")

                ad.register_logg(username,password,rpassword)
                Mname = input("Write Manager name here : ")
                Pname = input("write Pharmacy name here : ")

                ad.register(Mname,Pname)
                print("\n")
                exit =input("do you want  to add another manager (y/n)")
                
                if exit == 'y':
                    continue
                else:
                    break

        elif Choise== 2 :
        
            print("\n")
            print("This is loggin page ")
            print("\n")
            print("you have three try to loggin(type carfully)")
            print("\n")

            username = input("please write your user Name : ")
            login = input("please write your password : ") 
            
            

        elif Choise==3:
            
            print("\n\n")
            views = Admin()
            print("\n")
            print("Password is required for loggin ")
            username = input("enter your username:")
            password = input("enter your password: ")
            ad =Admin()
            ad.login(username,password)
            
            if ad.login(username,password)== True:
                ad.view_manager()
            else:
                print("Your password is wrong (please re-try)")
                
        
        
        elif Choise==4:
            print("\n\n")
            views = Admin()
            print("\n")
            print("Password is required for loggin ")
            username = input("enter your username:")
            password = input("enter your password: ")
            ad =Admin()
            ad.login(username,password)
            
            if ad.login(username,password)== True:
                ad.view_medicine()
            else:
                print("Your password is wrong (please re-try)")
                
    elif input1== 2:
        
        print("\n")
        print("This is Pharmacy manager system ")
        phrma = Phrmacy_manager()
        

        print("\n")
        Choise_pharma = int(input("enter your choise here :"))
        print("\n")

        if  Choise_pharma == 1:
            username = input("Please enter your user Name :")
            print("\n")
            password = input("please enter your password : ")
            print("\n")
            rpassword = input("please repeat your password : ")
            print("\n")

            Pharmacy.register_logg(username,password,rpassword)
            Mname = input("Write Manager name here : ")
            Pname = input("write Pharmacy name here : ")

            ad.register(Mname,Pname)
            print("\n")
            exit =input("do you want  to add another manager (y/n)")
            
            if exit == 'y':
                continue
            else:
                break

        
        elif Choise_pharma ==2:
            print("\n\n")
            views = Admin()
            print("\n")
            print("Password is required for loggin ")
            username = input("enter your username:")
            password = input("enter your password: ")
            ad =Admin()
            ad.login(username,password)
            if ad.login(username,password)== True:
                ph = Phrmacy_manager()
                print("\n")
                SRNO= int(input("please enter your srno : "))
                medicine_name =input("please write your medicine : ")
                qty = input("type your qty for medicine : ")
                Added_date = input("type Date :")
                price = int(input("write your prise here : ")) 
                
                ph.ADD_medicine(medicine_name, qty,Added_date,price)
                
                print('\n\n')
                print("your data  added successfully ")
            else:
                print("Your password is wrong (please re-try)")
                
        
        elif Choise_pharma == 3:
            username = input("enter your username:")
            password = input("enter your password: ")
            ad =Admin()
            ad.login(username,password)
            ph = Phrmacy_manager()

            if ad.login(username,password)== True:
                ph.view_Pharma()
                
            else:
                print("Your password is wrong (please re-try)")
           
            
            

            



            

            


            


        
        


        
            
            



        