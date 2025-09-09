import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='stu',
         password='qP72x[!-2}ELoh',
         autocommit=True)

def search_airports (country_code):
    sql = "SELECT type as 'Type', count(*) as 'Amount' FROM airport WHERE iso_country = %s GROUP BY type;"
    #print(sql)
    cursor = connection.cursor(dictionary=True)
    cursor.execute (sql, (country_code,))
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row}")
    return

input_code = input("Give me the country code and I'll tell you how many of each type of airport it has: ")
search_airports(input_code)