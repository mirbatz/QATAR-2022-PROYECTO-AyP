import requests
import string
import random

def getapi(url):
    '''Receives data from an API url, returns data'''
    
    url_api = url
    req = requests.get(url_api)
    j = req.json()
    
    return j

def random_code(str_len):
    
    code = (''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(str_len)))

    return code
