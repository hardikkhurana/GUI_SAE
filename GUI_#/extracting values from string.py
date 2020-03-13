def extract_voltage():
    s="0.00V 0% -100 *c -100 *c 100km/h"
    x=s.index("V")
    voltage=float((s[:x]))    
    print (voltage)
    s=(s[(x+2):])
    x=s.index("%")    
    battery_percentage=int(s[:x])
    print(battery_percentage)
    s=(s[(x+3):])
    x=s.index(" ")    
    battery_temp=float(s[:x])
    print(battery_temp)
    s=(s[(x+5):])
    x=s.index(" ")    
    motor_temp=float(s[:x])
    print(motor_temp)
    s=(s[(x+4):])
    x=s.index("k")
    speed=int(s[:x])
    print(speed)

extract_voltage()
    
