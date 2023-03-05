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
        
    
    #Function for logging in User
    def login(self,userEntry,passEntry,func):
            
            #Getting Username And Password entered
            self.password = passEntry.get()
            self.username = userEntry.get()

            self.cur.execute("SELECT Username,Password FROM users")
            data_retrieved=self.cur.fetchall()       #Storing username and password from database

            #Condition for empty Entry Box
            if self.username == "" or self.password == "":
                messagebox.showerror("No Data Entered","Please fill all the fields!")

            else:
                #Correct Creditionals
                if (self.username,self.password) in data_retrieved:
                        messagebox.showinfo("Success","You have Logged In Successfully.")
                        func()               
                #Incorrect Creditionals                         
                else:
                        messagebox.showerror("User not found","Username or Password is wrong") 
    
    #Function for Creating User
                  
