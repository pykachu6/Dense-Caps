# Import the required libraries
from tkinter import *
import tkinter as tk
import predictor

# Create an instance of tkinter win
win = Tk()
win.title('Dunce Cap GUI (Based off of lithium-ion batteries.csv)')
# Set the size of the tkinter window
win.geometry('600x300')



# Define an event to close the window
def close_win(e):
   win.destroy()


def buttonreset():
    
    listofoutputs = [outputtxt_formula,outputtxt_nsites,outputtxt_formationenergy,outputtxt_bandgap, outputtxt_density,outputtxt_volume,outputtxt_structure,
                     outputtxt_nsites_score,outputtxt_formationenergy_score,outputtxt_bandgap_score, outputtxt_density_score,outputtxt_volume_score,outputtxt_structure_score]
    for i in range(0,len(listofoutputs)):
        listofoutputs[i].configure(state = 'normal')
        listofoutputs[i].delete(1.0,'end')
        listofoutputs[i].configure(state = 'disabled')
        
    listofinputs = [inputtxt_formula,inputtxt_nsites,inputtxt_formationenergy,inputtxt_bandgap, inputtxt_density,inputtxt_volume]
    
    for i in range(0,len(listofinputs)):
        listofinputs[i].delete(1.0,'end')
    input_blank_label['text']= ' '
    
    
def printInput():
    
    listofoutputs = [outputtxt_formula,outputtxt_nsites,outputtxt_formationenergy,outputtxt_bandgap, outputtxt_density,outputtxt_volume,outputtxt_structure,
                     outputtxt_nsites_score,outputtxt_formationenergy_score,outputtxt_bandgap_score, outputtxt_density_score,outputtxt_volume_score,outputtxt_structure_score]

    listofinputs = [inputtxt_formula,inputtxt_nsites,inputtxt_formationenergy,inputtxt_bandgap, inputtxt_density,inputtxt_volume]
    
    for i in range(0,len(listofoutputs)):
        listofoutputs[i].configure(state = 'normal')
        listofoutputs[i].delete(1.0,'end')
    
    
    val_formula = inputtxt_formula.get('1.0','end-1c')
    val_nsites = inputtxt_nsites.get('1.0','end-1c')
    val_formationenergy = inputtxt_formationenergy.get('1.0','end-1c')
    val_bandgap = inputtxt_bandgap.get('1.0','end-1c')
    val_density = inputtxt_density.get('1.0','end-1c')
    val_volume = inputtxt_volume.get('1.0','end-1c')
    

    
    
    
    if val_formula == '':
        input_blank_label['text']= 'At least enter the formula'
        
    else:
        
        Overall_value, Scores = predictor.value_finder(formula = val_formula, 
                                     formation_e   = val_formationenergy,
                                     bandgap_input = val_bandgap,
                                     Nsites  = val_nsites,
                                     Density = val_density,
                                     Volume  = val_volume)
        if val_formula != '':
            outputtxt_formula.insert(1.0, val_formula)
            
        if val_nsites != '':
            outputtxt_nsites.insert(1.0, val_nsites)
        else:
            outputtxt_nsites.insert(1.0, int(Overall_value['Nsites']))
            outputtxt_nsites_score.insert(1.0, Scores['Nsites'])
            
        if val_formationenergy != '':
            outputtxt_formationenergy.insert(1.0, val_formationenergy)
        else:
            outputtxt_formationenergy.insert(1.0, Overall_value['Formation Energy (eV)'])
            outputtxt_formationenergy_score.insert(1.0, Scores['Formation Energy (eV)'])
            
        if val_bandgap != '':
            outputtxt_bandgap.insert(1.0, val_bandgap)
        else:
            outputtxt_bandgap.insert(1.0, Overall_value['Band Gap (eV)'])
            outputtxt_bandgap_score.insert(1.0, Scores['Band Gap (eV)'])
            
        if val_density != '':
            outputtxt_density.insert(1.0, val_density)
        else:
            outputtxt_density.insert(1.0, Overall_value['Density (gm/cc)'])
            outputtxt_density_score.insert(1.0, Scores['Density (gm/cc)'])
                    
        if val_volume != '':
            outputtxt_volume.insert(1.0, val_volume)
        else:
            outputtxt_volume.insert(1.0, Overall_value['Volume'])
            outputtxt_volume_score.insert(1.0, Scores['Volume'])
        
        outputtxt_structure.insert(1.0, Overall_value['Crystal System'])
        outputtxt_structure_score.insert(1.0, Scores['Crystal System'])

        input_blank_label['text']= ''
    
    
    for i in range(0,len(listofoutputs)):
        listofoutputs[i].configure(state = 'disabled')
    
# Input Widget
row = 0
col = 0
input_label = tk.Label(win, text='Inputs: ', font=('Aerial 11')).grid(row=row, column=col,sticky = ' ', columnspan = 3)

