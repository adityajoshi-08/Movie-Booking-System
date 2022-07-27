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
| Movie_id        | int          | YES  |     | NULL    |                   |
+-----------------+--------------+------+-----+---------+-------------------+

'''



from secrets import choice
from setuptools import Command
from tabulate import tabulate
import mysql.connector
mydb1 = mysql.connector.connect(
    host="localhost", user="root", passwd="Home@253144", database="cinema_hall")
mycursor = mydb1.cursor()




# mycursor.execute("CREATE TABLE "+table+"(NAME VARCHAR(100), SNO INTEGER)")

def showtable(table_name, header):
    mycursor.execute("select * from "+table_name)
    command = mycursor.fetchall()
    table = (tabulate(command, headers=header, tablefmt="pretty"))
    print(table)

def main():
    
    user_choice = int(input("Server side or user side? 1 - > Server | 2 - > User"))

    if user_choice == 2:
        while True:
            mycursor.execute("show tables")
            cmd = mycursor.fetchall()

            headers = ["Available Cinemas"]

            table = (tabulate(cmd, headers=headers, tablefmt="pretty"))
            print(table)

            cinema_name  = input("Please enter the cinema name \n")
            cinema_header = ["Movie Name","Date","Tickets Sold","Total Available", "Tickets Available","Price","Movie ID"]
            showtable(cinema_name, cinema_header)
            movie_choice  = input("Which movie do you want to see? \n")

            mycursor.execute("UPDATE "+cinema_name+" SET Ticket_Sold = (Ticket_Sold + 1) where Movie_id = %s",(movie_choice,))
            print("Movie booked!")
            showtable(cinema_name, cinema_header)
            book_again = int(input("Do you want to book again? 1 | 0"))
            if (book_again == 0):
                break




    elif user_choice == 1:
    
        choice = int(input("Do you want to create a table for a cinema hall? 1 | 0"))

        if choice == 1:
            table_name_variable  = input("Enter table name")
            mycursor.execute('create table '+table_name_variable+'(Movie_Name VARCHAR(100), Date DATE, Ticket_Sold INTEGER, Total_Available INTEGER, Ticket_Left INTEGER GENERATED ALWAYS AS(Total_Available - Ticket_Sold), Price decimal(7,3), Movie_id INT)')
        
        
        mycursor.execute("show tables")
        cmd = mycursor.fetchall()

        headers = ["Available Cinemas"]

        table = (tabulate(cmd, headers=headers, tablefmt="pretty"))
        print(table)
        table_name = input("Which table you want to work with?")

        print("1. Insert new movie details \n"
              "2. Update a movie details")
        operation = int(input("What do you want to do?"))
        
        if operation == 1:
            print("Enter the details of the movie")
            movie_name = input("Enter the movie name : ")
            movie_date = input("Enter the movie date YYYY-MM-DD : ")
            ticket_total = int(input("Enter the total tickets : "))
            ticket_sold = int(input("Enter the tickets sold : "))
            price = float(input("Enter the price of the ticket"))
            movie_id = int(input("Enter the movie id"))
            mycursor.execute("INSERT INTO "+table_name+" (Movie_Name,Date,Ticket_Sold,Total_Available,Price,Movie_id) VALUES(%s,%s,%s,%s,%s,%s)",(movie_name,movie_date,ticket_sold,ticket_total,price,movie_id))
            print("Added movie to the table!")
            mydb1.commit()
        
        if operation == 2:
            cinema_header = ["Movie Name","Date","Tickets Sold","Total Available", "Tickets Available","Price","Movie ID"]
            showtable(table_name, cinema_header)
            movie_id = int(input("Enter the movie id"))
            print("1. Movie Name \n 2. Date \n 3. Tickets Sold \n 4. Total Tickets \n 5. Price of ticket")
            update_choice = int(input("What do you want to update: "))
            if update_choice == 1:
                movie_name = input("Enter the movie name: ")
                mycursor.execute("UPDATE "+table_name+" SET Movie_Name = %s where Movie_id = %s",(movie_name,movie_id))
                mydb1.commit()
            
            elif update_choice == 2:
                movie_date = input("Enter the movie date: ")
                mycursor.execute("UPDATE "+table_name+" SET Date = %s where Movie_id = %s",(movie_date,movie_id))
                mydb1.commit()
            
            elif update_choice == 3:
                ticket_sold = int(input("Enter number of tickets sold: "))
                mycursor.execute("UPDATE "+table_name+" SET Ticket_Sold = %s where Movie_id = %s",(ticket_sold,movie_id))
                mydb1.commit()

            elif update_choice == 4:
                ticket_available = int(input("Enter number of tickets available: "))
                mycursor.execute("UPDATE "+table_name+" SET Ticket_Available = %s where Movie_id = %s",(ticket_available,movie_id))
                mydb1.commit()

            elif update_choice == 5:
                price = int(input("Enter price of ticket: "))
                mycursor.execute("UPDATE "+table_name+" SET Price = %s where Movie_id = %s",(price,movie_id))
                mydb1.commit()








main()
