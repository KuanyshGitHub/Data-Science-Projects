import requests

sites = ['https://vk.com', 'https://google.com', 'https://youtube.com']
for site in sites:
    for i in range(100):
        r = requests.get(site)
        print(site, i, r.status_code)