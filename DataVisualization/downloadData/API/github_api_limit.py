# -*- coding:utf-8 -*-
'''
github API的使用限制
'''
import requests

url = 'http://api.github.com/rate_limit'
r = requests.get(url)
print('r.status_code:', r.status_code)
respond = r.json()
print(respond)

'''
{
"resources": {
"core": {
"limit": 60,
"remaining": 60,
"reset": 1570883448
},
"search": {
"limit": 10,
"remaining": 10,
"reset": 1570879908
},
"graphql": {
"limit": 0,
"remaining": 0,
"reset": 1570883403
},
"integration_manifest": {
"limit": 5000,
"remaining": 5000,
"reset": 1570883448
}
},
"rate": {
"limit": 60,
"remaining": 60,
"reset": 1570883448
}
}
'''
