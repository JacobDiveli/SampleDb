import psycopg2


conn = psycopg2.connect(
    database = "suppliers",
    user = "postgres",
    password="Jacob@123227",
    host="localhost",
    port="5432"
)


print(conn)

update_sql_query='''
    update customer set age =75 where id =2

'''

pointer=conn.cursor()

pointer.execute(update_sql_query)

conn.commit()

print("Record is updated")

conn.close()
