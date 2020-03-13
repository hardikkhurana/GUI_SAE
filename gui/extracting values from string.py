def extract_voltage():
    s="b'53.92V 88% -127 *c -127 *c 60km/h"
    print (s)
    
    s=s[2:]
    print (s)
    x=s.index("V")
    voltage=float((s[:x]))    
    print (voltage)
    s=(s[(x+2):])
    print (s)
    x=s.index("%")    
    battery_percentage=int(s[:x])
    print(battery_percentage)
    s=(s[(x+3):])
    print (s)
    x=s.index(" ")    
    battery_temp=float(s[:x])
    print(battery_temp)
    s=(s[(x+5):])
    print (s)
    x=s.index(" ")    
    motor_temp=float(s[:x])
    print(motor_temp)
    s=(s[(x+4):])
    print (s)
    x=s.index("k")
    speed=int(s[:x])
    print(speed)

extract_voltage()
    
