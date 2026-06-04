def has_digit(text):
    return any (sumbol.isdigit() for sumbol in text)

a = input("Введите текст: ")
if has_digit(a):
    print("Есть цифры")
else:
    print("Нет цифр")
======================================================

def is_very_long():
    password_len = len(a)
    
    
print(password_len)
