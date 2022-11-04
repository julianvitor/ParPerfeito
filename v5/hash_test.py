from hashlib import sha256
import csv
import os 



files = os.listdir(os.curdir)
print (files)


file="v5/dados.csv"
nova_lista = []


with open(file, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    for i in range(len(numbers)):
        data[i] = 


input_ = input('Enter something: ')
print(sha256(input_.encode('utf-8')).hexdigest())