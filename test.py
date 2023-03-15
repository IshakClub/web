from requests import get, post, delete




print(get('http://localhost:5000/api/v2/users/1').json())
print(get('http://localhost:5000/api/v2/users/999').json())
print(get('http://localhost:5000/api/v2/users/t').json())

print(post('http://localhost:5000/api/v2/users',
           json={'surname': '1',
                 'name': '1',
                 'age': 1,
                 'position': '1',
                 'speciality': '1',
                 'address': '1',
                 'email': '1',
                 'password': 1
                 }).json())
print(post('http://localhost:5000/api/v2/users',
           json={'surname': 1,
                 'name': '1',
                 'age': '1',
                 'position': 1,
                 'speciality': 1,
                 'address': '1',
                 'email': '2',
                 'password': 1
                 }).json())
print(post('http://localhost:5000/api/v2/users',
           json={'surname': 1,
                 'name': '1',
                 'position': 1,
                 'speciality': 1,
                 'address': '1',
                 'email': '3',
                 'password': 1
                 }).json())

print(delete('http://localhost:5000/api/v2/users/2').json())
print(delete('http://localhost:5000/api/v2/users/100').json())
print(delete('http://localhost:5000/api/v2/users/t').json())