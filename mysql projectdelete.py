import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password='Mysql',
    database='JOB'
)
mycursor=mydb.cursor()
#delete statement to remove record of selected user id
sql="DELETE FROM job_seeker_profile WHERE user_account_id=1"
#executing query to remove selected record
mycursor.execute(sql)
#committing changes to the database
mydb.commit()