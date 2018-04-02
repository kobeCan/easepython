#coding=utf-8
album = ['Black Start', 'David Bowie', 25, True]
print(album)
album.append('new Song')
print(album)
print(album[0], album[-1])

isIn = 'new Song' in album
print(isIn)

print(bool([]))

print('--------------------------------')

print(1 < 3 and 2 < 5)
print(1 < 3 and 2 > 5)
print(1 < 3 or 2 < 5)
print(1 > 3 or 2 > 5)

print('--------------------------------')
password_list = ['*#*#', '123456']

def account_login():
	pwd = str(input('Password:'))
	password_correct = pwd == password_list[-1]
	password_reset = pwd == password_list[0]


	if password_correct:
		print('Login Success!')
	elif password_reset:
		new_password = str(input('Enter a new password:'));
		print('Your password has changed successfully! ' + new_password)
	else:
		print('Wrong password or invalid input!')
		account_login()

# account_login()

# Loop

for every_letter in 'Hello, Python!':
	print(every_letter)

def addAlgorithm ():
	for i in range(1, 11):
		print('1 + ' + str(i) + ' = ' + str(i + 1))

addAlgorithm()

print('---------------9 & 9 乘法表-----------------')

def ninenine():
	for i in range(1, 10):
		for j in range(1, i+1):
			print '{}*{}={}'.format(j, i, i * j),
	print(' ')

ninenine()