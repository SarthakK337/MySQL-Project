import  mysql.connector as sql

def user_table():
    conn=sql.connect(host='localhost',user='root',passwd='1234',database='bank')
    cur = conn.cursor()
    cur.execute('create table user_table(username varchar(25) primary key,passwrd varchar(25) not null )')

