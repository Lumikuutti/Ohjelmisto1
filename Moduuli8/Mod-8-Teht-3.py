import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='dbuser',
         password='password',
         autocommit=True)

def select_airport (icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s;"
    #print(sql)
    cursor = connection.cursor()
    cursor.execute (sql, (icao,))
    result = cursor.fetchall()
    return result

icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-koodi: ")
location1 = select_airport(icao1)
location2 = select_airport(icao2)

print(f"Lentokenttien etäisyys toisistaan on {distance.distance(location1,location2).km:.2f} kilometriä.")