#ejercico 1

import os
n = int(input('Introduce un número entero entre 1 al 10: '))
file_name="./tabla-{}.txt".format(n)

with open (file_name, mode="w") as f:
    for i in range(1,11):
        cadena="{} x {} = {}\n ".format(n,i, i * n)
        f.write(cadena)

#ejercicio2
import os
n = int(input('Introduce un número entero entre 1 al 10: '))
file_name="./tabla-{}.txt".format(n)
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)

with open (file_name, mode="w") as f:
    for i in range(1,11):
    
        cadena="{} x {} = {}\n ".format(n,i, i * n)
        f.write(cadena)
       

#3
n = int(input('Introduce un número entero entre 1 al 10: '))
m = int(input('Introduce otro número entero entre 1 al 10: '))
file_name="./tabla-{}.txt".format(n)
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del ', n)
else:
    lines = f.readlines()
    print(lines[m - 1])
with open (file_name, mode="w") as f:


     for i in range(1,11):
    
        cadena="{} x {} = {}\n ".format(n,i, i * n)
        f.write(cadena)
 

 #1

import re
texto =input()
print(re.search("@robot3!",texto))

#2
import re

str = 'User_mentions:9'
#search using regex
x = re.findall('[User_mentions:9]+', str)
print(x)


import re

str = 'likes: 5'
#search using regex
x = re.findall('[likes: 5]+', str)
print(x)



import re

str = 'number of retweets: 4'
#search using regex
x = re.findall('[number of retweets: 4]+', str)
print(x)

#3
import re
fh = open("analisis_sentimientos.txt")
for line in fh:
    if re.search(r"J.*Neu",line):
        print(line.rstrip())
fh.close()

#4

import email.utils
import re

def is_valid_email(text):
    pattern = r'^[a-z][a-z0-9\-_\.]+[@][a-z]+[.][a-z]{1,3}$'
    
    return re.search(pattern, text)

if __name__ == '__main__':
    contacts = [input() for _ in range(int(input()))]
    
    for c in contacts:
        result = email.utils.parseaddr(c)
        if is_valid_email(result[1]):
            result = email.utils.formataddr(result)
            print(result)



