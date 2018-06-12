import MySQLdb

## Varibales globales
hostName='localhost'
userName='root'
password=''

print("MIGRACION SQL")
nombreBd1 = input("Base de datos principal (La que enviara datos):")
nombreBd2 = input("Base de datos secundaria (La que recibira datos):")

conn1 = MySQLdb.connect (host =hostName,
                        user = userName,
                        passwd = password)
cursor1 = conn1.cursor ()

cursor1.execute ("show tables in "+nombreBd1)
cursor2 = conn1.cursor ()

for row in cursor1.fetchall():
    consulta="INSERT INTO "+nombreBd2+"."+row[0]+" SELECT *  FROM "+nombreBd1+"."+row[0]
    print (consulta)
    cursor2.execute (consulta)
    conn1.commit()    

print("Termine!")
cursor1.close ()
cursor2.close()
conn1.close ()