# Input Blank Widget
row = 1
col = 0
input_blank_label = tk.Label(win, text=' ', font=('Aerial 11'))
input_blank_label.grid(row=row, column=col,sticky = ' ', columnspan = 3)

# Output Widget
row = 0
col = 2
tk.Label(win, text=' ', font=('Aerial 11')).grid(row=row, column=col,sticky = ' ', columnspan = 3)
output_label = tk.Label(win, text='Outputs: ', font=('Aerial 11')).grid(row=row, column=col,sticky = ' ', columnspan = 3)

def hidden():
    from PIL import ImageTk, Image

    root = tk.Toplevel()
    path = '6485498.png'
    img = ImageTk.PhotoImage(Image.open(path))  
    panel = tk.Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    root .mainloop()


row = 1
output_value_label = tk.Label(win, text='Value', font=('Aerial 11')).grid(row=row, column=3,sticky = ' ')
output_score_label = tk.Label(win, text='Score', font=('Aerial 11')).grid(row=row, column=4,sticky = ' ')
hiddenbutton = tk.Button(win, text=' ', font=('Aerial 11'),bd=0, command = hidden)
hiddenbutton.grid(row=2, column=4,sticky = ' ')


# Formula Widget
row = 2
tk.Label(win, text='Formula: ', font=('Aerial 11')).grid(row=row, column=0,stick = W)
inputtxt_formula = tk.Text(win, height = 1, width = 15)
inputtxt_formula.grid(row=row, column=1,stick = W)

tk.Label(win, text='   ', font=('Aerial 11')).grid(row=row, column=2,sticky = ' ')

outputtxt_formula = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_formula.grid(row=row, column=3,stick = W)

# Nsites Widget
row = 3
tk.Label(win, text='Number Sites: ', font=('Aerial 11')).grid(row=row, column=0,stick = W)
inputtxt_nsites = tk.Text(win, height = 1, width = 15)
inputtxt_nsites.grid(row=row, column=1,stick = W)

outputtxt_nsites = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_nsites.grid(row=row, column=3,stick = W)
outputtxt_nsites_score = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_nsites_score.grid(row=row, column=4,stick = W)

# Formation Energy Widget
row = 4
tk.Label(win, text='Formation Energy (eV): ', font=('Aerial 11')).grid(row=row, column=0,stick = W)
inputtxt_formationenergy = tk.Text(win, height = 1, width = 15)
inputtxt_formationenergy.grid(row=row, column=1,stick = W)

outputtxt_formationenergy = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_formationenergy.grid(row=row, column=3,stick = W)
outputtxt_formationenergy_score = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_formationenergy_score.grid(row=row, column=4,stick = W)

# Band Gap Widget
row = 5
tk.Label(win, text='Band Gap (ev): ', font=('Aerial 11')).grid(row=row, column=0,stick = W)
inputtxt_bandgap = tk.Text(win, height = 1, width = 15)
inputtxt_bandgap.grid(row=row, column=1,stick = W)

outputtxt_bandgap = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_bandgap.grid(row=row, column=3,stick = W)
outputtxt_bandgap_score = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_bandgap_score.grid(row=row, column=4,stick = W)

# Density Widget
row = 6
tk.Label(win, text='Density (gm/cc): ', font=('Aerial 11')).grid(row=row, column=0,stick = W)
inputtxt_density = tk.Text(win, height = 1, width = 15)
inputtxt_density.grid(row=row, column=1,stick = W)

outputtxt_density = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_density.grid(row=row, column=3,stick = W)
outputtxt_density_score = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_density_score.grid(row=row, column=4,stick = W)

# Volume Widget
row = 7
tk.Label(win, text='Volume: ', font=('Aerial 11')).grid(row=row, column=0,stick = W)
inputtxt_volume = tk.Text(win, height = 1, width = 15)
inputtxt_volume.grid(row=row, column=1,stick = W)

outputtxt_volume = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_volume.grid(row=row, column=3,stick = W)
outputtxt_volume_score = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_volume_score.grid(row=row, column=4,stick = W)

# Structure:
row = 8
tk.Label(win, text='Structure', font=('Aerial 11')).grid(row=row, column=0,stick = W)

outputtxt_structure = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_structure.grid(row=row, column=3,stick = W)
outputtxt_structure_score = tk.Text(win, height = 1, width = 15,state='disable', bg = '#DCDCDC')
outputtxt_structure_score.grid(row=row, column=4,stick = W)

# Input and Reset Button Widget
row = 9
Buttons = tk.Frame(win)
Buttons.grid(row=row, column=1)

printButton = tk.Button(Buttons,text = 'Print', command = printInput, width = 7)
printButton.grid(row=0, column=2,stick = ' ', columnspan = 1)

resetButton = tk.Button(Buttons,text = 'Reset', command = buttonreset, width = 7)
resetButton.grid(row=0, column=1,stick = '', columnspan = 1)
# Bind the ESC key with the callback function
win.bind('<Escape>', lambda e: close_win(e))

win.mainloop()

