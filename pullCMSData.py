'''
Program to pull JSON data from CMS API
JD Linares
31Dec2021

Outputs data to data/
'''

import requests
import json


cmsDocsExamples = 'https://data.cms.gov/data.json'
r=requests.get(cmsDocsExamples)

print(json.dumps(r.json(),indent=4,))



