import  mysql.connector as sql

def transac_table():
    conn=sql.connect(host='localhost',user='root',passwd='1234',database='bank')
    cur = conn.cursor()
    cur.execute('create table transactions(acct_no int(11),date date ,withdrawal_amt bigint(20),amount_added bigint(20) )')
