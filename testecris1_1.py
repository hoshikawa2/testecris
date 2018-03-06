import ui

def buttonClick(sender):
	print(sender.superview['textfield1'].text)
	print('ok1')

v = ui.load_view()
v.present('sheet')


