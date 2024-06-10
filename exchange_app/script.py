import requests

response1 = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response1)
task_info1 = response1.json()
print(task_info1)

updated_post = { 'title': 'updated title', 'body': 'updated body', 'userId': 1 }
response5 = requests.put('https://jsonplaceholder.typicode.com/posts/1', json = updated_post)
print(response5)
task_info5 = response5.json()
print(task_info5)
print(task_info5['title'].capitalize())

response3 = requests.post('https://jsonplaceholder.typicode.com/posts', {'title' : 'gooowno'})
print(response3)
task_info3 = response3.json()
print(task_info3)
print(task_info3['title'].capitalize())

response2 = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response2)
task_info2 = response2.json()
print(task_info2)

response3 = requests.put('https://jsonplaceholder.typicode.com/posts/1', {'type' : 'gooowno'})
print(response3)
task_info3 = response3.json()
print(task_info3)
print(task_info3['type'].capitalize())



'''
if response.status_code == 200:
    task_info = response.json()
    print(task_info['title'].capitalize())
else:
    print('failed')
'''