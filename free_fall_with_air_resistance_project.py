import tkinter as tk
from physice_logic import *


root = tk.Tk(screenName=None, baseName=None, className='Physics Simulation Tool', useTk=1)

def onclick():
    mass_float = mass_doub.get()
    high_float = hight_doub.get()
    cross_sec_float = cross_sec_doub.get()
    drag_co_float = drag_co_doub.get()
    fluid_den_float = fluid_den_doub.get()
    
    time = time_calculate(high_float)
    velocity = velocity_calculate(high_float)
    air_resistance = air_resistance_calculate(fluid_den_float, velocity, drag_co_float, cross_sec_float)

    output = tk.Label(root, text=f"เวลาที่ตกคือ {time.__round__(3)} m/s\nความเร็วคือ {velocity.__round__(3)} m/s\nแรงต้านอากาศ = {air_resistance.__round__(3)} N")
    output.grid(row = 6, column=1)

mass_doub = tk.DoubleVar(value=0.0) #mass
hight_doub = tk.DoubleVar(value=0.0) #initial high
cross_sec_doub = tk.DoubleVar(value=0.0) #cross sectional area
drag_co_doub = tk.DoubleVar(value=0.0) #drag coefficient
fluid_den_doub = tk.DoubleVar(value=1.225) #Fluid Density

objects_value = {"ทรงกลม" : 0.47,
                "ทรงลูกบาศก์" : 1.05}


mass_label = tk.Label(root, text="น้ำหนักวัตถุ", font=('calibre',10, 'bold'))
mass_entry = tk.Entry(root, textvariable= mass_doub, font=('calibre',10, 'normal'))

high_label = tk.Label(root, text="ความสูงเริ่มต้นที่ปล่อยวัตถุ", font=('calibre',10, 'bold'))
high_entry = tk.Entry(root, textvariable= hight_doub, font=('calibre',10, 'normal'))

cross_sec_label = tk.Label(root, text="พื้นที่หน้าตัดของวัตถุที่ปะทะอากาศ", font=('calibre',10, 'bold'))
cross_sec_entry = tk.Entry(root, textvariable= cross_sec_doub, font=('calibre',10, 'normal'))

drag_co_label = tk.Label(root, text="ค่าสัมประสิทธิ์แรงต้านอากาศ", font=('calibre',10, 'bold'))


fluid_den_label = tk.Label(root, text="ความหนาแน่นของอากาศ", font=('calibre',10, 'bold'))
fluid_den_entry = tk.Entry(root, textvariable= fluid_den_doub, font=('calibre',10, 'normal'))


button = tk.Button(root, text="test", width=50, command=onclick)


mass_label.grid(row=0, column=0, sticky="e")
mass_entry.grid(row=0, column=1)

high_label.grid(row=1, column=0, sticky="e")
high_entry.grid(row=1, column=1)

cross_sec_label.grid(row=2, column=0, sticky="e")
cross_sec_entry.grid(row=2, column=1)

fluid_den_label.grid(row=3, column=0, sticky="e")
fluid_den_entry.grid(row=3, column=1)

drag_co_label.grid(row=4, column=0, sticky="e")
for i, (object_text,object_value) in enumerate(objects_value.items()):
    tk.Radiobutton(root, text=object_text, variable=drag_co_doub, value=object_value).grid(row=4, column=1+i, padx=1)


#output_text = tk.Label(root, text="เวลาที่ใช้ตก", font=('calibre',10, 'bold'))
#output_text.grid(row=6, column=0)


button.grid(row=7, column=2)

root.mainloop()
