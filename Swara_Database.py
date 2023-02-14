import mysql.connector

from tkinter import messagebox

def database(username,password,func):
    global cur
    mycon = mysql.connector.connect(
            host = "bdviswxznb9a4x9gntyw-mysql.services.clever-cloud.com",
            user = "umi4t5ojvgegwvre",
            password = "v7eLTxeCKFcIibZv0dFN",
            database = "bdviswxznb9a4x9gntyw"
        )

    try:
        cur = mycon.cursor()   # Creating an Object for working in Database
        mycon.autocommit=True

        if mycon.is_connected():  # Checking Connection
           messagebox.showinfo("Connection Successfull... ")
           check_and_continue(username,password,func)
    except:
          messagebox.showerror("Connection Failed !!!")


def check_and_continue(username,password,func):
    cur.execute("SELECT Username,Password FROM users")
    data_retrieved=cur.fetchall()      #storing username and password from database
    
    if username=="" or password=="":
        messagebox.showerror("No Data Entered","Please fill all the fields!")
    else:
        if (username,password) in data_retrieved:
            messagebox.showinfo("Success","You have Logged In Successfully.")
            func()                        
        else:
            messagebox.showerror("User not found","Username or Password is wrong")   