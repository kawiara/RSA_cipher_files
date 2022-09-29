# encrypt you message with public key OwO/keys in this exceries's static
import math
import operator

c=int(input('give me your decymal message, my master OwO:    '))

e=11
p=907
q=773
n=p*q
k=3
message_01=c%n
one=0

for i in range(1, e):
 one+=i
 message_01=message_01*message_01
 
print(message_01)
