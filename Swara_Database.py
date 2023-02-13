import mysql.connector

mycon = mysql.connector.connect(
        host = "bdviswxznb9a4x9gntyw-mysql.services.clever-cloud.com",
        user = "umi4t5ojvgegwvre",
        password = "v7eLTxeCKFcIibZv0dFN",
        database = "bdviswxznb9a4x9gntyw"
    )

try : 
    cur = mycon.cursor()   # Creating an Object for working in Database
    mycon.autocommit=True

    if mycon.is_connected():# Checking Connection
        cur.execute("SELECT * FROM Users")
        data = cur.fecthall()
        print(data)
        for i in data:
            print(data)
        print("Connection Successfull !!!!!")    

except : 
    pass 