import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pymysql
#from collections import Counter

conn=pymysql.connect(host="localhost",user="scholar",password="starky",db="scholar",charset="utf8")
sql="select year,subject from xueshu"
data=pd.read_sql(sql,conn)

fangnian=['纺粘' in i for i in data.subject]
fangnian=data[fangnian]
rongpen=['熔喷' in i for i in data.subject]
rongpen=data[rongpen]

def generate(data):
	data1=data[data['year']<1996].count()[0]
	data2=data[data['year']<2001]
	data2=data2[data2['year']>1995].count()[0]
	data3=data[data['year']<2006]
	data3=data3[data3['year']>2000].count()[0]
	data4=data[data['year']<2011]
	data4=data4[data4['year']>2005].count()[0]
	data5=data[data['year']>2010].count()[0]
	return data1,data2,data3,data4,data5

rongpen=generate(rongpen)
fangnian=generate(fangnian)

N=5
ind=np.arange(N)
width=0.35
fig,ax=plt.subplots()
rong=ax.bar(ind,rongpen,width,color='#ffad00')
fang=ax.bar(ind+width,fangnian,width,color='#9b3c38')
ax.set_xticks(ind+width/2)
ax.set_xticklabels(('1991-1995','1996-2000','2001-2005','2006-2010','2011-2017'))
ax.legend((rong[0],fang[0]),('熔喷','纺粘'))
plt.rcParams['font.sans-serif']=['SimHei']
plt.title("关键词出现频率随年份的变化")
plt.xlabel("年份")
plt.ylabel("数量")
plt.show()
#print(rongpen)
#print(fangnian)



