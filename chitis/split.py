
a=["vig!ce!100000000009","nesh!lo!100000000007","julakanti!boom!100000000006"]


sal=[]
for i in a:
    sal.append(int((i.split("!")[2])))
sal.sort()
hsal=(int(sal[-1]))
print(hsal)

for i in a:
    if int(i.split("!")[2])==hsal:
       hname=(i.split("!")[0])
       print(hname)


# res=0
# resn=""
# for i in a:
#     res+=int((i.split("!"))[2])
#     resn+=(i.split("!"))[0]
# print(res)
# print("names",resn)