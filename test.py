import csv
import math
with open("data.csv",newline='') as file:
    data_read=csv.reader(file)
    data_list=list(data_read)
data=data_list[0]

def mean(data):
    total=0
    l=len(data)
    for i in data:
        total+=int(i)
    mean=total/l
    return mean

squaredlist=[]
for n in data:
    a=int(n)-mean(data)
    a=a**2
    squaredlist.append(a)
    
sum=0

for i in squaredlist:
    sum+=i
result=sum/(len(data)-1)
standarddeviation=math.sqrt(result)
print(standarddeviation)
