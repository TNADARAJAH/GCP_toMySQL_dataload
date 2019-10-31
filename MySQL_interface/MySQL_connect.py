import mysql.connector


def create_MySQLconnection():
    global MySQLdb

    MySQLdb = mysql.connector.connect(host='localhost', port=3306, user='thineth', passwd='thineth')

    MyCursor = MySQLdb.cursor()

    MyCursor.execute('USE mysql')

    try:
        MyCursor.execute('drop table Hackernews')
    except:
        print('Table does not exist')

    MyCursor.execute('create table Hackernews(username varchar(20), title varchar(100))')

    return(MyCursor)


def insert_results(results, cursor):
    insert_stat = 'Insert into Hackernews(username, title) values (%s,%s)'
    cursor.execute(insert_stat, ('three','four'))
    MySQLdb.commit()

    for row in results:
        val = (row['by'], row['title'])
        print(val)
        cursor.execute(insert_stat, val)
        MySQLdb.commit()
