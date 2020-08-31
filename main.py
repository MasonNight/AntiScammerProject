import os
import random
import requests
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

print('Program Started.')
url = 'https://www.sunwesttrust.com/login.microsoftonline.com/SAMLRequest.php'

firstNames = json.loads(open('nameList.json').read())
lastNames = json.loads(open('lastNameList.json').read())


while 1:
    username = random.choice(firstNames).lower() + '.' + random.choice(lastNames).lower() +'@siu.edu'
    password = ''.join(random.choice(chars) for i in range(15))

    requests.post(url, allow_redirects=False, data={
        'textfield': username,
        'textfield2': password
    })
    print('Sending username %s and password %s' % (username, password))



