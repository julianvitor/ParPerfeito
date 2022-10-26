from hashlib import sha256
import csv
  






# csv fileused id Geeks.csv
filename=""
 
# opening the file using "with"
# statement
with open(filename,'r') as data:
   for line in csv.reader(data):
            print(line)
         
# then data is read line by line
# using csv.reader the printed
# result will be in a list format
# which is easy to interpre
input_ = input('Enter something: ')
print(sha256(input_.encode('utf-8')).hexdigest())