import ui

def clickButton(sender):
	print(sender.superview['textfield1'].text)

v = ui.load_view()
v.present('sheet')
