import psycopg2
import csv
import re
import pickle
import os


i = 0
paper_old_id = []
with open('/home/rashedka/Desktop/reading_file_name/Delve_XML.txt', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        paper_old_id.append(row)

        #print(row[1])
#print(paper_old_id)
#for p in paper_old_id:
	#print(p)

connection = psycopg2.connect(user = "postgres", 
								  password = "IAMWATCHINGYOU",
                                  host = "10.68.203.10",
                                  port = "5432",
                                  database = "delvedb")


paper_title = []
for p in paper_old_id:
	pp = p[0].replace("['","")
	pp = pp.replace("']","")
	pp = "'" + pp + "'"
	cursor = connection.cursor()
	create_table_query = ('''SELECT title
	 FROM public.table_main_data where paper_id =''' + pp + ''';''')
	cursor.execute(create_table_query)
	record = cursor.fetchone()
	#writefile.write(str(record) + '\n')
	paper_title.append(record)
	#print(record)

csr = connection.cursor()  
csr.close()

writefile = open('/home/rashedka/Desktop/reading_file_name/Delve_XML_title.txt','a')


connection1 = psycopg2.connect(user = "postgres", 
								  password = "Kaust.1234",
                                  host = "localhost",
                                  port = "5432",
                                  database = "delve")


print(len(paper_title))
j = 0
#pp = '12345'
#print((pp[1:])[:-1])
for p1 in paper_title:
	pp1 = p1[0].replace("('","")
	pp1 = pp1.replace("',)","")
	pp1 = "'" + pp1 + "'"
	try:
		if "'" in (pp1[1:])[:-1]:
			pp1 = pp1.replace("'","''")
			pp1 = (pp1[1:])[:-1]
			cursor1 = connection1.cursor()
			create_table_query = ('''SELECT id
		 	 FROM public.table_main_data where title =''' + pp1 + ''';''')
			cursor1.execute(create_table_query)
			record1 = cursor1.fetchone()
			writefile.write(str(record1) + '\n')
			continue

		if "''" in (pp1[1:])[:-1]:
			pp1 = pp1.replace("''","''''")
			pp1 = (pp1[1:])[:-1]
			cursor1 = connection1.cursor()
			create_table_query = ('''SELECT id
		 	 FROM public.table_main_data where title =''' + pp1 + ''';''')
			cursor1.execute(create_table_query)
			record1 = cursor1.fetchone()
			writefile.write(str(record1) + '\n')
			continue

		if "'''" in (pp1[1:])[:-1]:
			pp1 = pp1.replace("'''","''''''")
			pp1 = (pp1[1:])[:-1]
			cursor1 = connection1.cursor()
			create_table_query = ('''SELECT id
		 	 FROM public.table_main_data where title =''' + pp1 + ''';''')
			cursor1.execute(create_table_query)
			record1 = cursor1.fetchone()
			writefile.write(str(record1) + '\n')
			continue

		if "''''" in (pp1[1:])[:-1]:
			pp1 = pp1.replace("''''","''''''''")
			pp1 = (pp1[1:])[:-1]
			cursor1 = connection1.cursor()
			create_table_query = ('''SELECT id
		 	 FROM public.table_main_data where title =''' + pp1 + ''';''')
			cursor1.execute(create_table_query)
			record1 = cursor1.fetchone()
			writefile.write(str(record1) + '\n')
			continue
		#if "regulation" in pp1:
			#print(pp1)
		cursor1 = connection1.cursor()
		create_table_query = ('''SELECT id
		 FROM public.table_main_data where title =''' + pp1 + ''';''')
		cursor1.execute(create_table_query)
		record1 = cursor1.fetchone()
		writefile.write(str(record1) + '\n')
	except:
		print(pp1)

		

	#paper_title.append(record)
	#print(record1)