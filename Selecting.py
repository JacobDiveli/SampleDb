import psycopg2


conn = psycopg2.connect(
    database = "suppliers",
    user = "postgres",
    password="Jacob@123227",
    host="localhost",
    port="5432"
)


print(conn)

select_query ='''
    select * from customer 

'''

pointer=conn.cursor()

pointer.execute(select_query)

rows=pointer.fetchall()

for each_row in rows:
    print(each_row[1],'-----Loanamount------',each_row[-1])






