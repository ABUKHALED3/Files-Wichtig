def isprime(num):
    for n in range(2,int(num**0.5)+1):
        return 'is Prime' if num%n ==0 else 'is not Prime'
    
print(isprime(14))
print(isprime(15))
print(isprime(7))