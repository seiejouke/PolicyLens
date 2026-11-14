"""A policylens for searching and retreiving data from the TweedeKamer API to a local database"""

import tkinter as tk

# Create the root window
root = tk.Tk()
root.configure(bg='white')
search_text = tk.StringVar # store search text?
# Set the title
root.title("Policy lens")
# Set the root window size
root.geometry('800x600')
root.resizable(False, False)
# What does the header do?
header = tk.Frame(root, bg="#264A5F")
header.pack(fill="x")
# Use a label to show the title
title = tk.Label(
    header, # places the title into the header?
    text="POLICYLENS NL",
    font=("Arial", 16, "bold"),
    bg="#264A5F",
    fg="white",
    anchor="w",
    padx=16,
    pady=12
)
title.pack(side="left")
#---
burger_page = tk.Frame(root, bg='#FFFFFF') # stakeholder; burger
onderzoeker_page = tk.Frame(root, bg='#FFFFFF') # stakeholder; onderzoeker
#--- stakeholder function
def show_page(page): # Place at top of of script or separate function script?
    burger_page.pack_forget() # container for burger; 'forgets' depending on which is called
    onderzoeker_page.pack_forget() # container for onderzoeker; 'forget' depending on...
    page.pack(fill='both', expand=True) # make selected container/UI the sole viewed UI
#--- search bar function
def make_search_bar(parent, text_var):
    search_row = tk.Frame(parent, bg='white')
    search_row.pack(fill="x", padx=22, pady=8)
#---Search button
    search_btn = tk.Button(
        search_row,
        text='Zoeken',
        bg='#264A5F',
        fg="white",
        relief="flat",
        padx=20
    )
    search_btn.pack(side='right', fill='y', padx=(10, 0))
#---Entry field
    name_inp = tk.Entry(
        search_row,
        font=('Arial 20 bold', 16),
        insertbackground="#264A5F",
        insertwidth=4,
    )
    name_inp.configure( # Adjust the default dropshadow around the input box (looks neater)
        relief='flat',
        borderwidth=0,
        highlightthickness=1,
        highlightbackground='#CBD5DC',
        highlightcolor='#264A5F'
    )
    name_inp.pack(
        side="left",
        fill="x",
        expand=True,
        ipady=10
    )

    return name_inp   
#---
onderzoek_btn = tk.Button( # onderzoeker button
    header,
    text='Onderzoek',
    command=lambda: show_page(onderzoeker_page) # what does lambda do?
)
onderzoek_btn.pack(side='right', padx=8)
#--- BURGER CONTENT STARTS HERE!
burger_btn = tk.Button( # burger button
    header,
    text='Burger',
    command=lambda: show_page(burger_page)
)
burger_btn.pack(side='right', padx=8)
#--- 
name_label = tk.Label( # content for burger
    burger_page,
    text='Vind documenten over data en privacy',
    font=('Arial 16 bold'),
    bg='#FFFFFF', # root is already white?
    fg='#264A5F',
    anchor='w',
    padx=24,
    pady=24                  
)
name_label.pack(fill='x')
#---
name_label = tk.Label( # content for burger
    burger_page,
    text='Search for keywords; eq data, iso or NISP2',
    font=('Arial 11 bold'),
    bg='#FFFFFF', # root is already white?
    fg='#264A5F',
    anchor='w',
    padx=24,
    pady=16
)
name_label.pack(fill='x') # Placing the label as a widget
#---

#--- ONDERZOEKER CONTENT STARTS HERE!
research_heading = tk.Label(
    onderzoeker_page, # function for onderzoeker container
    text='Onderzoek parlementarire documenten',
    font=('Arial 16 bold'),
    bg='#FFFFFF', # root is already white?
    fg='#264A5F',
    anchor='w',
    padx=24,
    pady=24
)
research_heading.pack(fill='x')
#---
root.mainloop()
