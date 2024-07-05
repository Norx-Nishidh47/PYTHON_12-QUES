import mysql.connector as sql
con=sql.connect(host="localhost",username="root",password="nishidh@123",database="SCHOOL")
cur=con.cursor()

def init(enteries):
    for i in range(enteries):
        global query
        query=f"insert into Student (rno,name,DOB,fee) values ({int(input('Enter Roll NO :'))},'{str(input('Enter the name of the student : '))}','{str(input("Enter the date of Admission in (YYYY-MM-DD) : "))}',{float(input("Enter the fee of the student : "))});"
        cur.execute(query)
        con.commit()
init()
if cur.rowcount!=None:
    print("Successfully executed")
else:
    print("try again")
    init()    
print(query)