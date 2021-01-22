a=int(input())

print("*"*a)
for i in range(a-2):
    print("*{0}*".format(" "*(a-2)))
print("*"*a)

