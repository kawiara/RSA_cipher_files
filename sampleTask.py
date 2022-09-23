#step one: i want to know how to generate keys in RSA cipher. This task helped understand how to create keys



p=5   #p and q must be a prime number
q=11
n=p*q
phi=(p-1)*(q-1)
e=7   #e must be  1<e<phi
#public key= e=7, n=55

lewa_a=phi%e         #calculate d (private key)
lewa_b=lewa_a*e
lewa_c=phi-lewa_b


prawa_a=lewa_c*1
prawa_b=phi-prawa_a


nextStep_a=round(e/lewa_c)
nextStep_b=nextStep_a*lewa_c
nextStep_c=e-nextStep_b

next_a=nextStep_a*prawa_b
next_b=1-next_a
next_c=next_b%phi

ne_a=round(lewa_c/nextStep_c)
ne_b=ne_a*nextStep_c
ne_c=lewa_c-ne_b

n_a=ne_a*next_c
n_b=prawa_b-n_a #number d

print('e=',e)
print('n=',n)
print('d=',n_b)


