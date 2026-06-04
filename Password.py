password = input("Введите пароль: ")

def has_digit(password):
	return any (symbol.isdigit() for symbol in password)

if has_digit(password):
	print("Есть цифра")
else:
	print("Нет цифр") 

def is_very_long(password):
	password_len = len(password)

	if password_len < 13:
		print("Короткий")
	elif password_len > 12:
		print("Длинный")

has_digit(password)
is_very_long(password)
