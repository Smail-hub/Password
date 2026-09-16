password = input("Введите пароль: ")

def has_digit(password):
	return any (symbol.isdigit() for symbol in password)

def is_very_long(password):
	return len(password) > 12

def has_letters(password):
	return any (symbol.isalpha() for symbol in password)

def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)

def has_lower_letters(password):
	return any(symbol.islower() for symbol in password)

checks = [
	has_digit, is_very_long, has_letters,
	has_upper_letters, has_lower_letters
]

score = 0

for checks in checks:
	if checks(password):
		score += 2
#if has_digit(password):
#	score = score + 2
#
#if is_very_long(password):
#	score = score + 2
#
#if has_letters(password):
#	score = score + 2
#
#if has_upper_letters(password):
#	score = score + 2
#
print(f"Рейтинг пароля: {score}")
