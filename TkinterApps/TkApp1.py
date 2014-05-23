from Tkinter import *

class TkApp1(Frame):

	def say_hi(self):
		print 'hi there, everyone!'
		#print self.QUIT.config()
		print 'screen width', self.winfo_screenwidth()
		print 'window width', self.winfo_width()
		print 'window height', self.winfo_height()

	def createWidgets(self):
		self.QUIT = Button(self,
			text = 'QUIT',
			fg = 'red',
			command = self.quit).pack(side = 'left',
				padx = 5, pady = 5)
		
		'''
		#Alternatively...
		self.QUIT['text'] = 'QUIT'
		self.QUIT['fg'] = 'red'
		self.QUIT['command'] = self.quit
		
		self.QUIT.pack({'side': 'left'})
		'''
				
		self.hi_there = Button(self)
		self.hi_there['text'] = "Hello"
		self.hi_there['command'] = self.say_hi
		
		self.hi_there.pack(side = 'left', padx = 5, pady = 5)
		#self.hi_there.pack({'side': 'left'})
		
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master.title("Demo")
		self.pack()
		self.createWidgets()
		
root = Tk()
app = TkApp1(master = root)
app.mainloop()
root.destroy()
