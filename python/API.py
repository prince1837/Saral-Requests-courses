import requests
import json
import os.path
from os import path
if path.exists("prince.json"):
	with open ("prince.json", "r") as pk:
		data=json.load(pk)
		# print (data)
else:
	url="http://saral.navgurukul.org/api/courses"
	p= requests.get(url).text

	with open ("prince.json", "w+") as pk:
		pk.write(p)
		data=json.loads(p)
		# print(data)
count=0
courses=[]
for i in data['availableCourses']:
	count+=1
	a=count,i['name']
	courses.append(i['id'])
	print (a)
user=int(input())
new_url="http://saral.navgurukul.org/api/courses/"+str(courses[user-1])+"/exercises"
q=requests.get(new_url).text
q1=json.loads(q)
# print (q1)
cou=1
slug=[]
ID=[]
for i in q1['data']:
	slug.append(i['slug'])
	print (cou,i['name'])
	cou+=1
# print (slug)
user1=int(input())
new_url1="http://saral.navgurukul.org/api/courses/"+str(courses[user-1])+"/exercise/getBySlug?slug="+str(slug[user1-1])
# print (new_url1)
s1=requests.get(new_url1).text
s2=json.loads(s1)
print (s2['content'])