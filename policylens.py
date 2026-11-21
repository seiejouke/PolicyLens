"""Lokale Tkinter-app voor zoeken in fictieve CSV-data met TinyDB-opslag."""

import tkinter as tk
from tkinter import ttk
import csv
from pathlib import Path # for csv
from datetime import datetime # checking and verifying dates for mock searches
from json import JSONDecodeError
from tinydb import TinyDB

# Vaste ontwerpafspraken: beide zoekroutes gebruiken dezelfde grenzen.
MIN_SEARCH_LENGTH = 2
MAX_RETRIEVED_RESULTS = 25
MAX_BURGER_RESULTS = 10

CSV_FILE = Path(__file__).with_name( # Path called from pathlib/Path
    'policylens_mock_tweede_kamer.csv'
)
#---
DATABASE_FILE = Path(__file__).with_name("policy_data.json")
#---
research_documents = []
#Later mogelijk functies in een apart script callen?
def load_mock_document():
    """Lees de fictieve CSV-records als een lijst met dictionaries."""
    with CSV_FILE.open(
        encoding='utf-8-sig', # encoding standard
        newline=''
    ) as csv_file:
        reader= csv.DictReader(csv_file)
        return list(reader)
    
def search_burger():
    """Zoek in titel en onderwerp en toon de beperkte burgerresultaten."""
    term = search_text.get().strip().casefold() 
    #.strip() verwijdert omliggende spaties. .casefold() zorgt dat bijvoorbeeld DATA ook overeenkomt met data

    for item in burger_results.get_children():
        burger_results.delete(item)

    if len(term) < MIN_SEARCH_LENGTH:
        burger_status.set('Vul minimaal twee tekens in.')
        return

    try:
        documents = load_mock_document()
    except (OSError, UnicodeError, csv.Error) as error: # error testing
        burger_status.set(f'CSV kon niet worden gelezen: {error}') # error testing foutmelding
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

    # De nieuwste treffers staan vooraan; Burger toont daarvan een kleinere set.
    retrieved = matches[:MAX_RETRIEVED_RESULTS]
    visible = retrieved[:MAX_BURGER_RESULTS]

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

def search_researcher():
    """Pas onderzoeksfilters toe binnen de nieuwste geselecteerde treffers."""
    term = search_text.get().strip().casefold() # remove empty space and force to lowercase (better searches)
    from_text = from_date_inp.get().strip()
    to_text = to_date_inp.get().strip()
    document_type = document_type_inp.get().strip().casefold()

    display_research_results([])

    if len(term) < MIN_SEARCH_LENGTH: # dezelfde invoergrens als bij Burger
        research_status.set('Vul minimaal twee tekens in.') # Misschien wat te kort? Hoe kom ik hierachter?
        return

    from_date = None
    to_date = None

    try:
        if from_text:
            from_date = datetime.strptime(from_text, '%d-%m-%Y') # dd-mm-jjjj indeling
        if to_text:
            to_date = datetime.strptime(to_text, '%d-%m-%Y')
    except ValueError:
        research_status.set('Gebruik geldige datums als dd-mm-jjjj.')
        return

    if from_date and to_date and from_date > to_date:
        research_status.set('Vanaf datum mag niet na Tot datum liggen')
        return
    
    try:
        documents = load_mock_document()
    except (OSError, UnicodeError, csv.Error) as error: # How does this work exactly? review
        research_status.set(f'CSV kon niet worden gelezen: {error}')
        return

    matches = []

    for document in documents:
        if document['Verwijderd'].casefold() == 'true':
            continue # how does his work exactly? review

        searchable_text = document['Titel'] + ' ' + document['Onderwerp']

        if term in searchable_text.casefold():
            matches.append(document) # If search term and document terms match, we add the doc

    matches.sort(
        key=lambda document: document['Datum'],
        reverse=True
    )
    # Volgens het ontwerp filteren we alleen binnen deze begrensde set.
    retrieved = matches[:MAX_RETRIEVED_RESULTS]
    visible = [] # verzamel hier de documenten die aan alle filters voldoen

    for document in retrieved:
        document_date = datetime.strptime(document['Datum'], '%Y-%m-%d') # why is date in reverse?

        if from_date and document_date < from_date:
            continue # check date search logic 
        if to_date and document_date > to_date:
            continue # more date checking logic
        if document_type and document_type != 'alle soorten':
            if document['Soort'].casefold() != document_type: # Hoe werkt dit?
                continue

        visible.append(document) # add documents after logic function sorting

    display_research_results(visible)

    if visible:
        research_status.set(
            f'{len(visible)} resultaten uit {len(retrieved)} opgehaalde records (fictief).' # hoe werkt dit?            
        )
    else:
        research_status.set(
            'Geen documenten gevondeon met deze zoekterm en filters.'
        )    

