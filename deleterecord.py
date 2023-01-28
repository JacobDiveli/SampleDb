import psycopg2


conn = psycopg2.connect(
    database = "suppliers",
    user = "postgres",
    password="Jacob@123227",
    host="localhost",
    port="5432"
)


print(conn)
delete_sql_query='''
    delete from customer where id =3

'''

pointer=conn.cursor()

pointer.execute(delete_sql_query)

conn.commit()

print("Record is deleted")

conn.close()
