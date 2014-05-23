from Tkinter import *
import gtk
import random
import globalvars

class GuessingGame(Frame):

	answer = 0
	
	def initAnswer(self):
		self.answer = random.randrange(100) + 1
		
	def onGuess(self, e):
		#globalvars.printest()
		#print globalvars.answer
		guess = self.entGuess.get()
		if (len(guess) == 0):
			message = "You forgot to make a guess\n"
		else:
			guess = int(guess)
			if (self.answer > guess):
				message = ': try greater\n'
			elif (self.answer< guess):
				message = ': try smaller\n'
			else:
				message = ': bingo!!\n'
		self.txtConsole.insert(END, str(guess) + message)
		self.entGuess.delete(0, END)
		
	def onClear(self, e):
		self.txtConsole.delete(1.0, END)
		self.entGuess.delete(0, END)
		
	def onQuit(self, e):
		message = "The answer is: " + str(self.answer) + '\n'
		self.txtConsole.delete(1.0, END)
		self.txtConsole.insert(END, message)
		
	def onRestart(self, e):
		self.onClear(e)
		self.initAnswer()
		
	def createWidgets(self):	
	
		#Guess text box
		self.entGuess = Entry(self,
			width = 24
			)
		self.entGuess.grid(padx = 5, 
			pady = 5,
			row = 0,
			column = 0)
			
	
		#Guess Button
		self.btnGuess = Button(self,
			text = 'Guess',
			width = 7)
		self.btnGuess.grid(padx = 5,
			pady = 5,
			row = 0,
			column = 1)
		self.btnGuess.bind('<Button-1>', self.onGuess)
		
		#Results Console
		self.txtConsole = Text(self,
			width = 27,
			height = 10)
		self.txtConsole.grid(padx = 5,
			pady = 5,
			row = 1,
			column = 0,
			rowspan = 4)
		
		#Quit Button
		self.btnQuit = Button(self,
			text = 'Quit',
			width = 7)
		self.btnQuit.grid(padx = 5,
			pady = 5,
			row = 1,
			column = 1)
		self.btnQuit.bind('<1>', self.onQuit)
		
		#Restart Button
		self.btnRestart = Button(self,
			text = 'Restart',
			width = 7)
		self.btnRestart.grid(padx = 5,
			pady = 5,
			row = 2,
			column = 1)
		self.btnRestart.bind('<Button-1>', self.onRestart)
		
		#Clear Button
		self.btnClear = Button(self,
			text = 'Clear',
			width = 7)
		self.btnClear.grid(padx = 5,
			pady = 5,
			row = 3,
			column = 1)
		self.btnClear.bind('<1>', self.onClear)
		
		#Close Button
		self.btnClose = Button(self,
			text = 'Close',
			width = 7,
			command = self.quit)
		self.btnClose.grid(padx = 5,
			pady = 5,
			row = 4,
			column = 1)
			
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master.title("Guessing Game")
		self.pack()
		self.createWidgets()
		self.entGuess.focus()
		self.initAnswer()

def main():	
	root = Tk()	
	root.resizable(0, 0)
	root.geometry('+300+300')
	app = GuessingGame(root)
	app.mainloop()
		
if __name__ == '__main__':
	main()
