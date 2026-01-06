attendace=[18,20,19,15,21]
count=0
sum=0
for x in attendace:
    if x>=20:
        print("class is Full")
        count=count+1
    else:
        print("Not Full")
print("class was full in total",count,"days")
for x in attendace:
    sum=sum+x
print("Total attendance for all 5 days is:",sum)
