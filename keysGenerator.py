def generating(x, y):    #generating p and q
    prime = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime.append(n)
            
    return prime

import random

prime =  generating(1,31)
q = random.choice(prime)
p = random.choice(prime)

########

n=p*q
phi=(p-1)*(q-1)

def NWD(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a

e=7
while e<phi:
    a=NWD(e,phi)
    if a==1:
        break
    else:
        e+=1

def obD(phi, e):
    k=1
    while(((k*phi)+1)%e)!=0:
        k+=1
    d=((k*phi)+1)/e
    return d

d=obD(phi, e)

print('your public key e and n',e,n)
print('your private key',d)

#----------------------------------
#import random
#base = random.getrandbits(2048)
#p = next_prime(base + random.getrandbits(256))
#q = next_prime(base + random.getrandbits(256))
#n = p * q
#e = 65537
#print("e = ", e)
#print("n = ", n)
#c = power_mod(m, e, n)
#print("c = ", c)
#------------------------------------





        
    
