import tkinter
from calculate import Calcul

window = tkinter.Tk()
window.title("Convertisseur Miles > KM")
window.minsize(width=500,height=300)
window.config(padx=100,pady=100)

def calculate_entry():
    first_entry_value = int(first_entry.get())
    calculus = Calcul(n=first_entry_value)

    second_entry.delete(0,tkinter.END)
    second_entry.insert(0,calculus.calculate())

first_entry = tkinter.Entry(width=20)
first_entry.grid(column=3,row=1,pady="20")

first_text = tkinter.Label(text="Miles")
first_text.grid(column=4,row=1)

second_text = tkinter.Label(text="est égal à ")
second_text.grid(column=2,row=2,padx=10)

second_entry = tkinter.Entry(width=20)
second_entry.grid(column=3,row=2,pady="20")

third_label = tkinter.Label(text=" Kilomètres.")
third_label.grid(column=4,row=2,padx=10)

calcul_button = tkinter.Button(text="Calcul", command=calculate_entry)
calcul_button.grid(column=3,row=3)

window.mainloop()