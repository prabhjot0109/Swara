import mysql.connector
from tkinter import messagebox

class Database:
    #Checking Connection with Database
    try:
        mycon = mysql.connector.connect(
                host = "bdviswxznb9a4x9gntyw-mysql.services.clever-cloud.com",
                user = "umi4t5ojvgegwvre",
                password = "v7eLTxeCKFcIibZv0dFN",
                database = "bdviswxznb9a4x9gntyw"
        )

        # Creating an Object for working in Database
        cur = mycon.cursor()

        #If Connection is Successfull 
        if mycon.is_connected(): 
                messagebox.showinfo("Connection Successfull","Connected to database Successfully.")


    #If Connection is Unsuccessful        
    except mysql.connector.Error:
            messagebox.showerror("Connection Failed","We can't connect to database at this movemnt.\nPlease Try Again Later.")
            quit()
        
    
    #Function for Logging In User
    def login(self,userEntry,passEntry,func):
            
            #Getting Username And Password entered
            self.password = passEntry.get()
            self.username = userEntry.get()

            self.cur.execute("SELECT Username,Password FROM users")
            self.data_retrieved=self.cur.fetchall()       #Storing username and password from database

            #Condition for empty Entry Box
            if self.username == "" or self.password == "":
                    messagebox.showerror("No Data Entered","Please fill all the fields!")

            else:
                    #Correct Creditionals
                    if (self.username,self.password) in self.data_retrieved:
                            messagebox.showinfo("Success","You have Logged In Successfully.")
                            func()               
                    #Incorrect Creditionals                         
                    else:
                            messagebox.showerror("User not found","Username or Password is Incorrect") 
    
    #Function for Checking New Users Email Id And Password
    def regCheck(self,mobileEntry,emailEnrtry,func):
        #Getting Mobile No. and Email Id entered
        self.mobile_no = mobileEntry.get()
        self.email = emailEnrtry.get()

        #Getting data from Table 
        self.cur.execute("SELECT Mobile_no,Email FROM users")
        self.data = self.cur.fetchall()

        #Checking Details
        #Invalid Input of Mobile No.
        if self.mobile_no.isdigit() == False:
            messagebox.showerror("Invalid Input","Please Enter Valid Mobile No. \nIn Digits")

        elif len(self.mobile_no) != 10:
            messagebox.showerror("Invalid Input","Please Enter Valid Mobile No. \nIt should be of 10 digits  ")
        
        #If Mobile No. satisfies the above conditons
        else:
            for current in self.data:
                if (self.mobile_no in current) and (self.email in current):
                        messagebox.showerror("Already Exists","Email and Phone alread exist")
                    
                elif (self.mobile_no not in current) and (self.email in current):
                        messagebox.showerror("Already Exists","Email Already Exists")
                    
                elif (self.mobile_no in current) and (self.email not in current):
                        messagebox.showerror("Already Exists","Mobile No. Already Exists")
                    
                #Enabling the disaled Entries after verification is complete
                else:
                        func()
            
        

           
     

                  
