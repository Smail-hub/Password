#a = input()
#
#found_letter = False
#for symbol in a:
#    if symbol.isalpha():
#        found_letter = True
#if found_letter:
#    print("Есть буква!")
#else:
#    print("Нет буквы!")
#
#======================================================================================
#
#a = input()
#
#found_exclamation_mark = False
#found_letter = False
#
#for symbol in a:
#    if symbol == "!":
#        found_exclamation_mark = True
#
#    if symbol.isalpha():
#        found_letter = True
#
#if found_exclamation_mark:
#    print("Есть восклицательный знак!")
#else:
#    print("Нет восклицательного знака!")
#
#if found_letter:
#    print("Есть буква!")
#else:
#    print("Нет буквы!")

#=================================================


def get_vat_and_price_with_vat(price):
    vat_rate = 20
    vat = price * vat_rate / 100
    price_with_vat = price + vat
    return vat, price_with_vat
    
vat, price = get_vat_and_price_with_vat(100)
print(vat)  # 20
print(price)  # 120
