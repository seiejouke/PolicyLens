"""A policylens for searching and retreiving data from the TweedeKamer API to a local database"""

import tkinter as tk

# Create the root window
root = tk.Tk()
root.configure(bg='white')
# Set the title
root.title("Policy lens")
# Set the root window size
root.geometry('800x600')
root.resizable(False, False)
# Use a label to show the title
title = tk.Label(
    root,
    text='PolicyLens',
    font=('Arial 16 bold'),
    bg='#264A5F',
    fg='#FFFFFF', # root is already set white?
    anchor='w',
    padx=16,
    pady=12
)
title.pack(fill='x')
#---
name_label = tk.Label(
    root,
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
name_label = tk.Label(
    root,
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
search_row = tk.Frame(root, bg='white')
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
#---Input button
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
#------*HBO-ICT-DT Module-2*------#
#              ____               #  
#       _,-ddd888888bbb-._        #
#     d88888888888888888888b      #
#   d888888888888888888888888b    # 
#  6888888888888888888888888889   #
#  68888b8""8q8888888p8""8d88889  #
#  `d8887     p88888q     4888b'  #
#   `d8887    p88888q    4888b'   #
#     `d887   p88888q   488b'     #
#       `d8bod8888888dob8b'       #
#         `d88888888888d'         #
#           `d8888888b'           #
#             `d8888b'            #
#               `bd'              #
#-------------Take-off!-----------# 
root.mainloop()