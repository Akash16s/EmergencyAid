from firebase import firebase
import tkinter as tk

firebase = firebase.FirebaseApplication('https://emergencyhospital-c9f88.firebaseio.com/')

counter = 0
counter = firebase.get('/Management/Hospitals/H1/availableBeds',None)

def add():
    global counter
    counter = counter + 1
    label.config(text=str(counter))
    firebase.patch('/Management/Hospitals/H1', {'availableBeds': counter})


def sub():
    global counter
    counter = counter - 1
    label.config(text=str(counter))
    firebase.patch('/Management/Hospitals/H1', {'availableBeds': counter})


root = tk.Tk()
root.title( 'H1')
frame = tk.Frame(root)
frame.pack()
SUB = tk.Button(frame, text="-", font=("Helvetica", 25), fg="red", width=15, height= 5, command=sub)
SUB.pack(side=tk.LEFT )
ADD = tk.Button(frame, text="+", font=("Helvetica", 25), fg='green', width=15, height= 5, command=add)
ADD.pack(side=tk.LEFT)
label = tk.Label(root, fg="black")
label.config(text=str(counter),font=("Helvetica", 25))
label.pack(side = tk.TOP)

root.mainloop()


