from Tkinter import *
import ttk
#from ttk import Treeview

tree_columns = ("country", "capital", "currency")
tree_data = [
	("Argentina",      "Buenos Aires",     "ARS"),
	("Australia",      "Canberra",         "AUD"),
	("Brazil",         "Brazilia",         "BRL"),
	("Canada",         "Ottawa",           "CAD"),
	("China",          "Beijing",          "CNY"),
	("France",         "Paris",            "EUR"),
	("Germany",        "Berlin",           "EUR"),
	("India",          "New Delhi",        "INR"),
	("Italy",          "Rome",             "EUR"),
	("Japan",          "Tokyo",            "JPY"),
	("Mexico",         "Mexico City",      "MXN"),
	("Russia",         "Moscow",           "RUB"),
	("South Africa",   "Pretoria",         "ZAR"),
	("United Kingdom", "London",           "GBP"),
	("United States",  "Washington, D.C.", "USD")
	]
	
def sortby(tree, col, descending):
	'''Sort tree contents when a column is clicked on.'''
	# grab values to sort
	data = [(tree.set(child, col), child) for child in tree.get_children('')]
	
	# reorder data
	data.sort(reverse = descending)
	for indx, item in enumerate(data):
		tree.move(item[1], '', indx)
		
	# swith the heading so that it will sort
	#in the opposite direction
	tree.heading(col, command = lambda col = col: sortby(tree,
		col, int(not descending)))
	
class treeGui(Frame):
	
	msg = ttk.Label(wraplength = '4i',
		justify = 'left',
		anchor = 'n',
		padding = (10, 2, 10, 6),
		text = ('Ttk is the new Tk themed widget set. '
			'One of the the widgets it includes is a '
			'tree widget, which can be configured to '
			'dispaly the tree itself. This is a simple '
			'way to build a listbox that has multiple '
			'columns. Clicking on the heading for a '
			'column will sort the data by that column. '
			'You can also change the width og the columns'
			' by dragging the boundaries between them.'))
	msg.pack(fill = X)
	
	container = Frame()
	container.pack(fill = BOTH, expand = True)
	
	# Construct scrollbars here for the treeview....
	
	container.grid_columnconfigure(0, weight = 1)
	container.grid_rowconfigure(0, weight = 1)
	
	
	def createWidgets(self, path):
		#Close Button
		self.btnClose = Button(self,
			text = 'Close',
			width = 7,
			fg = 'red',
			command = self.quit)
		self.btnClose.grid(padx = 5,
			pady = 5,
			row = 4,
			column = 1)
		
		#msg
		self.msg = Label(wraplength = '4i',
			justify = 'left',
			anchor = 'n',
			padding = (10, 2, 10, 6),
			text = ('Ttk is the new Tk themed widget set. '
				'One of the the widgets it includes is a '
				'tree widget, which can be configured to '
				'dispaly the tree itself. This is a simple '
				'way to build a listbox that has multiple '
				'columns. Clicking on the heading for a '
				'column will sort the data by that column. '
				'You can also change the width og the columns'
				' by dragging the boundaries between them.'))
		self.msg.pack(fil = X)
	
		#container
		self.container = Frame()
		self.container.pack(fill = BOTH, expand = True)
	
		# Construct scrollbars here for the treeview....
	
		self.container.grid_columnconfigure(0, weight = 1)
		self.grid_rowconfigure(0, weight = 1)
		
	def buildTree(self):
		for col in tree_columns:
			self.tree.heading(col, text = col.title(),
				command = lambda c = col: sortby(self.tree, c, 0))
		for item in tree_data:
			self.tree.insert('', END, values = item)
			
		
		'''	
		#Directory Tree
		self.tree = Treeview(self)
		self.xscr = Scrollbar(self,
			orient = 'horizontal',
			command = self.tree.xview)
		self.yscr = Scrollbar(self,
			orient = 'vertical',
			command = self.tree.yview)
		self.tree.configure(xscroll = self.xscr.set,
			yscroll = self.yscr.set)
		self.tree.heading('#0', text = 'Path', anchor = 'w')
		self.tree.grid(row = 0, column = 0)
		self.xscr.grid(row = 0, column = 1, sticky = 'ns')
		self.yscr.grid(row = 1, column = 0, sticky = 'ew')
		self.grid()
		
	
	def process_directory(self, parent, path):
		for p in os.listdir(path):
			abspath = os.path.join(path, p)
			isdir = os.path.isdir(abspath)
			oid = self.tree.insert(parent, 
				'end', text=p, open=False)
			if isdir:
				self.process_directory(oid, abspath)
	'''

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master.title("Tree Gui")
		self.pack()
		self.tree = None
		self.createWidgets()
		self.buldTree()

def main():	
	root = Tk()	
	root.resizable(0, 0)
	root.geometry('+300+300')
	'''
	path_to_project = '../'
	app = treeGui(root, path_to_project)
	'''
	app.mainloop()
		
if __name__ == '__main__':
	main()
