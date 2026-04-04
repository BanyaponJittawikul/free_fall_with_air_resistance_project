import math

def velocity_calculate(h):
    return math.sqrt(2*9.81*h)
    
    

def time_calculate(h):
    return math.sqrt((h*2)/9.81)
    
    

def air_resistance_calculate(p, v, Cd, A):
    return 0.5*p*(v**2)*Cd*A
    

def gravitational_force_calculate(m):
    return m*9.81 #9.81 คือแรงโน้มถ่วง(g)

def accleration_calculate(m, Fd):
    return ((m*9.81)-Fd)/m