import ui

def clickButton(sender):
	print(sender.superview['textfield1'].text)
	print('ok8')

v = ui.load_view()
v.present('sheet')
