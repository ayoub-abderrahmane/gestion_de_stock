from dotenv import load_dotenv
import os
import mysql.connector 

#Load ".env"
load_dotenv()
host11 =  os.getenv('host')
print(host11)



 