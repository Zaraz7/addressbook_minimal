#основные переменные{
v="0.9.1"
#file=open('ab', r, w)
ls={'Моя почта': 'zaraz121801@gmail.com', 'VOID': '00000@email.org'}
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
info		о программе
'''

#} функции{
def E():
	print('Недоступная команда.\n(для помощи, введите \"help\").\n')
#} основной алгоритм{
print('\n\n'+logo+'\n\n')
while True:
	try:
		command=input('> ')
		w1=command[:4]
		if w1=='exit':
			break
		elif w1=='help':
			print(help)
		elif w1=='type':
			name=input('Имя контакта: ')
			address=input('Почта или номер телефона: ')
			ls[name]=address
		elif w1=='list':
			for n, a in ls.items():
				print('	{}: {}'.format(n, a))
		elif w1=='info':
			print('{}\nAddressBook\nV {}\n(с) 2020 Terlyk Maksim'.format(logo, v))
		elif w1=='find':
			w2=command[5:]
			if w2 in ls:
				print('	{}: {}'.format(w2, ls[w2]))
			else:
				print('Контакт "{}" не найден\n'.format(w2))
		elif w1=='del ':
			w2=command[4:]
			
			if w2 in ls:
				del ls[w2]
			else:
				print('Контакт "{}" не найден\n'.format(w2))
		else:
			E()
	except:
		E()
#}.