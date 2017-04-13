import json
#from scipy.misc import imread
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS

def get_text(file='../items.json'):
	text=''
	words=[]
	with open(file,'r') as f:
		for line in f.readlines():
			data=json.loads(line)
			words+=data['subject']
	for word in words:
		if '非织造' not in word and '生产' not in word:
			text=text+' '+word
	return text

stopwords=set(STOPWORDS)
stopwords.add('性能研究')
text=get_text()
#alice_coloring=imread('bg.png')
alice_coloring=np.array(Image.open('alice.png'))
wc=WordCloud(font_path='xingkai.ttf',
	background_color='black',max_words=2000,mask=alice_coloring,
	max_font_size=60,random_state=42,stopwords=stopwords)

wc.generate(text)
image_colors=ImageColorGenerator(alice_coloring)

#plt.imshow(wc,interpolation='bilinear')
#plt.axis('off')
#plt.figure()

plt.imshow(wc.recolor(color_func=image_colors),interpolation='bilinear')
plt.axis('off')

#plt.figure()
#plt.imshow(alice_coloring,cmap=plt.cm.gray,interpolation='bilinear')
#plt.axis('off')
plt.show()
wc.to_file('wordcloud.png')



