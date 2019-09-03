import os 
import csv

#os.rename('/home/rashedka/Desktop/kkk', '/home/rashedka/Desktop/qwertyu') 

#print(os.path.isfile('/home/rashedka/Desktop/Delve_XML/4069652.tei.xml'))

checking = []
old_new_id = {}
k = 0
with open('/home/rashedka/Desktop/old_new_paper_id_new.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        #checking.append()
        if row[1] in checking:
        	#print(row[1])
        	k = k + 1
        	print(k)
        	continue
        checking.append(row[1])
        old_new_id.update([ (row[1], row[0])] )

print(k)

for key,value in old_new_id.items():
	if '$' in value:
		old_new_id[key] = value.replace('$','E')

print(len(old_new_id))



#805E75C6.tei.xml
#/home/rashedka/Desktop/Delve_XML
extention = '.tei.xml'
name_directory = '/home/rashedka/Desktop/Delve_XML/'
i = 0 
for key,value in old_new_id.items():
	try:
		#print(key) new id
		#print(value) old id
		
			
		link = name_directory + value + extention
		new_link = name_directory + key + extention
		#print(link)
		
		#print('-------')
		if os.path.isfile(new_link):
			continue

		#if '$' in value:
			#print(value)
			#new_value = value
			#new_value = new_value.replace('$','E')
			#link = name_directory + new_value + extention
			#new_link = name_directory + key + extention
			#print(link)
			#print(new_link)
			#os.rename(link,new_link)
			#i = i + 1
		i = i + 1
		#if value.isdigit():
			#print(value)
			#print('-----')

		
		#print(key + ' -- ' + value)
			#print('old link', link)
			#print('new link', new_link)
			#print(value)
		
		'''
		#print(value)
		
		new_value = value
		new_value = new_value.replace('$','E')
		new_link = name_directory + new_value + extention
		print(os.path.isfile(new_link))
		'''
		os.rename(link,new_link)
	except Exception as e:
		print(e)

print(i)