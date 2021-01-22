a=int(input())
prime=True
for i in range(2,a):
    if a%i==0:
        prime=False
if(prime):
    print(f"{a} is a prime number")
else:
    print(f"{a} is not a prime number")
