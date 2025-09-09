import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='dbuser',
         password='password',
         autocommit=True)

def search_airports (icao):
    sql = "SELECT * FROM airport WHERE ident=%s"
    #print(sql)
    cursor = connection.cursor(dictionary=True)
    cursor.execute (sql, (icao,))
    result = cursor.fetchone()
    return result

icao = input("Anna lentokentän ICAO koodi: ")
table = search_airports(icao)
print(table['name'], table['municipality'])