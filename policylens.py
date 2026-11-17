"""A policylens for searching and retreiving data from the TweedeKamer API to a local database"""

import tkinter as tk
from tkinter import ttk
import csv
from pathlib import Path

CSV_FILE = Path(__file__).with_name( # Path called from pathlib/Path
    'policylens_mock_tweede_kamer.csv'
)

def load_mock_document():
    with CSV_FILE.open(
        encoding='utf-8-sig', # what is this?
        newline=''
    ) as csv_file:
        reader= csv.DictReader(csv_file)
        return list(reader)
def search_burger():
    term = search_text.get().strip().casefold() 
    #.strip() verwijdert omliggende spaties. .casefold() zorgt dat bijvoorbeeld DATA ook overeenkomt met data

    for item in burger_results.get_children():
        burger_results.delete(item)

    if len(term) < 2:
        burger_status.set('Vul minimaal twee tekens in.')
        return

    try:
        documents = load_mock_document()
    except (OSError, UnicodeError, csv.Error) as error:
        burger_status.set(f'CSV kon niet worden gelezen: {error}')
        return

    matches = []

    for document in documents:
        if document['Verwijderd'].casefold() == 'true':
            continue

        searchable_text = (
            document['Titel'] + ' ' + document['Onderwerp']
        )

        if term in searchable_text.casefold():
            matches.append(document)

    matches.sort(
        key=lambda document: document['Datum'],
        reverse=True
    )

    retrieved = matches[:25]
    visible = retrieved[:10]

    for document in visible:
        burger_results.insert(
            '',
            tk.END,
            values=(
                document['Titel'],
                document['Datum'],
                document['Soort']
         )
    )

    if visible:
        burger_status.set(
            f'Fictieve CSV-data: {len(visible)} resultaten getoond.'
        )
    else:
        burger_status.set('Geen documenten gevonden.')

    
# Create the root window
root = tk.Tk()
root.configure(bg='white')
search_text = tk.StringVar() # store search text?
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
def make_search_bar(parent, text_var, on_search=None):
    search_row = tk.Frame(parent, bg='white')
    search_row.pack(fill="x", padx=22, pady=8)
#---Search button
    search_btn = tk.Button(
        search_row,
        text='Zoeken',
        command=on_search,
        bg='#264A5F',
        fg="white",
        relief="flat",
        padx=20
    )
    search_btn.pack(side='right', fill='y', padx=(10, 0))
#---Entry field
    name_inp = tk.Entry(
        search_row,
        textvariable=text_var, # what does this do? | connect entry to the variable passed into the function?
        font=('Arial', 16, 'bold'),
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
#---  Onderzoeker search bar function
def make_search_bar_onderzoeker(parent, label_text):
    filter_label = tk.Label(
        parent,
        text=label_text,
        bg='#FFFFFF'
    )
    filter_label.pack(
        anchor='w',
        padx=22
    )
    filter_inp = tk.Entry(
        parent,
        font=('Arial', 12),
        insertbackground='#264A5F',
        insertwidth=3
    )
    filter_inp.configure(
        relief='flat',
        borderwidth=0,
        highlightthickness=1,
        highlightbackground='#CBD5DC',
        highlightcolor='#264A5F'
    )
    filter_inp.pack(
        fill='x',
        padx=22,
        pady=(4, 12),
        ipady=6
    )

    return filter_inp
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
burger_input = make_search_bar(
    burger_page,
    search_text,
    on_search=search_burger
)

burger_status = tk.StringVar(
    value='Zoek in de fictieve CSV-data.'
)

burger_status_label = tk.Label(
    burger_page,
    textvariable=burger_status,
    bg='#FFFFFF',
    fg='#264A5F',
    anchor='w'
)
burger_status_label.pack(
    fill='x',
    padx=22,
    pady=(4, 8)
)

burger_results = ttk.Treeview(
    burger_page,
    columns=('Titel', 'Datum', 'Soort'),
    show='headings',
    height=10
)

burger_results.heading('Titel', text='Titel')
burger_results.heading('Datum', text='Datum')
burger_results.heading('Soort', text='Documentsoort')

burger_results.column('Titel', width=450)
burger_results.column('Datum', width=110, stretch=False)
burger_results.column('Soort', width=150, stretch=False)

burger_results.pack(
    fill='both',
    expand=True,
    padx=22,
    pady=(0, 12)
)

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
research_input = make_search_bar(
    onderzoeker_page,
    search_text
)
#--- Onderzoeker filters from function
from_date_inp = make_search_bar_onderzoeker(
    onderzoeker_page,
    'Vanaf datum (dd-mm-jjjj)'
)

to_date_inp = make_search_bar_onderzoeker(
    onderzoeker_page,
    'Tot datum (dd-mm-jjjj)'
)

document_type_inp = make_search_bar_onderzoeker(
    onderzoeker_page,
    'Documenttype'
)

show_page(burger_page)
#---
root.mainloop()