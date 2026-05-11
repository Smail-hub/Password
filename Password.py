Password = input("Введите пароль: ")

Password_len = len(Password)

if Password_len < 13:
	print("Короткий")
if Password_len > 12:
	print("Длинный")

for text in Password:
	print(text)
	if text.isdigit():
		print("-Цифра")
	if text.isalpha():
		print("-Буква")
print("Длинна пароля:", Password_len)