text1= "gsjgktipfolqgfmq"
text2= "ifffiljjgujfklhn"
pvals=[]
for i in range(0,8):
    for j in range(0,16):
        pvals.append(chr(i+ord("f"))+chr(j+ord("f")))
f1=open("out_filter1.txt","r+")
f2=open("out_filter2.txt","r+")
fptr1=open("ipassword1.txt","r+")
fptr2=open("ipassword2.txt","r+")
k=int(input("Give number of known bytes:"))#represents number of bytes decrypted
if(k!=0):
    p1=fptr1.readline()
    p2=fptr2.readline()
else:
    p1=""
    p2=""
fptr1.close()
fptr2.close()
fptr1=open("ipassword1.txt","w+")
fptr2=open("ipassword2.txt","w+")
i=0
while True:
    q=f1.readline()
    if(q[0:(2*k+2)]==text1[0:(2*k+2)]):
        break
    i=i+1
w1=p1+pvals[i]
fptr1.write(w1)
i=0
while True:
    q=f2.readline()
    if(q[0:(2*k+2)]==text2[0:(2*k+2)]):
        break
    i=i+1
w2=p2+pvals[i]
fptr2.write(w2)