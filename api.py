
# import requests
# url="http://saral.navgurukul.org/api/courses"
# r=requests.get(url)
# print (r.text)



# import requests
# def url():
# 	url="http://saral.navgurukul.org/api/courses"
# 	r=requests.get(url)
# 	p =(r.text)
# 	return p
# print (url())



# import requests
# url="http://saral.navgurukul.org/api/courses"
# r=requests.get(url)
# w= (r.text)
# my_file =open("saral_data.txt",'w')
# my_file.write(w)
# my_file.close()







# import requests,json
# url="http://saral.navgurukul.org/api/courses"
# r=requests.get(url)
# s= (r.text)
# with open('prince.json','w') as saral_data:
# 	data = json.dumps(s)
# 	raw = saral_data.write(data)
# 	saral_data.close()





# import json
# with open('prince.json','r') as saral_data:
# 	data=saral_data.read()
# 	p= json.loads(data)
# 	p1= json.loads(p)
# 	saral_data.close()
# 	print (p1)






# import requests
# import json
# url="http://saral.navgurukul.org/api/courses"
# r=requests.get(url)
# raw=r.json()
# for j in raw['availableCourses']:
# 	print (j)






# import requests
# import json
# url="http://saral.navgurukul.org/api/courses"
# r=requests.get(url)
# raw=r.json()
# for j in raw['availableCourses']:
# 		print (j['id'])
# 		print (j['name'])







# import requests
# import json
# url="http://saral.navgurukul.org/api/courses"
# r=requests.get(url)
# raw=r.json()
# c=0
# for j in raw['availableCourses']:
# 	c=c+1
# 	print (c,j['name'])




# c=0
# list1=[]
# for j in raw['availableCourses']:
# 	c=c+1
# 	print (c,j['name'],j['logo'])
# 	list1.append(j['logo'])
# user=int(input("appka kisa detail chahte hai........\n"))
# d=requests.get(list1[user-1]).text
# print (d)






# import requests
# import json
# def saral_data():	
# 	r=requests.get("http://saral.navgurukul.org/api/courses")
# 	a = json.loads(r.text)
# 	print (a)
# saral_data()
	
# ===============================================================================================================================================================================================================





# import requests
# import json
# import os.path
# from os import path
# def api():
# 	if path.exists("prince.json"):
# 		with open ("prince.json", "r") as pk:
# 			data=json.load(pk)
# 			# print (data)
# 	else:
# 		url="http://saral.navgurukul.org/api/courses"
# 		p= requests.get(url).text

# 		with open ("prince.json", "w+") as pk:
# 			pk.write(p)
# 			data=json.loads(p)
# 			# print(data)
# 	count=0
# 	courses=[]
# 	for i in data['availableCourses']:
# 		count+=1
# 		a=count,i['name']
# 		courses.append(i['id'])
# 		print (a)
# 	user=int(input())
# 	new_url="http://saral.navgurukul.org/api/courses/"+str(courses[user-1])+"/exercises"
# 	q=requests.get(new_url).text
# 	q1=json.loads(q)
# 	print (q1)
# 	cou=1
# 	slug=[]
# 	for i in q1['data']:
# 		slug.append(i['slug'])
# 		print (cou,i['name'],"\n","           ",json.dumps(i['parentExerciseId']))
# 		if i['parentExerciseId']==None:
# 			print (i['slug'])
# 		cou+=1
# api()








# ====================================================================================================================================================================================================================





# import requests
# import json
# import os.path
# from os import path
# def api():
# 	if path.exists("prince.json"):
# 		with open ("prince.json", "r") as pk:
# 			data=json.load(pk)
# 			# print (data)
# 	else:
# 		url="http://saral.navgurukul.org/api/courses"
# 		p= requests.get(url).text

# 		with open ("prince.json", "w+") as pk:
# 			pk.write(p)
# 			data=json.loads(p)
# 			# print(data)
# 	count=0
# 	courses=[]
# 	for i in data['availableCourses']:
# 		count+=1
# 		a=count,i['name']
# 		courses.append(i['id'])
# 		print (a)
# 	user=int(input())
# 	new_url="http://saral.navgurukul.org/api/courses/"+str(courses[user-1])+"/exercises"
# 	q=requests.get(new_url).text
# 	q1=json.loads(q)
# 	# print (q1)
# 	cou=1
# 	slug=[]
# 	ID=[]
# 	for i in q1['data']:
# 		slug.append(i['slug'])
# 		print (cou,i['name'])
# 		cou+=1
# 	# print (slug)
# 	user1=int(input())
# 	new_url1="http://saral.navgurukul.org/api/courses/"+str(courses[user-1])+"/exercise/getBySlug?slug="+str(slug[user1-1])
# 	# print (new_url1)
# 	s1=requests.get(new_url1).text
# 	s2=json.loads(s1)
# 	print (s1)
# api()



# =======================================================================================================================================================================================================







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
	



