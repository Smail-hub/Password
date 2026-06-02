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

def return_interrupt_example():
    print('Это фраза всегда будет печататься на экране')
    somevalue = 1000
    return somevalue
    print(somevalue)
    
return_interrupt_example()
