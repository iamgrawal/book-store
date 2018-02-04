"""
A program that stores this information:
Title, Author
Year, ISBN

User can:

View all records
Search an entry
Add entry
Update entry
Delete
Close
"""
from tkinter import *

window = Tk()

title_label = Label(window, text = "Title")
title_label.grid(row = 0, column = 0)

title_text = StringVar()
title_entry = Entry(window, textvariable=title_text)
title_entry.grid(row = 0, column = 1)

author_label = Label(window, text = "Author")
author_label.grid(row = 0, column = 2)

author_text = StringVar()
author_entry = Entry(window, textvariable=author_text)
author_entry.grid(row = 0, column = 3)

year_label = Label(window, text = "Year")
year_label.grid(row = 1, column = 0)

year_text = StringVar()
year_entry = Entry(window, textvariable=year_text)
year_entry.grid(row = 1, column = 1)

isbn_label = Label(window, text = "ISBN")
isbn_label.grid(row = 1, column = 2)

isbn_text = StringVar()
isbn_entry = Entry(window, textvariable=isbn_text)
isbn_entry.grid(row = 1, column = 3)

listBox = Listbox(window)
listBox.grid(row=2, column = 0, rowspan = 6, columnspan = 2)

scrollBar = Scrollbar(window)
scrollBar.grid(row = 2, column = 2, rowspan = 6)

listBox.configure(yscrollcommand = scrollBar.set)
scrollBar.configure(command = listBox.yview)

view_button = Button(window,text="View all", width = 12)
view_button.grid(row = 2, column = 3)

search_button = Button(window,text="Search entry", width = 12)
search_button.grid(row = 3, column = 3)

add_button = Button(window,text="Add entry", width = 12)
add_button.grid(row = 4, column = 3)

update_button = Button(window,text="Update", width = 12)
update_button.grid(row = 5, column = 3)

delete_button = Button(window,text="Delete", width = 12)
delete_button.grid(row = 6, column = 3)

close_button = Button(window,text="Close", width = 12)
close_button.grid(row = 7, column = 3)

window.mainloop()