import os
import subprocess
import csv
import argparse
 
# to do: make sure the CSV has correct city names
# to do: input validation

city = 'NA'
state = 'NA'
exchanges = []

# set up command line arguments
parser = argparse.ArgumentParser(description='Enter your city and state abbreviation and this script will brute force Wi-Fi passwords based on valid phone numbers.')
parser.add_argument('-c', help='City name',required=True)
parser.add_argument('-s', help='State abbreviation',required=True)
args = parser.parse_args()

# read command line arguments, force uppercase
city = args.c
state = args.s
city = city.upper()
state = state.upper()

# clear previous wordlist
e = open("phoneList.txt","w")
e.write("")
e.close()

# magic occurs
# search_for = [city, state]

# pull out valid NPA/NXX exchange numbers for the requested city
with open('phones.csv') as inf:
  reader = csv.reader(inf)
  for row in reader:
    if row[2] in city and row[3] in state:
      exchanges.append(row[1]+row[0])
  print "List of valid NPA/NXX numbers for %s, %s:" % (city, state)
  print exchanges

# generate all 10,000 possibilities for each exchange
for i in exchanges:
  for y in range(0, 10):
    for z in range(0, 10):
      for l in range(0, 10):
        for m in range(0, 10):

# squish 'em together
          passwordParts=[i,y,z,l,m]
          password = ''.join(str(b)for b in passwordParts)

# write each password candidate to file
          f = open("phoneList.txt","a")
          f.write(password + '\n')
          f.close()

# great job
print "Done. See /phoneList.txt for your phone number wordlist."
