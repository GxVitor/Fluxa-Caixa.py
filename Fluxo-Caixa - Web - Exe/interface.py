import tkinter as tk
import subprocess

app_process = None

def start_program():
    global app_process
    app_process = subprocess.Popen(["python", "app.py"])

def interfaceWeb():
    subprocess.Popen(["python", "setup.py"])

root = tk.Tk()
root.title("Fluxo de CAIXA")

start_button = tk.Button(root, text="Iniciar", command=start_program)
start_button.pack()

start_button = tk.Button(root, text="Interface", command=interfaceWeb)
start_button.pack()


root.mainloop()
