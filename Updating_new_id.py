import csv
import re
import pickle
import os

old_new_id = {}
checking = []
with open('/home/rashedka/Desktop/old_new_id_with_title.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        old_new_id.update([ (row[1], row[0])] )
 



#for key,value in old_new_id.items():
#	print(key + ' $ '  + value)
#key old id

key_paper = '' + '820F0CBA' + "'" 
print(old_new_id.get(key_paper))


writefile = open('/home/rashedka/Desktop/fianl_data_ref.txt','a')
i = 0
with open('/home/rashedka/Desktop/Data_ref.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
    	if old_new_id.get(row[5]) == None:
    		writefile.write(row[0] + '$' + row[1] + '$' + row[2] + '$' + row[3] + '$' +  row[4] + '$' + row[5] + '\n')
    		
    	else:
    		writefile.write(row[0] + '$' + row[1] + '$' + row[2] + '$' + row[3] + '$' +  row[4] + '$' + old_new_id.get(row[5]) + '$' + row[5] + '\n' )
    		

    	'''
    	for key,value in old_new_id.items():
    		if row[5] == key:
    			writefile.write(row[0] + '$' + row[1] + '$' + row[2] + '$' + row[3] + '$' + row[4] + '$' + value + '\n')
    			#print(key)
    			#break
    		else:
    			writefile.write(row[0] + '$' + row[1] + '$' + row[2] + '$' + row[3] + '$' + row[4] + '$' + row[5] + '\n')
    			#print(key)
    			#break
		'''
print(i)