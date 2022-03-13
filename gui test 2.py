import tkinter as tk
root = tk.Tk()
root.geometry("400x240")

def setTextInput(text):
    textExample.delete(1.0,"end")
    textExample.insert(1.0, text)

textExample = tk.Text(root, height=10)
textExample.pack()

btnSet = tk.Button(root, 
                   height=1, 
                   width=10, 
                   text="Set", 
                   command=lambda:setTextInput("new content"))
btnSet.pack()

root.mainloop()