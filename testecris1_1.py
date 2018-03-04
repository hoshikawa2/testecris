import ui

def buttonClick(sender):
	print(sender.superview['textfield1'].text)
	print('mensagem enviada')

v = ui.load_view()
v.present('sheet')