def display_research_results(documents):
    research_documents.clear()
    research_documents.extend(documents)

    for item in research_results.get_children():
        research_results.delete(item)

    for document in research_documents:
        research_results.insert(
            "",
            tk.END,
            values=(
                document["Titel"],
                document["Datum"],
                document["Soort"]
            )
        )

def save_research_results(): # data opslag for tinyDB
    if not research_documents:
        research_status.set("Geen resultaten om op te slaan.")
        return

    with TinyDB(DATABASE_FILE, encoding='utf-8') as database:
            table = database.table('documents')
            table.truncate()
            table.insert_multiple(research_documents)

    research_status.set(
        f"{len(research_documents)} documenten opgeslagen."
    )

def load_research_results(): # data ophalen uit tinyDB
    """Laad lokale documenten en behoud vorige resultaten bij een leesfout."""
    try:
        with TinyDB(DATABASE_FILE, encoding='utf-8') as database:
            documents = database.table('documents').all()
    except (OSError, UnicodeError, JSONDecodeError):
        # TinyDB leest JSON: het pad, de codering of de JSON-inhoud kan fout zijn.
        research_status.set("Lokale opslag kon niet worden gelezen.")
        return # stop zonder het bronbestand of de vorige resultaten te vervangen

    # Werk het scherm pas bij nadat het lezen volledig is gelukt.
    display_research_results(documents)

    research_status.set(
        f'Lokale opslag: {len(documents)} documenten geladen. '
        'Zoekterm en filters niet toegepast.'
    )


