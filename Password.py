password = input("Введите пароль: ")

password_len = len(password)

if password_len < 13:
	print("Короткий")
elif password_len > 12:
	print("Длинный")

for text in password:
	if text.isdigit():
		print(text, "- Цифра")
	if text.isalpha():
		print(text, "- Буква")
print("Длина пароля:", password_len)