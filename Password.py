password = input("Введите пароль: ")

def has_digit(password):
	return any (symbol.isdigit() for symbol in password)

def is_very_long(password):
	return len(password) > 12

score = 0

if has_digit(password):
	score = score + 2

if is_very_long(password):
	score = score + 2


print(f"рейтинг пароля {score}")
