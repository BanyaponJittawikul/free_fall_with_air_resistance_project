import tkinter as tk
#from physics_func import physics_function

root = tk.Tk(screenName=None, baseName=None, className='Physics Simulation Tool', useTk=1)

def physics_function():
    mass_float = float(mass_doub.get())
    high_float = float(hight_doub.get())
    drag_co_float = float(drag_co_doub.get())
    
    
    
    ans = mass_float+high_float+drag_co_float



    output = tk.Label(root, text=ans)
    output.grid(row = 6, column=0)

mass_doub = tk.DoubleVar(value="") #mass
hight_doub = tk.DoubleVar(value="") #initial high
cross_sec_doub = tk.DoubleVar(value="") #cross sectional area
drag_co_doub = tk.DoubleVar() #drag coefficient
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


button = tk.Button(root, text="test", width=50, command=physics_function)


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





button.grid(row=6, column=1)

root.mainloop()
