import ui

def clickButton(sender):
	print(sender.superview['textfield1'].text)
	print('ok3')

v = ui.load_view()
v.present('sheet')
