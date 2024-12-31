import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password='Mysql',
    database='JOB'
)
mycursor = mydb.cursor()
#creating a table in the database
sql="""CREATE TABLE job_seeker_profile (user_account_id int NOT NULL)""" 
#executing query to create table in database
mycursor.execute(sql)
