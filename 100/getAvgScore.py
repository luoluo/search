import sqlite3
conr = sqlite3.connect("bdre100rep")
cr = conr.cursor()
ff = cr.execute("select * from docr")
sum1 = 0
sum2 = 0
sum3 = 0
rows = ff.fetchall()
for row in rows:
	if row[0] %	10 == 0:
		sum1 += row[5]
	elif row[0] % 10 == 2:
		sum2 += row[5]
	elif row[0] % 10 == 4:
		sum3 += row[5]
sum1 /= 10.0
sum2 /= 10.0
sum3 /= 10.0
print sum1
print sum2
print sum3
