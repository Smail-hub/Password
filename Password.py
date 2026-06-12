password = input("Введите пароль: ")

def has_digit(password):
	return any (symbol.isdigit() for symbol in password)

def is_very_long(password):
	return len(password) > 12

print(has_digit(password))
print(is_very_long(password))
