import tkinter as tk

root = tk.Tk()
root.title("Mijn eerste GUI")
root.geometry("800x600+200+200")

label = tk.Label(root, text="Hallo tk!")
label.pack()

root.mainloop()