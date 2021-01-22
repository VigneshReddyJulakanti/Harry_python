#break will exit the loop permanently if encountered
for i in range(10):
    if i==4:
        break
    print(i)


#continue will skip the loop itterration for the instance it is executed
for i in range(10):
    if i==4:
        continue
    print(i)