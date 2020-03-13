import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyUSB1",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600
while True:
    read_ser=ser.readline()
    print(read_ser)
    
    
    stri=str(read_ser)
#    s="b'53.92V 88% -127 *c -127 *c 60km/h"
    print (s)
    
    stri=stri[2:]
    print (stri)
    f=stri.index("V")
    voltage=float((stri[:f]))    
    print (voltage)
    stri=(stri[(f+2):])
    print (stri)
    f=stri.index("p")    
    battery_percentage=int(stri[:f])
    print(battery_percentage)
    stri=(stri[(f+3):])
    print (stri)
    f=stri.index(" ")    
    battery_temp=float(stri[:f])
    print(battery_temp)
    stri=(stri[(f+5):])
    print (stri)
    f=stri.index(" ")    
    motor_temp=float(stri[:f])
    print(motor_temp)
    stri=(stri[(f+4):])
    print (stri)
    f=stri.index("k")
    speed=int(stri[:f])
    print(speed)

