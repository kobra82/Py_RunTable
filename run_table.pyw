from tkinter import *
from tkinter import ttk
from datetime import *

def calcola():
    data_iniziale=first_entry.get()
    data_finale=second_entry.get()
    percentuale=int(first_combobox.get())
    a=datetime.strptime(data_iniziale, "%d/%m/%Y")
    b=datetime.strptime(data_finale, "%d/%m/%Y")
    if (percentuale == 0):
        data_media=a
    elif (percentuale == 100):
        data_media=b
    else:
        data_media=(a+(timedelta(days=((b-a).days+1)*round((percentuale/100),2))))
    fourth_entry=Entry(root, width=10, takefocus=0)
    fourth_entry.grid(row=1, column=4, padx=10)
    fourth_entry.insert(END, str(data_media.strftime("%d/%m/%Y")))

root=Tk()
root.resizable(False, False)
root.title("Tabella di marcia")
first_label=Label(root, text="Data Iniziale: ")
first_label.grid(row=0, column=0, padx=10)
first_entry=Entry(root, width=10)
first_entry.grid(row=1, column=0, padx=10, pady=5)
first_entry.focus()
second_label=Label(root, text="Data Finale: ")
second_label.grid(row=0, column=1, padx=10)
second_entry=Entry(root, width=10)
second_entry.grid(row=1, column=1, padx=10, pady=5)
third_label=Label(root, text="%")
third_label.grid(row=0, column=2, padx=10)
perc_sel=IntVar()
first_combobox=ttk.Combobox(root, textvariable=perc_sel, width=3, values=[perc_sel for perc_sel in range(101)])
first_combobox.grid(row=1, column=2, padx=10)
forth_label=Label(root, text="Endline data: ")
forth_label.grid(row=0, column=4, padx=10)
first_button=Button(root, text="Calculate", command=calcola, height=2)
first_button.grid(row=0, column=3, rowspan=2)
fourth_entry=Entry(root, width=10, takefocus=0)
fourth_entry.grid(row=1, column=4, padx=10)
    
root.mainloop()