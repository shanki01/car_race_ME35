import time
import machine

from secrets import Tufts_Wireless as wifi
import mqtt_CBR

mqtt_broker = '10.245.153.182' 
topic_sub = 'class/#'
topic_pub = 'class/Sophie'
client_id = 'MyESP_sophieandmadeline'

mqtt_CBR.connect_wifi(wifi)
led = machine.Pin(2, machine.Pin.OUT)  # 6 for 2040

def blink(delay = 0.1):
    led.off()
    time.sleep(delay)
    led.on()
    
def whenCalled(topic, msg):
    print((topic.decode(), msg.decode()))
    blink()
    time.sleep(0.5)
    blink()
        
def main():
    fred = mqtt_CBR.mqtt_client(client_id, mqtt_broker, whenCalled)
    fred.subscribe(topic_sub)

    old = 0
    i = 0
    while True:
        try:
            fred.check()
            if (time.time() - old) > 5:
                msg = 'purple'
                fred.publish(topic_pub, msg)
                old = time.time()
                i += 1
                blink()
        except OSError as e:
            print(e)
            fred.connect()
        except KeyboardInterrupt as e:
            fred.disconnect()
            print('done')
            break
    
main()