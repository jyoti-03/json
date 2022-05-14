import json
f=open("meraki_q7.txt","r")
d={}
for l in f.readlines():
    s=""
    c=0
    for i in l:
        if i ==" ":
            d[s]=l[c+1:len(l)-1]
            break
        else:
            s+=i
            c+=1
j=json.dumps(d,indent=4)
print(j)
f.close()