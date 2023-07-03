import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='information_schema')

try:
    with connection.cursor() as cursor:
        # Get the list of all tables
        cursor.execute("SELECT TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME FROM KEY_COLUMN_USAGE WHERE REFERENCED_TABLE_SCHEMA = 'mob_development_mp_02' AND REFERENCED_TABLE_NAME IS NOT NULL;")
        relations = cursor.fetchall()

        for relation in relations:
            print(f"Table: {relation[0]}, Column: {relation[1]}, References: {relation[2]}.{relation[3]}")
finally:
    connection.close()
