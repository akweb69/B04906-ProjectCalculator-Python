import tkinter as tk
from tkinter import messagebox

def click(event):
    global sc_input
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(sc_input.get())
            sc_input.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
            sc_input.set("")
    elif text == "C":
        sc_input.set("")
    else:
        sc_input.set(sc_input.get() + text)

# Main application window
root = tk.Tk()
root.title("Calculator by Abu Kalam")
root.geometry("360x500")  
root.resizable(True, True)
root.configure(bg="#f0f0f0")  

# Input screen
sc_input = tk.StringVar()
screen = tk.Entry(root, textvar=sc_input, font=("Arial", 24), bd=5, relief=tk.FLAT, justify="right", bg="#ffffff", fg="#333333")
screen.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=20)

# Button configuration
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Frame for buttons
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

# Add buttons
row, col = 0, 0
for button in buttons:
    btn = tk.Button(
        btn_frame, text=button, font=("Arial", 18), padx=20, pady=20,
        bg="#0078D7" if button in "+-*/=" else "#e1e1e1",  # Operator buttons highlighted
        fg="#ffffff" if button in "+-*/=" else "#333333",  # Text color
        relief=tk.FLAT, activebackground="#005a9e", activeforeground="#ffffff"
    )
    btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Adjust button size to fit evenly
for i in range(4):
    btn_frame.columnconfigure(i, weight=1)
for j in range(5):
    btn_frame.rowconfigure(j, weight=1)

# Run the Tkinter event loop
root.mainloop()
