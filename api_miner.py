import requests
import json

s = requests.Session()

posts = s.get('https://jsonplaceholder.typicode.com/posts')

# users.json() holds complete user data in list
users = s.get('https://jsonplaceholder.typicode.com/users')

# loading user data into variable
data = users.json() # this is list
post = posts.json() # this is list

# this function return list of user id in list
def user_ids():
    user_list = []
    for i in data:
        user_list.append(i['id'])  # taking only value of key 'id'
    return user_list

# storing list to a variable
user_ids_list = user_ids()

# Initializing the dictionary and list
full_dict = { 'userId':'', 'username':'', 'city':'', 'postId':'', 'title':''}
full_data = []

# this funtion returns user details for supplied userId in list which includes id, username, address, city
def user_details(userId):
    for i in data:
        if i['id'] == userId:
            return [i['id'], i['username'], i['address']['city']]

'''
Picking one user from user_ids_list, and taking one post from post list
check wether the userId of post matches with picked user from the list
since posts are arranged in ascending order with respect user such 111,222,333 it will not miss any post

'''
counter = 0
for i in user_ids_list:
    for j in post:
        counter += 1
        if j['userId'] == i:
            value_list = user_details(i)
            value_list.append(j['id'])
            value_list.append(j['title'])
            # zipping dict and value list
            res = dict(zip(full_dict, value_list))
            # appedning to full_data list of zipped dict
            full_data.append(res)

# saving result to outfile
with open("result.json", "w") as outfile:
    outfile.write(json.dumps(full_data))
    print('loaded successfully')

print(counter) 
# counter value 1000 for 10 user, and 100 posts

# converting json data into string
# jposts = json.dumps(posts.json())
# jusers = json.dumps(users.json())
# data = json.loads(json.dumps(users.json()))

# with open("posts.json", "w") as outfile:
#     outfile.write(jposts)

# with open("users.json", "w") as outfile:
#     outfile.write(jusers)
# with open("users.json", "r") as read_file:
#     data = json.load(read_file)

# print(type(data[0]["username"]))
# print(data[0]["username"])

# if its a dict need to use the key to read the value
# print(type(data[0]['address']))
# print(data[0]['address']['geo']['lat'])

# extracting only keys from the dict 
# print((data[0]['address']).keys())
# print((data[0]).keys())         

# here data is list, and each objects in the list is a dict, reading id from dict

# Can print the title from post of first user
# for i in post:
#     if i['userId'] == 1:
#         print(i['title'])

# userId, username, city, postid, title
# need two functions for details and another function to bind it to json list

'''
Create a empyt dictionary with
dict = { 'userId':'', 'username':'', 'city':'', 'postId':'', 'title':''}
Create a empyt value list to append the values of above dict
value_list = []

Take one user id, since post is in the order of user id, 
compare the post list with userId and take post id and address from that user
then store it to list if it matches with post's user id.

for i in user_list:
    for j in post:
        if j[userId] == i:
            print(j[id])

'''
