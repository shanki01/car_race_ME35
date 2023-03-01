#main reads buttons and sends number to ESP (not sending right now, getting error), then ESP has a function Publish(IP,number) that sends the number to the car

def main():
    from machine import UART, Pin, Timer
    import time
    import functions
    
    button = Pin(16, Pin.IN, Pin.PULL_UP)
    led = Pin(13, Pin.OUT)
    status = button.value()
    t = time.ticks_ms()
    sum = 0
    num = 0
    s = functions.serial_comm(115200)
    s.abort()
    s.send_code('import Publish')
    s.read()
    while True:
        led.off()
        status = not button.value()
        if status:
            start = time.ticks_ms()
            count = 0
            
            while time.ticks_ms()-start < 3000:
                status = not button.value()
                led.on()
                time.sleep_ms(100)
                led.off()
                if status:
                    count = count +1
                time.sleep(0.01)
            print('count',count)
            if count < 10:
                num = 1
                s.abort()
                s.send_code('Publish.send("10.247.37.202","1")')
                print(num)
            if count > 10:
                num = 2
                s.abort()
                s.send_code('Publish.send("10.247.37.202","2'')')
                print(num)
