# Import the required libraries
from tkinter import *
import tkinter as tk


# Create an instance of tkinter win
win = Tk()
win.title("Dunce Cap GUI (Based off of lithium-ion batteries.csv)")
# Set the size of the tkinter window
win.geometry("700x350")



# Define an event to close the window
def close_win(e):
   win.destroy()



def printInput():
#     print('Hey get values from here')
    val_formula = inputtxt_formula.get("1.0","end-1c")
    val_spacegroup = inputtxt_spacegroup.get("1.0","end-1c")
    val_formationenergy = inputtxt_formationenergy.get("1.0","end-1c")
    val_bandgap = inputtxt_bandgap.get("1.0","end-1c")
    val_density = inputtxt_density.get("1.0","end-1c")
    
    if val_formula == "" and val_spacegroup == "" and val_formationenergy == "" and val_bandgap == "" and val_density == "":
        blank_label["text"]= "Enter at least one field!"


# Input Widget
row = 0
input_label = tk.Label(win, text="Inputs: ", font=('Aerial 11')).grid(row=row, column=0,sticky = ' ', columnspan = 3)

# Blank Widget
row = 1
blank_label = tk.Label(win, text=" ", font=('Aerial 11'))
blank_label.grid(row=row, column=0,sticky = ' ', columnspan = 3)

# Formula Widget
row = 2
tk.Label(win, text="Formula: ", font=('Aerial 11')).grid(row=row, column=0,stick = W)
inputtxt_formula = tk.Text(win, height = 1, width = 20)
inputtxt_formula.grid(row=row, column=1,stick = W)
  
# Space Group Widget
row = 3
tk.Label(win, text="Space Group: ", font=('Aerial 11')).grid(row=row, column=0,stick = W)
inputtxt_spacegroup = tk.Text(win, height = 1, width = 20)
inputtxt_spacegroup.grid(row=row, column=1,stick = W)

# Formation Energy Widget
row = 4
tk.Label(win, text="Formation Energy (eV): ", font=('Aerial 11')).grid(row=row, column=0,stick = W)
inputtxt_formationenergy = tk.Text(win, height = 1, width = 20)
inputtxt_formationenergy.grid(row=row, column=1,stick = W)

# Band Gap Widget
row = 5
tk.Label(win, text="Band Gap (ev): ", font=('Aerial 11')).grid(row=row, column=0,stick = W)
inputtxt_bandgap = tk.Text(win, height = 1, width = 20)
inputtxt_bandgap.grid(row=row, column=1,stick = W)

# Density Widget
row = 6
tk.Label(win, text="Density (gm/cc): ", font=('Aerial 11')).grid(row=row, column=0,stick = W)
inputtxt_density = tk.Text(win, height = 1, width = 20)
inputtxt_density.grid(row=row, column=1,stick = W)


# Input Button Widget
row = 7
printButton = tk.Button(win,text = "Print", command = printInput, width = 20)
printButton.grid(row=row, column=1,stick = '', columnspan = 2)

 
# Bind the ESC key with the callback function
win.bind('<Escape>', lambda e: close_win(e))

win.mainloop()