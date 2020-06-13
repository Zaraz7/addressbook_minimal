import re
#основные переменные{
v="0.1.1"
logo=\
'''		  ┌┐      ┌┐
		  ├┤      ├<
		  ││ddress││ook
		  ┘└──────└┘──---'''
help='''
help		выводит это сообщение
exit		выход
list <страница>	список контактных данных
type		создание/редактирование контакта
find <имя>	поиск контакта
del  <имя>	удалить контакт
info		о программе
'''
e=' Недоступная команда.\n'
h='(для помощи, введите \"help\").\n'
#} функции{
def E(x):
	print(e+x*h)


#} сама программа{
print('\n\n'+logo+'\n\n')
while True:
	try:
		velue=input('> ')
		o=re.findall(r'\w+', velue)[0]
		if o=='exit':
			break
		elif o=='help':
			print(help)
		elif o=='type':
			E(0)
		elif o=='list':
			E(0)
		elif o=='find':
			E(0)
		elif o=='del':
			E(0)
		elif o=='info':
			print('{}\nAddressBook\nV {}\n(с) 2020 Terlyk Maksim'.format(logo, v))
		else:
			E(1)
	except:
		E(1)
#}.