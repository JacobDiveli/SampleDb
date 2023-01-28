import psycopg2


conn = psycopg2.connect(
    database = "suppliers",
    user = "postgres",
    password="Jacob@123227",
    host="localhost",
    port="5432"
)


print(conn)

sql_query ='''
    CREATE TABLE Customer(
        Id INT  PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE INT NOT NULL,
        ADDRESS CHAR(100),
        LOAM_AMOUNT REAL
    )
'''

pointer=conn.cursor()

pointer.execute(sql_query)

conn.commit()

print("Table is created")






