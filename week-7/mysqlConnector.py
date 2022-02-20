import mysql.connector
from config import DB

cnx = mysql.connector.connect(pool_name = "pool",
                              pool_size = 10,
                              **DB.dbinfo())

def account_query(username):
    queryData = {}
    cnx = mysql.connector.connect(pool_name = "pool")
    cursor = cnx.cursor()
    query = ("SELECT id, name, username, password FROM member " 
            "WHERE username = %s")
    data = (username,)
    cursor.execute(query, data)
    
    for q in cursor:
        queryData['id'] = q[0]
        queryData['name'] = q[1]
        queryData['username'] = q[2]
        queryData['password'] = q[3]

    cursor.close()
    cnx.close()
    return queryData


def account_create(name, username, passworrd):
    cursor = cnx.cursor()
    cnx = mysql.connector.connect(pool_name = "pool")
    add_member = ("INSERT INTO member (name, username, password) "
                  "VALUES (%s, %s, %s)")
    data = (name, username, passworrd)
    
    cursor.execute(add_member, data)
    cnx.commit()
    cursor.close()
    cnx.close()
    

def account_name_update(name, username):
    cursor = cnx.cursor()
    cnx = mysql.connector.connect(pool_name = "pool")
    update_member_name = ("UPDATE member "
                        "SET name = %s "
                        "WHERE username = %s")
    data = (name, username)
    
    cursor.execute(update_member_name, data)
    cnx.commit()
    cursor.close()
    cnx.close()