from machine import ADC, Pin, Timer
import utime

#Setup for GPIO Pins
led = Pin(25,Pin.OUT)
digit = Pin(22,Pin.IN)
pump = Pin(21,Pin.OUT)

#Setting Pump to Default be Low
pump.value(0)

#Interrupt Function
def engage_water(digit):
    avg = 0
    for x in range(100):
        avg = avg + digit.value()
    avg = avg / 100
    if(avg >= 0.9):
        print("Time to water...")
        pump.value(1)
        utime.sleep(2)
        while(digit.value()>0):
            pump.value(1)
        pump.value(0)
        utime.sleep(5)
        
#Set Out 22 GPIO as Interrupt Pin
digit.irq(trigger=Pin.IRQ_RISING, handler=engage_water)

#Default Moisture to 0
digit.value(0)

#Set LED to Ensure On Status
led.value(1)

#Enter Main Loop
while True:
    print("Not time to water:",digit.value())
    utime.sleep(5)
#tim.init(freq=1.0,mode=Timer.PERIODIC,callback=tick)
