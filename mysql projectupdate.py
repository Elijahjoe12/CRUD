import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password='Mysql',
    database='JOB'
)
mycursor=mydb.cursor()
#update statement to modfify the cities of selected user ids
job_update=[('ojodu', 1), ('ojota', 2)]
sql="UPDATE job_seeker_profile SET city=%s WHERE user_account_id=%s"
#executing query to modify
mycursor.executemany(sql, job_update)
#committing the changes to the database
mydb.commit()
