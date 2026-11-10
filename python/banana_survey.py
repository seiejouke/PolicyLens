# A banana preferences survey written in Python with Tkinter
import tkinter as tk

root = tk.Tk()
root.title('Banana interest survey')

title = tk.Label(
    root,
    text='Please take the survey',
    font=('Arial 16 bold'),
    bg='brown',
    fg='#FF0'
)

title.pack()

name_label = tk.Label(root,
                text='What is your name?'
                )
name_label.pack()

name_inp = tk.Entry(root)
name_inp.pack()

eater_inp = tk.Checkbutton(
    root,
    text='Check this box if you eat bananas'
    )
eater_inp.pack()

num_label = tk.Label(
    root,
    text='How many bananas do you eat per day?'
)
num_label.pack()
num_inp = tk.Spinbox(root,
                from_=0,
                to=1000,
                increment=1
                )
num_inp.pack()

color_label = tk.Label(
    root,
    text='What is the best color for a banana?'
    )
color_label.pack()

color_inp = tk.Listbox(root, height=7) # only show selected item
# add choices
color_choices = (
    'Any', 'Green', 'Green-Yellow',
    'Yellow', 'Brown Spotted', 'Black'
)
for choice in color_choices:
    color_inp.insert(tk.END, choice)
color_inp.pack()

plantain_label = tk.Label(root, text='Do you eat plantains?')
plantain_label.pack()

plantain_frame = tk.Frame(root)
plantain_frame.pack()

plantain_yes_inp = tk.Radiobutton(
    plantain_frame,
    text='Yes'
    )
plantain_yes_inp.pack()

plantain_no_inp = tk.Radiobutton(
    plantain_frame,
    text='Ewww, no!'
    )
plantain_no_inp.pack()

banana_haiku_label = tk.Label(
    root,
    text='Write a haiku about banana'
    )
banana_haiku_label.pack()

banana_haiku_inp = tk.Text(root, height=3)
banana_haiku_inp.pack()

submit_btn = tk.Button(root, text='Submit Survey')
submit_btn.pack()

output_line = tk.Label(
    root,
    text='Thank you for submitting',
    anchor='w',
    justify='left'
    )
output_line.pack()

root.geometry('640x480+300+300')
root.resizable(False, False)

root.mainloop()