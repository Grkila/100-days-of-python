from tkinter import *

def button_clicked():
    number=int(input.get())
    label_result["text"]=round(number*1.609,2)

window = Tk()
window.title("Mile to km converter")
window.minsize(width=500,height=300)


label_Miles=Label(text="Miles",font=("Arial",24,"bold"))


label_KM=Label(text="Km",font=("Arial",24,"bold"))

label_equal=Label(text="is equal to",font=("Arial",24,"bold"))

label_result=Label(text="0",font=("Arial",24,"bold"))

button=Button(text="Calculate",command=button_clicked)

input=Entry(width=10)

input.grid(column=1,row=0)
label_Miles.grid(column=2,row=0)
label_KM.grid(column=2,row=1)
label_equal.grid(column=0,row=1)
label_result.grid(column=1,row=1)
button.grid(column=1,row=2)



window.mainloop()

