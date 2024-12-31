import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password='Mysql',
    database='JOB'
)
mycursor = mydb.cursor()
#inserting data into the table
sql = """INSERT INTO job_seeker_profile (user_account_id, city, country, employment_type, 
first_name, last_name, email, state, phone) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
job_seeker_profile = [
    (1, 'lagos', 'nigeria', 'data engineer', 'judge', 'bush', 'bush2@gmail.com', 'lagos', 22654738),
    (2, 'lagos', 'nigeria', 'developer', 'joe', 'luis', 'joe3@gmail.com', 'lagos', 67464737),
    (3, 'port harcourt', 'nigeria', 'graphics designer', 'simon', 'peter', 'peter12@gmail.com', 'rivers', 20786767),
    (4, 'abuja', 'nigeria', 'editor', 'andrew',  'philip', 'philip42@gmail.com', 'FCT', 21865678),
    (5, 'benin', 'nigeria', 'HR', 'david',  'james', 'james30@gmail.com', 'FCT', 21865678),
    (6, 'warri', 'nigeria', 'instructor', 'utomi',  'emmanuel', 'utomi90@gmail.com', 'FCT', 21865678),
    (7, 'jos', 'nigeria', 'animator', 'joy',  'joseph', 'joy21@gmail.com', 'FCT', 21865678),
    (8, 'ibadan', 'nigeria', 'accountant', 'grace',  'ojo', 'grace75@gmail.com', 'FCT', 21865678),
]
#executing query to insert data into the table
mycursor.executemany(sql,job_seeker_profile)
#committing to the database
mydb.commit()
