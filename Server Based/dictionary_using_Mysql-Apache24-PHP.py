import mysql.connector

#Establishing Connection with MySQL Database
con = mysql.connector.connect(
user = "root",
password = "", #enter password here
host = "localhost",
database = "dictionary"
)

#Defining the cursor
cursor = con.cursor()

word=input("Enter the word: ")
query = cursor.execute("SELECT Definition FROM Dictionary WHERE Word = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")