import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","123456","whatsKonsole" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "select DISTINCT userId from users"
 
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      userId = row[0]
      print userId+":",
      sql2 = "select groupName from users where userId='"+userId+"'"
      cursor.execute(sql2)
      results2=cursor.fetchall()
      for col in results2:
         groupName = col[0]
         print groupName+",",
      print "",
except:
   print "Error: unable to fetch data"

# disconnect from server
db.close()
