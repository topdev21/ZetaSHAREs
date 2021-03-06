import tkinter
class About:
	def __init__(self, parent):
		self.parent = parent
		self.layout()

	def layout(self):
		self.parent.wm_attributes("-disabled", True)

		# Creating the toplevel dialog
		self.toplevel_dialog = tkinter.Toplevel(self.parent)
		self.toplevel_dialog.geometry("300x130+200+200")
		self.toplevel_dialog.resizable(0, 0)
		# Tell the window manager, this is the child widget.
		# Interesting, if you want to let the child window 
		# flash if user clicks onto parent
		self.toplevel_dialog.transient(self.parent)

		x = """developpé par christian Fare\n copyright 2021 zetashare ph.d .inc\n Kara Togo(228) chaminade.inc
		"""
		self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_About)
		tkinter.Label(self.toplevel_dialog, text="ZetaSHARE", font=("Helvetica", 30, "italic"), fg="gray55").pack(fill=tkinter.X, pady=3)

		for line in x.split("\n"):
			tkinter.Label(self.toplevel_dialog, text=line, font=("poppins", 10, "italic"), fg="gray33").pack( fill=tkinter.X)

	def Close_About(self):

		# IMPORTANT!
		self.parent.wm_attributes("-disabled", False) # IMPORTANT!

		self.toplevel_dialog.destroy()

		# Possibly not needed, used to focus parent window again
		self.parent.deiconify()

if __name__ == "__main__":
	pass