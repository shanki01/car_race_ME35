import serial

s = serial.Serial('COM3', baudrate=115200)

from machine import UART

class serial_comm():
    def __init__(self, baud, timeout = 50):
        self.uart = UART(0, baud, timeout = timeout)  #tx=Pin(0), rx=Pin(1)
        self.Ctrl = {'C':'\x03','D':'\x04','E':'\x05'}
        
    def send_raw(self, text):
        self.uart.write(text.encode())
        
    def send(self, text):
        self.send_raw(text+'\r\n')
        return self.read()
        
    def send_code(self, text):
        self.send(self.Ctrl['E'])
        self.send(text.replace('\n','\r\n'))
        self.send(self.Ctrl['D'])
        
    def read(self):
        if self.any():
            reply = self.uart.read()
            return reply.decode()
        return None
        
    def readln(self):
        if self.any():
            reply = self.uart.readline()
            return reply.decode()
        return None
        
    def abort(self):
        self.send(self.Ctrl['C'])
        
    def any(self):
        return self.uart.any()

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

startcode = '''
num = 0

count = 0
accel = lsm.read_accel()
if accel[2] < 1:
    count = count +1
if count = 1:
    num = 1
'''
