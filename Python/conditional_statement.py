def question1():
    v = 3.35
    print("Under Voltage" if v < 3.0 else "Over Voltage" if v > 3.3 else "Nominal")

def question2():
    reg = 0b10010010
    print("MSB set" if reg & 0b10000000 else "MSB not set")

def question3():
    t = 18
    print("Overheat" if t > 75 else "Low Temp" if t < 25 else "Normal")

def question4():
    a,b = 1,0
    print(f"AND: {a&b}, OR: {a|b}, XOR: {a^b}")

def question5():
    s = 950
    print("Sensor Fault" if s < 100 or s > 900 else "Sensor OK")

def question6():
    code = 230
    print("Critical" if code >= 1000 else "Warning" if code >= 100 else "Info")

def question7():
    power_on, overcurrent, overvoltage = True, True, False
    print("Critical Failure" if overcurrent and overvoltage else
          "Shut Down: Overcurrent" if overcurrent else
          "Shut Down: Overvoltage" if overvoltage else
          "System Safe")

def question8():
    val = 140
    print("0-63" if val < 64 else
          "64-127" if val < 128 else
          "128-191" if val < 192 else
          "192-255")

def question9():
    f = 8000
    print("Low Band" if f < 1000 else
          "Mid Band" if f < 10000 else
          "High Band" if f < 100000 else
          "Out of Range")

def question10():
    a,b,c = 40,65,70
    print("Majority High" if (a>50)+(b>50)+(c>50) >= 2 else "Majority Low")

def question11():
    n = 0xAAAA
    print("Parity: Even" if bin(n).count('1')%2==0 else "Parity: Odd")

def question12():
    v,i = 2.9,600
    print("Power Error" if (v<3.0 or v>3.3) and (i<10 or i>500) else
          "Voltage Error" if (v<3.0 or v>3.3) else
          "Current Error" if (i<10 or i>500) else
          "Power OK")

def question13():
    l1,l2,l3 = 0,1,0
    print("LED1 ON" if l1 else "", "LED2 ON" if l2 else "", "LED3 ON" if l3 else "" if l1 or l2 or l3 else "All LEDs off")

def question14():
    mode = 1
    print("Standby" if mode==0 else "Active" if mode==1 else "Fault" if mode==2 else "Unknown mode")

def question15():
    a,b = 98,101
    print("Match" if abs(a-b)<=5 else "No Match")


question1()
question2()
question3()
question4()
question5()
question6()
question7()
question8()
question9()
question10()
question11()
question12()
question13()
question14()
question15()
