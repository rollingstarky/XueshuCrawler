import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pymysql

#xueshu=pd.read_csv("xueshu.csv")
conn=pymysql.connect(host="localhost",user="scholar",password="starky",db="scholar",charset="utf8")
sql="select year,cite from xueshu"
xueshu=pd.read_sql(sql,conn)
xueshu=xueshu[xueshu.cite<80]

g=sns.FacetGrid(xueshu,palette="Set1",size=8)
g.map(plt.scatter,"year","cite",s=180,linewidth=0.65,edgecolor="white")
g.add_legend()
plt.show()