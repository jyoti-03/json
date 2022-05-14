import json
e=[["neelam","programer","24","2400"],["komal","trainer","24","20000"],["anuradha","HR","25","40000"],["Abhishek","manager","29","63000"]]
d=["name","designation","age","salary"]
bd={}
c2=0
for el in e:
    di={}
    c=0
    for i in el:
        di[d[c]]=i
        c+=1
    c2+=1
    bd["emp"+str(c2)]=di
j=json.dumps(bd,indent=4)
print(j)
