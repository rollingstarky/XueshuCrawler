from pymongo import MongoClient
from bson.son import SON
import seaborn as sns
import matplotlib.pyplot as plt

client=MongoClient()
db=client.baidu
collection=db.xueshu

pipeline=[
{"$unwind":"$subject"},
{"$group":{"_id":"$subject","count":{"$sum":1}}},
{"$sort":SON([("count",-1),("id",-1)])}
]

subject=list(collection.aggregate(pipeline))
#print(subject)

keys=[]
values=[]
stopwords=['非织造','双组分纤维','生产']
for item in subject:
	if '非织造' not in item['_id'] and '双组分纤维' not in item['_id'] and '生产' not in item['_id'] and item['count'] > 8:
		keys.append(item['_id'])
		values.append(item['count'])
print(keys)
print(values)

sns.set_style("darkgrid")
sns.barplot(x=keys,y=values,palette="muted")
plt.rcParams['font.sans-serif']=['SimHei']
plt.title("非织造论文关键词分布")
plt.xlabel("关键词")
plt.ylabel("数量")
axis=plt.gca().xaxis
for label in axis.get_ticklabels():
    label.set_rotation(90)
plt.show()