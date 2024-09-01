import requests
from random import *

ssesion = requests.Session()


req = requests.get(f'https://randomuser.me/api/?nat=us')
r = req.json()['results'][0]
first = r['name']['first']
last = r['name']['last']
mail = r['email']

cookies = {
        '_gcl_au': '1.1.731619426.1684510916',
        '_ga': 'GA1.1.760488622.1684510916',
        'optiMonkClientId': 'b91f7bfb-a8f8-a5ab-c384-000535d27fbc',
        'optiMonkSession': '1684510921',
        'ci_session': 'vma2n5lp26ht3o7b0macbrv8dsh4nt48',
        'optiMonkClient': 'N4IgjA7ALAHArAThALlAYwIYtAZmyDNAFxQAYAaAgByrMrQCcUQA2HSKAEzAFMoIATJxxpSpATgBmIzmk4hKAOwD285KQC+GypIBuKMCxhQ4YUggEUQAG33JDx02DgmlyqnYFagA',
        '_ga_4HXMJ7D3T6': 'GS1.1.1684510916.1.1.1684511611.0.0.0',
        '_ga_KQ5ZJRZGQR': 'GS1.1.1684510916.1.1.1684511611.0.0.0',
    }

headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'es-ES,es;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.lagreeod.com',
        'Referer': 'https://www.lagreeod.com/subscribe',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

list = ['xvpdohon-rotate:j3hvas2j91cd','bnvudhvm-rotate:jkgnyp9lecnr','kpsldceh-rotate:58keli6fhazy','urzeqtzv-rotate:f24yk1gwccta','oiinvlnx-rotate:r2lx2vr4jbjo','hftsdyhr-rotate:iziwp0qs6av1']

rndp  =   choices(list)
ip = rndp[0]
proxya = {"http": f"http://{ip}@p.webshare.io:80/",}