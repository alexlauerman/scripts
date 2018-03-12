import os

inputfile = "\\path\\dbip-city-2017-11.csv\\dbip-city-2017-11.csv"
outputfile = "\\path\\dbip-city-2017-11.csv\\seckcrange.csv"

def ipRange(start_ip, end_ip):
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    temp = start
    ip_range = []

    ip_range.append(start_ip)
    while temp != end:
        start[3] += 1
        for i in (3, 2, 1):
            if temp[i] == 256:
                temp[i] = 0
                temp[i - 1] += 1
        ip_range.append(".".join(map(str, temp)))

    return ip_range


try:
    os.remove(outputfile)
except OSError:
    pass

f = open(outputfile, "w")

import csv
with open(inputfile) as csvfile:
    reader = csv.DictReader(csvfile, fieldnames = ( "startip","endip","country","state","city" ))
    for row in reader:
        #debug mode
		#print(row['startip'], row['endip'])
        if row['country'] == "US":
            if row['state'] == "Kansas" or row['state'] == "Missouri":
                if row['city'] != "St. Louis" and row['city'] != "Lyons" and row['city'] != "Wichita":
                    #so this means... if row['city'] != "Kansas City" and row['city'] != "Overland Park":
                    if str(row['startip']).find(":") == -1 :
                        ip_range = ipRange(row['startip'], row['endip'])
                        for ip in ip_range:
                            f.write(ip + "\n")
                            #debug mode
                            #print(ip)
                            #print (ip + " " + row['state'] + " " + row['city'])
                            #f.write(ip + " " + row['state'] + " " + row['city'] + "\n")