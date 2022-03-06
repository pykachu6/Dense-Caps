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


def buttonreset():
    print(1)
    

    
def printInput():
#     print('Hey get values from here')
    val_formula = inputtxt_formula.get("1.0","end-1c")
    val_spacegroup = inputtxt_spacegroup.get("1.0","end-1c")
    val_formationenergy = inputtxt_formationenergy.get("1.0","end-1c")
    val_bandgap = inputtxt_bandgap.get("1.0","end-1c")
    val_density = inputtxt_density.get("1.0","end-1c")
    
    
    outputtxt_formula.configure(state  = "normal")
    outputtxt_spacegroup.configure(state  = "normal")
    outputtxt_formationenergy.configure(state  = "normal")
    outputtxt_bandgap.configure(state  = "normal")
    outputtxt_density.configure(state  = "normal")

    outputtxt_formula.delete(1.0,"end")
    outputtxt_spacegroup.delete(1.0,"end")
    outputtxt_formationenergy.delete(1.0,"end")
    outputtxt_bandgap.delete(1.0,"end")
    outputtxt_density.delete(1.0,"end")
    
    formula_model = 0
    formula_spacegroup = 0
    formula_formationenergy = 0
    formula_bandgap = 0
    formula_density = 0
    
    if val_formula == "":
        input_blank_label["text"]= "At least enter the formula"
    
    if val_formula != "":
        outputtxt_formula.insert(1.0, val_formula)
        formula_model = 1

    if val_spacegroup != "":
        outputtxt_spacegroup.insert(1.0, val_spacegroup)
        spacegroup_model = 1
        
    if val_formationenergy != "":
        outputtxt_formationenergy.insert(1.0, val_formationenergy)
        formationenergy_model = 1

    if val_bandgap != "":
        outputtxt_bandgap.insert(1.0, val_bandgap)
        bandgap_model = 1

    if val_density != "":
        outputtxt_density.insert(1.0, val_density)
        density_model = 1

    outputtxt_formula.configure(state  = "disabled")
    outputtxt_spacegroup.configure(state  = "disabled")
    outputtxt_formationenergy.configure(state  = "disabled")
    outputtxt_bandgap.configure(state  = "disabled")
    outputtxt_density.configure(state  = "disabled")
        
# Input Widget
row = 0
col = 0
input_label = tk.Label(win, text="Inputs: ", font=('Aerial 11')).grid(row=row, column=col,sticky = ' ', columnspan = 3)

# Input Blank Widget
row = 1
col = 0
input_blank_label = tk.Label(win, text=" ", font=('Aerial 11'))
input_blank_label.grid(row=row, column=col,sticky = ' ', columnspan = 3)

# Output Widget
row = 0
col = 2
tk.Label(win, text=" ", font=('Aerial 11')).grid(row=row, column=col,sticky = ' ', columnspan = 3)


output_label = tk.Label(win, text="Outputs: ", font=('Aerial 11')).grid(row=row, column=col,sticky = ' ', columnspan = 3)



# Formula Widget
row = 2
tk.Label(win, text="Formula: ", font=('Aerial 11')).grid(row=row, column=0,stick = W)
inputtxt_formula = tk.Text(win, height = 1, width = 15)
inputtxt_formula.grid(row=row, column=1,stick = W)

tk.Label(win, text="   ", font=('Aerial 11')).grid(row=row, column=2,sticky = ' ')

outputtxt_formula = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_formula.grid(row=row, column=3,stick = W)

# Space Group Widget
row = 3
tk.Label(win, text="Space Group: ", font=('Aerial 11')).grid(row=row, column=0,stick = W)
inputtxt_spacegroup = tk.Text(win, height = 1, width = 15)
inputtxt_spacegroup.grid(row=row, column=1,stick = W)

outputtxt_spacegroup = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_spacegroup.grid(row=row, column=3,stick = W)

# Formation Energy Widget
row = 4
tk.Label(win, text="Formation Energy (eV): ", font=('Aerial 11')).grid(row=row, column=0,stick = W)
inputtxt_formationenergy = tk.Text(win, height = 1, width = 15)
inputtxt_formationenergy.grid(row=row, column=1,stick = W)

outputtxt_formationenergy = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_formationenergy.grid(row=row, column=3,stick = W)

# Band Gap Widget
row = 5
tk.Label(win, text="Band Gap (ev): ", font=('Aerial 11')).grid(row=row, column=0,stick = W)
inputtxt_bandgap = tk.Text(win, height = 1, width = 15)
inputtxt_bandgap.grid(row=row, column=1,stick = W)

outputtxt_bandgap = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_bandgap.grid(row=row, column=3,stick = W)

# Density Widget
row = 6
tk.Label(win, text="Density (gm/cc): ", font=('Aerial 11')).grid(row=row, column=0,stick = W)
inputtxt_density = tk.Text(win, height = 1, width = 15)
inputtxt_density.grid(row=row, column=1,stick = W)

outputtxt_density = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_density.grid(row=row, column=3,stick = W)

# Input and Reset Button Widget
row = 7
Buttons = tk.Frame(win)
Buttons.grid(row=row, column=1)

printButton = tk.Button(Buttons,text = "Print", command = printInput, width = 7)
printButton.grid(row=0, column=2,stick = ' ', columnspan = 1)

resetButton = tk.Button(Buttons,text = "Reset", command = buttonreset, width = 7)
resetButton.grid(row=0, column=1,stick = '', columnspan = 1)
# Bind the ESC key with the callback function
win.bind('<Escape>', lambda e: close_win(e))

win.mainloop()
