import os
import pickle
#
v="1.0.0"
path='ab.data'
if os.access(path, os.F_OK) and os.path.getsize(path) > 0:
	file=open(path, 'rb')
	ls=pickle.load(file)
	file.close()
else:
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
info		о программе
'''
#
def E():
	print('Неверная команда.\n(для помощи, введите \"help\").\n')
def save():
	file=open(path, 'wb')
	pickle.dump(ls, file)
	file.close()
#
print('\n\n'+logo+'\n\n')
while True:
	try:
		command=input('> ')
		w1=command[:4]
		if w1=='exit':
			opt=input(' При выходе все несохранённые изменения будут утеряны.\n Продолжить?\n yes/no: ')
			if opt=='yes':
				break
			else:
				del opt
		elif w1=='help':
			print(help)
		elif w1=='type':
			name=input('Имя контакта: ')
			address=input('Почта или номер телефона: ')
			ls[name]=address
		elif w1=='list':
			if len(ls)>0:
				for n, a in ls.items():
					print('	{}: {}'.format(n, a))
			else:
				print('Книга пока пуста')
		elif w1=='info':
			print('{}\nAddressBook\nV {}\n(с) 2020 Terlyk Maksim.'.format(logo, v))
		elif w1=='find':
			w2=command[5:]
			if w2 in ls:
				print('	{}: {}'.format(w2, ls[w2]))
			else:
				print('Контакт "{}" не найден.'.format(w2))
		elif w1=='del ':
			w2=command[4:]
			if w2 in ls:
				del ls[w2]
			else:
				print('Контакт "{}" не найден.'.format(w2))
		elif w1=='save':
			save()
			print('Сохранение прошло успешно.')
		else:
			E()
	except:
		E()

