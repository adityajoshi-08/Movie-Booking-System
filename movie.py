'''

CREATING A NEW TABLE---> 


create table abhinav(Movie_Name VARCHAR(100), Date DATE, 
Ticket_Sold INTEGER, Total_Available INTEGER, 
Ticket_Left INTEGER GENERATED ALWAYS AS(Total_Available - Ticket_Sold), Price decimal(7,3));


'''

'''
+-----------------+--------------+------+-----+---------+-------------------+
| Field           | Type         | Null | Key | Default | Extra             |
+-----------------+--------------+------+-----+---------+-------------------+
| Movie_Name      | varchar(100) | YES  |     | NULL    |                   |
| Date            | date         | YES  |     | NULL    |                   |
| Ticket_Sold     | int          | YES  |     | NULL    |                   |
| Total_Available | int          | YES  |     | NULL    |                   |
| Ticket_Left     | int          | YES  |     | NULL    | VIRTUAL GENERATED |
| Price           | decimal(7,3) | YES  |     | NULL    |                   |
+-----------------+--------------+------+-----+---------+-------------------+

'''



from secrets import choice
import mysql.connector
mydb1 = mysql.connector.connect(
    host="localhost", user="root", passwd="Home@253144", database="cinema_hall")
mycursor = mydb1.cursor()




# mycursor.execute("CREATE TABLE "+table+"(NAME VARCHAR(100), SNO INTEGER)")

while True:
    user_choice = int(input("Server side or user side? 1 - > Server | 2 - > User"))
    if user_choice == 2:
        user()
    choice = int(input("Do you want to create a table for a cinema hall? 1 | 0"))


    
    if choice == 1:
        table_name  = input("Enter table name")
        mycursor.execute('create table '+table_name+'(Movie_Name VARCHAR(100), Date DATE, Ticket_Sold INTEGER, Total_Available INTEGER, Ticket_Left INTEGER GENERATED ALWAYS AS(Total_Available - Ticket_Sold), Price decimal(7,3))')
        
        mycursor.execute("show tables")
        for i in mycursor:
            print(i)
        break


    def user():
        seecinemas = int(input)