Original_Dictionary= [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
aa = []
for i in Original_Dictionary:
        aa.append(i['Science'])
print(aa)


#======================================

x = [10,20,30,10]
xx = [10,20,35,15]
xxx = []

for d in range (len(x)):
        if x[d]<xx[d]:
                xxx.append(d+1)
print(xxx)







