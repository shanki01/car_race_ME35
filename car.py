#gets value from airtable and sends main() to 2040 to start loop 

import serial
s = serial.Serial('COM9', baudrate=115200)

import requests
URL = 'https://api.airtable.com/v0/apphXum5G3hbhYwyE/Car'
Base_ID = 'apphXum5G3hbhYwyE'
Token = 'pat2cv1bwUeJkcSyg.ecd085b2cf8ef7bca193b976228aeb5c86757efd4ed2981eededf02d0bfc8f7e'
headers = {'Authorization':'Bearer '+Token}
r = requests.get(URL,headers = headers)
print(r.status_code)
data = r.json()
value = data['records'][1]['fields']['Value']
print(value)

if value == 'Start':
    print('works')
    s.write(b'import run\r\n')
    s.write(b'run.main()\r\n')


print(s.read_all())
s.close()

