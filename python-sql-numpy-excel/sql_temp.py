#Script 2 Query the database
import sqlite3
con = sqlite3.connect("database.db")
c = con.cursor()
#List distinct major cities in southern hemisphere and order by country
create_table = """CREATE TABLE southern_Cities(
              city VARCHAR(50),
              country VARCHAR(50),
              latitude VARCHAR(10),
              longitude VARCHAR(10));"""
#get cities in southern hemisphere
sql_command = """SELECT DISTINCT city, country, latitude, longitude
                 FROM temp_by_city
                 WHERE latitude LIKE '%S'
                 ORDER BY country;"""
insert = "INSERT INTO southern_Cities(city, country, latitude, longitude) VALUES(?, ?, ?, ?);"
#create table
c.execute("DROP TABLE IF EXISTS southern_Cities;")
c.execute(create_table)
#populate table
c.execute(sql_command)
fetch = c.fetchall()
for row in fetch:
    c.execute(insert, row)
c.execute("""SELECT MAX(aver_temp), MIN(aver_temp), AVG(aver_temp) FROM temp_by_state WHERE state = "Queensland" AND date LIKE "2000%";""")
fetch = c.fetchall()
print(fetch)
#save
con.commit()
con.close()