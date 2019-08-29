

def lprint(msg,*tuple):

	print(msg)
	if len(tuple)>1:
		for obj in tuple:
			print(obj)
	print("结束")