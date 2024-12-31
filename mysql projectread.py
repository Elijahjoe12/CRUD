import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password='Mysql',
    database='JOB'
)
mycursor = mydb.cursor()
#select statement for job_seeker_profile which returns all columns 
job_read = """SELECT * FROM job_seeker_profile""" 
#executing query to fetch rows
mycursor.execute(job_read)
#fetching data in the database
job_data=mycursor.fetchall()
#printing all data in the database
for i in job_data:
    print(i)