import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='stu',
         password='qP72x[!-2}ELoh',
         autocommit=True)

def search_airports (country_code):
    sql = "SELECT type, count(*) as 'amount' FROM airport WHERE iso_country = %s GROUP BY type;"
    #print(sql)
    cursor = connection.cursor(dictionary=True)
    cursor.execute (sql, (country_code,))
    result = cursor.fetchall()
    return result

input_code = input("Anna maakoodi niin kerron sinulle kuinka monta minkäkin tyyppistä lentokenttää maasta löytyy: ")
print(search_airports(input_code))