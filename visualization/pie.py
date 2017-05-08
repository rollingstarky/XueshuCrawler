import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
#import seaborn as sns
import pymysql

keys=[]
values=[]
conn=pymysql.connect(host="localhost",user="scholar",password="starky",db="scholar",charset="utf8")
sql="select subject from xueshu"
data=pd.read_sql(sql,conn)
subjects=[]

for i in data['subject']:
	for a in i.split():
		if '非织造' not in a and '生产' not in a and '性能' not in a:
			subjects.append(a)

for i in Counter(subjects).most_common(8):
	keys.append(i[0])
	values.append(i[1])		
#print(subjects)
#print(keys)
#print(values)
colors=['yellowgreen','gold','lightskyblue','lightcoral','red','purple','orange','green']
explode=(0,0,0,0,0.1,0,0,0)
plt.pie(values,explode=explode,labels=keys,autopct='%1.1f%%',colors=colors)
plt.axis('equal')
plt.rcParams['font.sans-serif']=['SimHei']
plt.show()


