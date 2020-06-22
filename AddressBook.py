import os
import pickle
import traceback

save_chek=False	# указатель на локальные изменения
#
v="1.2.1"
path='ab.data'	# имя файла данных (битовый)
def load():
	file = open(path, 'rb')
	pickl = pickle.load(file)
	file.close()
	return pickl
if os.access(path, os.F_OK) and os.path.getsize(path) > 0:
	ls=load()
else:
	save_chek = True
	ls = {}
don = False			# 'Debug On'
error_check = False	# Указатель на ошибки 
logo=\
'''		  ┌┐      ┌┐
		  ├┤      ├<
		  ││ddress││ook
		  ┘└──────└┘──---'''
help='''
help		выводит это сообщение
exit		выход
list		список контактных данных
type		создание/редактирование контакта
find <имя>	поиск контакта
del  <имя>	удалить контакт
save		сохранить изменения
info		о программе
debug		включить режим откладки
'''

E = 'Неверная команда.\n'				# - говорит что error
H = 'Для помощи, введите \"help\".\n'	# - рекомендует help

def save():
	file=open(path, 'wb')
	pickle.dump(ls, file)
	file.close()
def line(n, a):
	print('	{}: {}'.format(n, a))
def delit(n):
	del ls[n]
	print('Контак удалён.')
def debug():
	if don:
		print(
'-Значения переменных-\n\
Присутствие измений контактов(save_chek) = {}\n\
Словарь контактов: = {}'.format(save_chek, ls))
		if error_check:
			print('Что-то создает скриптовые ошибки!')
		print('---------------------')

print('\n\n'+logo+'\n\n'+H)
while True:
	debug()
	error_check = False
	try:
		command = input('> ')
		w1 = command[:4]
		if w1 == 'exit':
			if save_chek or (ls!=load()):
				opt = input(' При выходе все несохранённые изменения будут утеряны.\n Продолжить?\n y/n ')
				if opt == 'y':
					break
				else:
					del opt		# opt - optional
			else:	
				break
		elif w1 == 'help':
			print(help)
		elif w1 == 'type':
			name=input('Имя контакта: ')
			address=input('Почта или номер телефона: ')
			ls[name]=address
		elif w1 == 'list':
			if len(ls)>0:
				for n, a in ls.items():
					line(n, a)
			else:
				print('Книга пуста.')
		elif w1 == 'info':
			print('{}\nAddressBook\nV {}\n(с) 2020 Terlyk Maksim.'.format(logo, v))
		elif w1 == 'find':		
			w2=command[5:]
			line(w2, ls[w2])
		elif w1 == 'del ':
			w2 = command[4:]
			delit(w2)			
		elif w1 == 'save':
			save()
			print('Сохранение прошло успешно.')
		elif w1 == 'debu':
			don = not don
		else:
			x/=0
	except KeyError as err:
		print('Контакт "{}" не найден.'.format(w2))
		print(err)
		error_check = True

	except: 
		print(E+H)
		error_check = True