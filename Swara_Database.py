import mysql.connector
def database(username,password):
        
    mycon = mysql.connector.connect(
            host = "bdviswxznb9a4x9gntyw-mysql.services.clever-cloud.com",
            user = "umi4t5ojvgegwvre",
            password = "v7eLTxeCKFcIibZv0dFN",
            database = "bdviswxznb9a4x9gntyw"
        )


    cur = mycon.cursor()   # Creating an Object for working in Database
    mycon.autocommit=True

    if mycon.is_connected():# Checking Connection
        cur.execute("SELECT Username FROM users")
        data = cur.fetchall()
        for i in data:
            if i == username:
                print("Username Already")
        print("Connection Successfull !!!!!")    
    