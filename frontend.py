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
from backend import Database

class Frontend:
		
	def get_selected_row(self,event):
		self.selected_tuple
		try:
			self.index = listBox.curselection()[0]
			self.selected_tuple = listBox.get(index)
			self.title_entry.delete(0,END)
			self.title_entry.insert(END,selected_tuple[1])
			self.author_entry.delete(0,END)
			self.author_entry.insert(END,selected_tuple[2])
			self.year_entry.delete(0,END)
			self.year_entry.insert(END,selected_tuple[3])
			self.isbn_entry.delete(0,END)
			self.isbn_entry.insert(END,selected_tuple[4])
		except IndexError:
			pass

	def view_command(self):
		self.listBox.delete(0,END)
		for row in dt.view():
			self.listBox.insert(END,row)

	def search_command(self):
		self.listBox.delete(0,END)
		for row in dt.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
			self.listBox.insert(END,row)

	def add_command(self):
		self.listBox.delete(0,END)
		self.dt.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
		self.listBox.insert(END,(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

	def update_command(self):
		self.dt.update(self.selected_tuple[0],self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())

	def delete_command(self):
		self.listBox.delete(0,END)
		self.dt.delete(self.selected_tuple[0])

	def close_command(self):
		self.window.destroy()

	def create_window(self):
		self.title_label = Label(window, text = "Title")
		self.title_label.grid(row = 0, column = 0)

		self.title_text = StringVar()
		self.title_entry = Entry(window, textvariable=self.title_text)
		self.title_entry.grid(row = 0, column = 1)

		self.author_label = Label(window, text = "Author")
		self.author_label.grid(row = 0, column = 2)

		self.author_text = StringVar()
		self.author_entry = Entry(window, textvariable=self.author_text)
		self.author_entry.grid(row = 0, column = 3)

		self.year_label = Label(window, text = "Year")
		self.year_label.grid(row = 1, column = 0)

		self.year_text = StringVar()
		self.year_entry = Entry(window, textvariable=self.year_text)
		self.year_entry.grid(row = 1, column = 1)

		self.isbn_label = Label(window, text = "ISBN")
		self.isbn_label.grid(row = 1, column = 2)

		self.isbn_text = StringVar()
		self.isbn_entry = Entry(window, textvariable=self.isbn_text)
		self.isbn_entry.grid(row = 1, column = 3)

		self.listBox = Listbox(window, width = 80, height = 20)
		self.listBox.grid(row=2, column = 0, rowspan = 6, columnspan = 2)

		self.scrollBar = Scrollbar(window)
		self.scrollBar.grid(row = 2, column = 2, rowspan = 6)

		self.listBox.configure(yscrollcommand = self.scrollBar.set)
		self.scrollBar.configure(command = self.listBox.yview)

		self.listBox.bind('<<ListboxSelect>>',self.get_selected_row)

		self.view_button = Button(window,text="View all", width = 12, command = self.view_command)
		self.view_button.grid(row = 2, column = 3)

		self.search_button = Button(window,text="Search entry", width = 12, command = self.search_command)
		self.search_button.grid(row = 3, column = 3)

		self.add_button = Button(window,text="Add entry", width = 12, command = self.add_command)
		self.add_button.grid(row = 4, column = 3)

		self.update_button = Button(window,text="Update", width = 12, command = self.update_command)
		self.update_button.grid(row = 5, column = 3)

		self.delete_button = Button(window,text="Delete", width = 12, command = self.delete_command)
		self.delete_button.grid(row = 6, column = 3)

		self.close_button = Button(window,text="Close", width = 12, command = self.close_command)
		self.close_button.grid(row = 7, column = 3)

	def __init__(self,window,dt):
		self.window = window
		self.window.wm_title("BookStore")
		self.create_window()
		self.dt = Database("books.db")

window = Tk()
dt = Database("books.db")
Frontend(window,dt)
window.mainloop()