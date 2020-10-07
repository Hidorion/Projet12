import psycopg2

def db_connect (connection_infos, request):
    connection = psycopg2.connect(connection_infos)
    cursor = connection.cursor()
    sql_request = request
    cursor.execute(sql_request ,)
    connection.commit()
    result = cursor.fetchone()
    return result