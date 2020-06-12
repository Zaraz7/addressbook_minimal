import re
#строчные переменные{
logo='''\n\n
	┌┐      ┌┐
	├┤      ├<
	││ddress││ook
	┘└──────└┘──---\n\n
'''
h='(для помощи, введите \"help\").\n'
help='''
help		выводит это сообщение
exit		выход
list <страница>	список контактных данных
type		создание/редактирование контакта
find <имя>	поиск контакта
del  <имя>	удалить контакт
info		о программе
'''
e='Недоступная команда '
#} функции{
def E(x):
	print(e+x*h)


#} сама программа{
print(logo)
while True:
	try:
		velue=input()
		o=re.findall(r'\w+', velue)[0]
		if o=='exit':
			break
		elif o=='help':
			print(help)
		elif o=='type':
			E(0)
		elif o=='type':
			E(0)
		elif o=='list':
			E(0)
		elif o=='find':
			E(0)
		elif o=='del':
			E(0)
		elif o=='info':
			E(0)
		else:
			x/=0
	except:
		E(1)
#}.