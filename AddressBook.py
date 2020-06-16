import os
import pickle
#
save_chek=False
#
v="1.2.0"
path='ab.data'
def load():
	file=open(path, 'rb')
	pickl=pickle.load(file)
	file.close()
	return pickl
if os.access(path, os.F_OK) and os.path.getsize(path) > 0:
	ls=load()
else:
	save_chek=True
	ls={}
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
debug		включить ркжим откладки
info		о программе
'''
E='Неверная команда.\n'
H='Для помощи, введите \"help\".\n'
#
def save():
	file=open(path, 'wb')
	pickle.dump(ls, file)
	file.close()
def line(n, a):
	print('	{}: {}'.format(n, a))
def find(n, action):
	if n in ls:
		action
	else:
		print('Контакт "{}" не найден.'.format(n))
def delit(n):
	del ls[n]
	print('Контак удалён.')
#
print('\n\n'+logo+'\n\n'+H)
while True:
	try:
		command=input('> ')
		w1=command[:4]
		if w1=='exit':
			if save_chek or (ls!=load()):
				opt=input(' При выходе все несохранённые изменения будут утеряны.\n Продолжить?\n y/n ')
				if opt=='y':
					break
				else:
					del opt
			else:	
				break
		elif w1=='help':
			print(help)
		elif w1=='type':
			name=input('Имя контакта: ')
			address=input('Почта или номер телефона: ')
			ls[name]=address
		elif w1=='list':
			if len(ls)>0:
				for n, a in ls.items():
					line(n, a)
			else:
				print('Книга пуста.')
		elif w1=='info':
			print('{}\nAddressBook\nV {}\n(с) 2020 Terlyk Maksim.'.format(logo, v))
		elif w1=='find':		
			w2=command[5:]
			find(w2, (line(w2, ls[w2])))
		elif w1=='del ':
			w2=command[4:]
			delit(w2)			
		elif w1=='save':
			save()
			print('Сохранение прошло успешно.')
		else:
			x/=0
	except KeyError:
		print('Контакт "{}" не найден.'.format(w2))
	except: 
		print(E+H)
