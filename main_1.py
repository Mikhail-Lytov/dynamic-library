from ctypes import *
import os

libs = []
name = "pushkin.so"
text = None

libs = [ os.path.join(root, path) for root, dirs, files in os.walk("./") for path in files if path.endswith(name) ] # поиск библиотек в текущей директории и во всех её поддиректориях

if len(libs) > 0:
	for lib_path in libs: # загрузим каждую библиотеку 
		try:
			func = CDLL(lib_path)
			pushkin = func.pushkin

			pushkin.argtype = c_char_p	# принимает
			pushkin.restype = c_char_p	# возвращает
			
		except Exception as err:
			print("не загрузил функцию(")
			
		try:
			res = string_at(pushkin(text))	# передача в библиотеку
			print(res.decode('utf-8'))		# возвращает из библиотке 
		except Exception as err:
			print("не выгрузил (") 
else:
	print("нету библиотек")