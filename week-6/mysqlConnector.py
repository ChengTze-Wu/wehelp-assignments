import mysql.connector
import configs

def account_query(username):
    queryData = {}
    
    cnx = mysql.connector.connect(**configs.DB_config.dbinfo())
    cursor = cnx.cursor()
    
    query = ("SELECT name, username, password FROM member " 
             "WHERE username = %s")

    data = (username,)
    cursor.execute(query, data)
    
    for q in cursor:
        queryData['name'] = q[0]
        queryData['username'] = q[1]
        queryData['password'] = q[2]
        
    cursor.close()
    cnx.close()
    return queryData


def account_create(name, username, passworrd):
    cnx = mysql.connector.connect(**configs.DB_config.dbinfo())
    cursor = cnx.cursor()
    
    add_member = ("INSERT INTO member (name, username, password) "
                  "VALUES (%s, %s, %s)")
    data_member = (name, username, passworrd)
    
    cursor.execute(add_member, data_member)
    cnx.commit()
    cursor.close()
    cnx.close()
    

