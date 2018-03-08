import ui

def button1Click(sender):
	v = ui.load_view('testecris')
	v.present('sheet')

v = ui.load_view('mainmenu')
v.present('sheet')
