password = input("Введите пароль: ")

#password_len = len(password)
#
#if password_len < 13:
#	print("Короткий")
#elif password_len > 12:
#	print("Длинный")
#
#found_digit = False
#
#for symbol in password:
#	if symbol.isdigit():
#		found_digit = True
#if found_digit:
#	print("Есть цифры")
#else:
#	print("Нет цифр")

def has_digit(password):
	found_digit = False
	
	for symbol in password:
		if symbol.isdigit():
			found_digit = True
	if found_digit:
		print("Есть цифры")
	else:
		print("Нет цифр")

def is_very_long(password):
	password_len = len(password)
	
	if password_len < 13:
		print("Короткий")
	elif password_len > 12:
		print("Длинный")

print (has_digit(password))
print (is_very_long(password))
