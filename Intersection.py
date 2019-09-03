import csv
import re
import pickle
import os



#writefile = open('/home/rashedka/Desktop/Untitled Folder/SecondPart.txt','a')


DataLinks = []
with open('/home/rashedka/Desktop/all_matching_data.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        #rint(row[0],row[1])
        links = row[1]
        links = links.lower()
        links = (re.sub('[^A-Za-z0-9]+', '', links))
        links = (links.replace("https", ""))
        links = (links.replace("http", ""))
        links = (links.replace("ftp", ""))
        links = (links.replace("ftps", ""))
        links = (links.replace("www", ""))
        DataLinks.append(links)
        #if links in intersectionList:
        	#writefile.write(str(row) + '\n')
#print(len(DataLinks))
#print(DataLinks)

FirstPart_onlylinks = []
with open('/home/rashedka/Desktop/FinalExtracting/onlylinks/FirstPart_onlylinks/extractingFootNoteSentence.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        #rint(row[0],row[1])
        links = row[1]
        links = links.lower()
        links = (re.sub('[^A-Za-z0-9]+', '', links))
        links = (links.replace("https", ""))
        links = (links.replace("http", ""))
        links = (links.replace("ftp", ""))
        links = (links.replace("ftps", ""))
        links = (links.replace("www", ""))
        FirstPart_onlylinks.append(links)
        if links in DataLinks:
        	print(row)
#print(len(FirstPart_onlylinks))


Delve_XML_onlylinks = []
with open('/home/rashedka/Desktop/FinalExtracting/onlylinks/Delve_XML_onlylinks/extractingFootNoteSentence.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        #rint(row[0],row[1])
        links = row[1]
       	links = links.lower()
        links = (re.sub('[^A-Za-z0-9]+', '', links))
        links = (links.replace("https", ""))
        links = (links.replace("http", ""))
        links = (links.replace("ftp", ""))
        links = (links.replace("ftps", ""))
        links = (links.replace("www", ""))
        Delve_XML_onlylinks.append(links)
        if links in DataLinks:
        	print(row)
#print(len(Delve_XML_onlylinks))


#intersectionList = pickle.load( open( "intersection_SecondPart_onlylinks.p", "rb" ) )
#intersectionList.remove('')
#intersectionList.remove('1')
#intersectionList.remove('m')
#print(intersectionList)




SecondPart_onlylinks = []
with open('/home/rashedka/Desktop/FinalExtracting/onlylinks/SecondPart_onlylinks/extractingFootNoteSentence.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        #rint(row[0],row[1])
        links = row[1]
        links = links.lower()
        links = (re.sub('[^A-Za-z0-9]+', '', links))
        links = (links.replace("https", ""))
        links = (links.replace("http", ""))
        links = (links.replace("ftp", ""))
        links = (links.replace("ftps", ""))
        links = (links.replace("www", ""))
        SecondPart_onlylinks.append(links)
        if links in DataLinks:
        	print(row)
#print(len(SecondPart_onlylinks))





#print(len(list(set(DataLinks2) - set(DataLinks))))
#print(len(intersection(Delve_XML_onlylinks, DataLinks)))

#print(len(list(set(Delve_XML_onlylinks) & set(DataLinks))))
#print(len(list(set(FirstPart_onlylinks) & set(DataLinks))))
#print(len(list(set(SecondPart_onlylinks) & set(DataLinks))))
#print((list(set(SecondPart_onlylinks) & set(DataLinks))))
#pickle.dump((list(set(SecondPart_onlylinks) & set(DataLinks))), open( "intersection_SecondPart_onlylinks.p", "wb" ) )