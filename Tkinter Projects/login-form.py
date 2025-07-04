import tkinter as tk
root=tk.Tk()
root.title("Login form")
root.geometry("350x300")

heading=tk.Label(root,text="Login",fg="darkblue",font=("Arial",20,"bold"))
heading.pack(pady=10)

tk.Label(root,text="Username",font=("Poppins",10,"bold")).pack(padx=30,anchor='w')
username_entry=tk.Entry(root,relief="solid",bd=2)
username_entry.pack(padx=30,fill='x')

tk.Label(root,text="Password",font=("Poppins",10,"bold")).pack(padx=30,anchor='w')
password_entry=tk.Entry(root,show="*",relief="solid",bd=2)
password_entry.pack(padx=30,fill='x')

def login():
    username=username_entry.get()
    password=password_entry.get()
    if username=="daniahmed758@gmail.com" and password=="12345678":
        result_label.config(text="Login successful!",fg="green")
    else:
        result_label.config(text="Invalid credentials",fg="red")

def on_enter(e):
    login_btn.config(bg="#2980b9", fg="white") 
def on_leave(e):
    login_btn.config(bg="white", fg="black") 

login_btn = tk.Button(root, text="Login", command=login, fg="black", padx=20, pady=5)
login_btn.pack(pady=20)


login_btn.bind("<Enter>", on_enter)
login_btn.bind("<Leave>", on_leave)


result_label=tk.Label(root,text="")
result_label.pack()
root.mainloop()