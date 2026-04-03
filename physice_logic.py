import math

def velocity_calculate(high_float):
    try:
        return math.sqrt(2*9.81*high_float)
    except ValueError:
        return "Error: กรุณาใส่ตัวเลข"
    

def time_calculate(high_float):
    try:
        return math.sqrt((high_float*2)/9.81)
    except ValueError:
        return "Error: กรุณาใส่ตัวเลข"
    

def air_resistance_calculate(p, v, Cd, A):
    try:
        return 0.5*p*(v**2)*Cd*A
    except ValueError:
        return "Error: กรุณาใส่ตัวเลข"