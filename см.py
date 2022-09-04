from requests import post, get

import base64

# server = 'https://people-eye.herokuapp.com'
server = 'http://localhost:5000'
# response = get(f'{server}/api/all_problems')
# print(list(response.json()['problems'][0].keys()))
# bytes = base64.b64decode(response.json()['problems'][1]['photo'])
# with open(f'exampl.jpg', "wb") as imageFile:
#    imageFile.write(bytes)
# for i in response.json()['problems']:
#    print(i)
# photo = base64.b64encode(open('пляж.jpg', 'rb').read())
# print(photo[:100])
# print(str(photo)[:100])
response = post(f'{server}/sign-up',
                json={"email": "36", "name": "оббш", "password": "jyu5m", "phone": 'yjnum', "surname": "гд"}).json()
print(response)
