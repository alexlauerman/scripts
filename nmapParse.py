#!/usr/bin/env python

#install requirements: pip install python-libnmap

#usage is something like ./python nmapParse.py scan.xml

from libnmap.parser import NmapParser
import sys

def printsortedlist(list):

        output = ""
        list = sorted(set(list))
        #list = list.sort(key=int)
        #list = sorted(list, key=lambda x: x[-1])
        for l in list:
                output += str(l) + ","
        print "Count: " + str(len(list))
        print output[:-1]


def printsortedlistall(list):
        output = ""
        list = sorted(list)
        for l in list:
                output += str(l) + ","
        print "Count: " + str(len(list))
        print output[:-1]

def printsortedlistnewlines(list):
	output = ""
        list = sorted(set(list))
        for l in list:
                output += str(l) + "\n"
        print "Count: " + str(len(list))
        print output[:-1]


def printsortedlistnewlineswithcount(list):
        output = ""
        countlist = []
        for l in list:
                countlist.append(str(l) + "," +  str(list.count(l)))
                #countlist = sorted(set(countlist))
        #for ltwo in countlist:
               #output += str(ltwo) +  str(countlist.count(ltwo)) + "\n"
        printsortedlistnewlines(countlist)

        #output = sorted(set(countlist))
        #print "Count: " + str(len(countlist))
        #print output[:-1]

def printsortedlistnewlineswithcountall(list):
        output = ""
        #list = sorted(set(list)) makes them unique
        list = sorted(list)
        for l in list:
                output += str(l) + "," +  str(list.count(l)) + "\n"
        print "Count: " + str(len(list))
        print output[:-1]


nmap_report = NmapParser.parse_fromfile(sys.argv[1])
#print "Nmap scan summary: {0}".format(nmap_report.summary)

openports = []
opentcp = []
openudp = []
openhosts = []

#trying to get
#PORT	PROTOCOL	SERVICE	VERSION
#443	tcp	ssl/http
openportprotoserviceversion = []
servicePort = []
servicePortNoBanner = []
servicePortCount = []

for h in nmap_report.hosts:
        for s in h.services:
                if s.state != "open|filtered":
                        openports.append(s.port)
                        openhosts.append(h.ipv4)
                        if s.protocol == "tcp":
                                opentcp.append(s.port)
                        else:
                                openudp.append(s.port)

                        openportprotoserviceversion.append(str(h.ipv4) + "," + str(s.port) + "," + str(s.protocol) + "," + str(s.state) + "," + str(s.service) + "," + str(s.banner) + "," +  str(s.servicefp))
                        servicePort.append(str(s.port) + " - " + str(s.protocol).upper() + " - " + str(s.service) + "," +  str(s.banner))
                        servicePortNoBanner.append(str(s.port) + " - " + str(s.protocol).upper() + " - " + str(s.service))
                        #for uniqueService in servicePort:
                        #        rcommmaindex = uniqueService.rfind(",")
                        #        if (uniqueService[:rcommmaindex] ==  str(s.port) + " - " + str(s.protocol).upper() + " - " + str(s.service) + "," +  str(s.banner)):
                        #                servicePortCount.append(uniqueService[:rcommmaindex] + " " + str(int(uniqueService[rcommmaindex+2:])+1))

print "--All Open Ports--"
printsortedlist(openports)


print "--TCP--" #+ str(len(opentcp))
printsortedlist(opentcp)


print "--UDP--" #+ str(len(openudp))
printsortedlist(openudp)

print "--Hosts with open ports-- " #+ str(len(openhosts))
printsortedlist(openhosts)

print "--Hosts with open ports newlines-- " #+ str(len(openhosts))
printsortedlistnewlines(openhosts)

print "--Hosts CSV--"
printsortedlistnewlines(openportprotoserviceversion)

#print "--Service,PortCount-- "
#printsortedlistnewlines(servicePortCount)

print "--Services,PortCount-Unique-Count--"
print "Services,Count"
printsortedlistnewlineswithcount(servicePort)

print "--Services,PortCount-Unique-Count--"
print "Services,Count"
printsortedlistnewlineswithcount(servicePortNoBanner)

print "--Services,PortCount-Unique-Count--"
print "Services,Count"
printsortedlistnewlines(servicePort)

#print "--Services,PortCount-Count--"
#print "Services,Count"
#printsortedlistnewlinesallcount(servicePort)
