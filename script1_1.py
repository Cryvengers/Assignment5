f1=open("out1.txt","r+")
i=0
while True:
    k=f1.readline()
    k=k.lstrip()
    k=k.rstrip()
    if(len(k)==16 and k[0]!='>'):
        print(k)
        i=i+1
    if(i==128):
        break
f1.close()