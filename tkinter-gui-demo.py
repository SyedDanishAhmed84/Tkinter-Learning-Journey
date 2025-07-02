import tkinter as tk

root=tk.Tk()
root.title("Tkinter App")
root.geometry("500x300")
label=tk.Label(root,text="Welcome to Tkinter",font=("Arial",15))
label.pack(pady=15)
def on_click():
    label.config(text="Hey Syed Danish Ahmed",fg="blue")

button=tk.Button(root,text="Show name",command=on_click)
button.pack(padx=5)

def set_blue():
    root.config(bg="blue")
def set_green():
    root.config(bg="green")
def set_yellow():
    root.config(bg="yellow")      

blue_btn=tk.Button(root,text="blue",bg="blue",fg="white",command=set_blue)
blue_btn.pack(side="left",padx=5)   

green_btn=tk.Button(root,text="green",bg="green",fg="white",command=set_green)
green_btn.pack(side="left",padx=5)   

yellow_btn=tk.Button(root,text="yellow",bg="yellow",fg="black",command=set_yellow)
yellow_btn.pack(side="left",padx=5)      

root.mainloop()