if __name__ == "__main__": # indent code after
    # Create the root window
    root = tk.Tk()
    root.configure(bg='white')
    search_text = tk.StringVar() # store search text?
    # Set the title
    root.title("Policy lens")
    # Set the root window size
    root.geometry('900x700')
    root.minsize(800, 600)
    root.resizable(True, True) # Need to fit the onderzoeker results!
    # What does the header do?
    header = tk.Frame(root, bg="#193548")
    header.pack(fill="x")
    # Use a label to show the title
    title = tk.Label(
        header, # places the title into the header?
        text="POLICYLENS NL",
        font=("Arial", 16, "bold"),
        bg="#193548",
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

        # Beide knoppen eerst hun gewone kleur geven
        burger_btn.configure(
            bg='#35566A', fg='white',
            activebackground='#35566A', activeforeground='white'
        )
        onderzoek_btn.configure(
            bg='#35566A', fg='white',
            activebackground='#35566A', activeforeground='white'
        )

        # Daarna de knop van de gekozen pagina kleuren
        if page is burger_page:
            burger_btn.configure(
                bg='#117D8D', fg='white',
                activebackground='#117D8D', activeforeground='white'
            )
        else:
            onderzoek_btn.configure(
                bg='#117D8D', fg='white',
                activebackground='#117D8D', activeforeground='white'
            )
    #--- search bar function
    def make_search_bar(parent, text_var, on_search=None):
        search_row = tk.Frame(parent, bg='white')
        search_row.pack(fill="x", padx=22, pady=8)
    #---Search button
        search_btn = tk.Button(
            search_row,
            text='Zoeken',
            command=on_search, # to do !
            bg='#117D8D',
            fg="white",
            activebackground='#117D8D',
            activeforeground='white',
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
        filter_inp.configure( #UI design
            relief='flat',
            borderwidth=0,
            highlightthickness=1,
            highlightbackground='#CBD5DC',
            highlightcolor='#264A5F'
        )
        filter_inp.pack(
            fill='x',
            padx=22,
            pady=(2, 6), # side adjusted to fit search results !
            ipady=3
        )

        return filter_inp
    #---
    onderzoek_btn = tk.Button( # onderzoeker button
        header,
        text='Onderzoeker',
        command=lambda: show_page(onderzoeker_page), # Wait for action until activated
        relief='flat',
        padx=16,
        pady=8
    )
    onderzoek_btn.pack(side='right', padx=8)
    #--- BURGER CONTENT STARTS HERE!
    burger_btn = tk.Button( # burger button
        header,
        text='Burger',
        command=lambda: show_page(burger_page), # Wait for action until activated
        relief='flat',
        padx=16,
        pady=8
    )
    burger_btn.pack(side='right', padx=8)
    #--- 
    name_label = tk.Label( # content for burger
        burger_page,
        text='Vind documenten over data en privacy',
        font=('Arial 16 bold'),
        bg='#FFFFFF', # Using Hex for precise hue's instead of 'white' ! 
        fg='#264A5F',
        anchor='w',
        padx=24,
        pady=24                  
    )
    name_label.pack(fill='x')
    #---
    name_label = tk.Label( # content for burger
        burger_page,
        text='Search for keywords',
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
        text='Onderzoek parlementaire documenten',
        font=('Arial 16 bold'),
        bg='#FFFFFF', 
        fg='#264A5F',
        anchor='w',
        padx=24,
        pady=10
    )
    research_heading.pack(fill='x')
    #--- 
    research_input = make_search_bar(
        onderzoeker_page,
        search_text,
        on_search=search_researcher # added search functionality
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

    research_status = tk.StringVar(
        value='Zoek in fictieve CSV-data. Lege filters worden niet toegepast.' # error testing
    )

    research_status_label = tk.Label(
        onderzoeker_page,
        textvariable=research_status,
        bg='#FFFFFF',
        fg='#264A5F',
        anchor='w'
    )
    research_status_label.pack(
        fill='x',
        padx=22,
        pady=(4, 8)
    )

    ttk.Button(
        onderzoeker_page,
        text='Bewaar resultaten lokaal',
        command=save_research_results
    ).pack(anchor='w', padx=22, pady=4)

    ttk.Button(
        onderzoeker_page,
        text='Laad opgeslagen data',
        command=load_research_results
    ).pack(anchor='w', padx=22, pady=4)

    research_results_frame = tk.Frame(
        onderzoeker_page,
        bg='#FFFFFF'
    )
    research_results_frame.pack(
        fill='both',
        expand=True,
        padx=22,
        pady=(0, 12)
    )

    research_results = ttk.Treeview( # How does this work exactly? review!
        research_results_frame,
        columns=('Titel', 'Datum', 'Soort'),
        show='headings',
        height=6
    )

    research_results.heading('Titel', text='Titel')
    research_results.heading('Datum', text='Datum')
    research_results.heading('Soort', text='Documentsoort')

    research_results.column('Titel', width=450)
    research_results.column('Datum', width=110, stretch=False)
    research_results.column('Soort', width=150, stretch=False)

    research_scrollbar = ttk.Scrollbar(
        research_results_frame,
        orient='vertical',
        command=research_results.yview
    )
    research_scrollbar.pack(
        side='right',
        fill='y'
    )

    research_results.configure(
        yscrollcommand=research_scrollbar.set
    )
    research_results.pack(
        side='left',
        fill='both',
        expand=True
    )

    show_page(burger_page)
    #---
    root.mainloop()
