import requests
import os
import random


print ('12345')
print(os.listdir('/clients'))
with open('/clients/secretClientFile.txt', 'r') as infile:
  print ('reading secrets ...')
  for l in infile:
    print ('\t' + l)

print ('writing secrets...')
with open ('/clients/secretFile' + str(random.randint(0,100000)) + '.txt', 'w') as outfile:
    outfile.write('output secret: ' + str(random.randint(0,123123123123123)))

print (" end ---")
