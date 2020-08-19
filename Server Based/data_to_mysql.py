import mysql.connector
import json
con = mysql.connector.connect(
user = "root",
password = "",#enter password here
host = "localhost",
database = "dictionary"
) #An instance of MySQL connector with credentials
cursor = con.cursor() #cursor
insert_query = """INSERT INTO dictionary (Word, Definition) VALUES (%s, %s) """
data = json.load(open("data.json"))
for word in data:
    obtained_list = data[word]
    for element in obtained_list:
        variable_data = (word, element)
    query = cursor.execute(insert_query, variable_data) #updating row by row

con.commit() #It is required to make the changes, otherwise no changes are made to the table.
cursor.close()
con.close() #closing session of the connection and cursor