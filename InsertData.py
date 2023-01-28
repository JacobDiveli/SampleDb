import psycopg2


conn = psycopg2.connect(
    database = "suppliers",
    user = "postgres",
    password="Jacob@123227",
    host="localhost",
    port="5432"
)


print(conn)

insert_sql_query='''
    insert into Customer(Id,name,age,address,loam_amount) 
    values(4,'swamy',60,'Rj',4500.14)

'''

pointer=conn.cursor()

pointer.execute(insert_sql_query)

conn.commit()

print("Record is created")

conn.close()
